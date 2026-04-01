#!/usr/bin/env python3
"""
SimulationCraft talent string codec.

Decodes and encodes SimC base64 talent hash strings, matching the format
in engine/player/player.cpp (generate_traits_hash / parse_traits_hash).

Encoding format:
  - Base64 alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
  - Bits packed LSB-first within each 6-bit character
  - Header: version(8b, value=2) + spec_id(16b) + tree_hash(128b, 0-filled)
  - Per node (ascending id_node order):
      selected(1b) -> if 1:
        purchased(1b) -> if 0: granted at rank 1; if 1:
          partially_ranked(1b) -> if 1: rank(6b)
          is_choice(1b) -> if 1: choice_index(2b)

Node types:
  NODE_TIERED (1): max_rank = sum of all entries' max_ranks, rank = sum
  NODE_CHOICE (2) / NODE_SELECTION (4): choice_index = index in entries list
"""

from collections import OrderedDict

# SimC base64 alphabet
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Constants matching SimC
LOADOUT_SERIALIZATION_VERSION = 2
VERSION_BITS = 8
SPEC_BITS = 16
TREE_BITS = 128
RANK_BITS = 6
CHOICE_BITS = 2
BYTE_SIZE = 6  # bits per base64 character

# Node types
# SimC enum trait_node_type_e (from sc_enums.hpp):
NODE_TIERED = 1
NODE_CHOICE = 2
NODE_SELECTION = 3  # hero sub-tree selection (NOT 4 — there is no type 4)


class BitReader:
    """Reads bits LSB-first from a SimC base64 talent string."""

    def __init__(self, talent_str):
        self.data = talent_str
        self.head = 0
        if talent_str:
            pos = BASE64_CHARS.find(talent_str[0])
            if pos == -1:
                raise ValueError(f"Invalid base64 character: {talent_str[0]}")
            self.byte = pos
        else:
            self.byte = 0

    def get_bits(self, bits):
        val = 0
        for i in range(bits):
            bit = self.head % BYTE_SIZE
            self.head += 1
            val += ((self.byte >> bit) & 1) << min(i, 63)
            if bit == BYTE_SIZE - 1:
                char_idx = self.head // BYTE_SIZE
                if char_idx >= len(self.data):
                    self.byte = 0
                else:
                    pos = BASE64_CHARS.find(self.data[char_idx])
                    if pos == -1:
                        raise ValueError(f"Invalid base64 character: {self.data[char_idx]}")
                    self.byte = pos
        return val


class BitWriter:
    """Writes bits LSB-first into a SimC base64 talent string."""

    def __init__(self):
        self.result = []
        self.head = 0
        self.byte = 0

    def put_bits(self, bits, value):
        for i in range(bits):
            bit = self.head % BYTE_SIZE
            self.head += 1
            self.byte += ((value >> min(i, 63)) & 1) << bit
            if bit == BYTE_SIZE - 1:
                self.result.append(BASE64_CHARS[self.byte])
                self.byte = 0

    def finish(self):
        if self.head % BYTE_SIZE:
            self.result.append(BASE64_CHARS[self.byte])
        return "".join(self.result)


def _get_node_info(entries):
    """Extract node_type, max_rank, and is_choice from a node's entries list.

    Args:
        entries: list of (trait_data_like, rank) pairs.
                 trait_data_like must have .node_type and .max_ranks attributes.

    Returns:
        (node_type, max_rank, is_choice)
    """
    if not entries:
        return (0, 0, False)

    node_type = entries[0][0].node_type
    is_choice = node_type in (NODE_CHOICE, NODE_SELECTION)

    if node_type == NODE_TIERED:
        max_rank = sum(e[0].max_ranks for e in entries)
    else:
        max_rank = entries[0][0].max_ranks

    return (node_type, max_rank, is_choice)


def decode_talent_string(talent_str, tree_nodes):
    """Decode a SimC base64 talent string.

    Args:
        talent_str: The base64 talent hash string.
        tree_nodes: OrderedDict keyed by id_node (ascending order).
                    Values are lists of (trait_data, rank) pairs where trait_data
                    has attributes: node_type, max_ranks, id_trait_node_entry.
                    The rank field in tree_nodes is the default/initial rank (usually 0).

    Returns:
        (spec_id, selections) where selections is a dict mapping
        node_id -> (rank, choice_index). choice_index is -1 for non-choice nodes.

    Raises:
        ValueError: On invalid input.
    """
    for ch in talent_str:
        if ch not in BASE64_CHARS:
            raise ValueError(f"Invalid character '{ch}' in talent string")

    min_chars = (VERSION_BITS + SPEC_BITS + TREE_BITS + BYTE_SIZE - 1) // BYTE_SIZE
    if len(talent_str) < min_chars:
        raise ValueError(f"Talent string too short: {len(talent_str)} < {min_chars}")

    reader = BitReader(talent_str)

    version = reader.get_bits(VERSION_BITS)
    if version != LOADOUT_SERIALIZATION_VERSION:
        raise ValueError(f"Invalid serialization version: {version}")

    spec_id = reader.get_bits(SPEC_BITS)
    # Known WoW spec IDs: classic specs 62-581, Midnight new specs up to ~1500
    # Devourer=1480, Evoker Devastation=1467, Evoker Augmentation=1473
    if spec_id == 0 or spec_id > 2000:
        raise ValueError(
            f"Invalid spec_id {spec_id} decoded from talent string header: "
            f"expected a non-zero value (got {spec_id})"
        )

    tree_hash = reader.get_bits(TREE_BITS)  # tree hash — must be all-zeros in valid strings
    if tree_hash != 0:
        raise ValueError(
            f"Non-zero tree hash detected in talent string header (got 0x{tree_hash:032x}). "
            f"The talent string appears to be corrupt or from an incompatible source."
        )

    selections = {}
    _purchased_flags = {}  # Track original purchased bits for round-trip fidelity

    for node_id, entries in tree_nodes.items():
        selected = reader.get_bits(1)
        if not selected:
            continue

        node_type, max_rank, is_choice = _get_node_info(entries)
        rank = max_rank
        choice_index = -1

        purchased = reader.get_bits(1)
        _purchased_flags[node_id] = purchased
        if not purchased:
            # Granted node, rank 1
            rank = 1
        else:
            # Check partial rank
            partial = reader.get_bits(1)
            if partial:
                rank = reader.get_bits(RANK_BITS)

            # Check choice
            is_choice_bit = reader.get_bits(1)
            if is_choice_bit:
                choice_index = reader.get_bits(CHOICE_BITS)

        selections[node_id] = (rank, choice_index)

    return spec_id, selections, _purchased_flags


def encode_talent_string(selections, tree_nodes, spec_id, purchased_flags=None):
    """Encode talent selections into a SimC base64 talent string.

    Args:
        selections: dict of node_id -> (rank, choice_index).
                    choice_index should be -1 or None for non-choice nodes.
        tree_nodes: OrderedDict keyed by id_node (ascending order).
                    Values are lists of (trait_data, rank) pairs.
        spec_id: The specialization ID (integer).
        purchased_flags: optional dict of node_id -> purchased_bit (0 or 1)
                        from a previous decode. When provided, these override
                        the is_granted heuristic for round-trip fidelity.

    Returns:
        The encoded base64 talent string.
    """
    writer = BitWriter()

    writer.put_bits(VERSION_BITS, LOADOUT_SERIALIZATION_VERSION)
    writer.put_bits(SPEC_BITS, spec_id)
    writer.put_bits(TREE_BITS, 0)  # tree hash, 0-filled

    for node_id, entries in tree_nodes.items():
        if node_id not in selections:
            writer.put_bits(1, 0)  # not selected
            continue

        rank, choice_index = selections[node_id]
        if choice_index is None:
            choice_index = -1

        if rank <= 0:
            writer.put_bits(1, 0)  # not selected
            continue

        node_type, max_rank, is_choice = _get_node_info(entries)

        writer.put_bits(1, 1)  # selected

        # Determine if this node was purchased.
        # If we have the original purchased flags (from decode), use those
        # for perfect round-trip. Otherwise, use is_granted heuristic.
        if purchased_flags is not None and node_id in purchased_flags:
            is_purchased = purchased_flags[node_id]
        else:
            is_granted = False
            if is_choice:
                idx = max(choice_index, 0)
                if idx < len(entries):
                    entry_data = entries[idx][0]
                    is_granted = _check_granted(entry_data)
            else:
                if entries:
                    is_granted = _check_granted(entries[0][0])
            init_rank = 1 if is_granted else 0
            is_purchased = 1 if rank > init_rank else 0

        if not is_purchased:
            writer.put_bits(1, 0)  # not purchased (granted)
            continue

        writer.put_bits(1, 1)  # purchased

        # Partial rank
        if rank == max_rank:
            writer.put_bits(1, 0)  # full rank
        else:
            writer.put_bits(1, 1)  # partial
            writer.put_bits(RANK_BITS, rank)

        # Choice
        if is_choice:
            writer.put_bits(1, 1)
            writer.put_bits(CHOICE_BITS, max(choice_index, 0))
        else:
            writer.put_bits(1, 0)

    return writer.finish()


def _check_granted(trait_data):
    """Check if a trait_data object represents a granted (baseline) talent.

    Supports multiple interfaces:
      - trait_data.is_granted (bool attribute)
      - trait_data.is_granted() (callable)
      - Always returns False if neither is available.
    """
    if hasattr(trait_data, 'is_granted'):
        val = trait_data.is_granted
        if callable(val):
            return val()
        return bool(val)
    return False


def validate_roundtrip(talent_str, tree_nodes):
    """Validate that decoding then re-encoding produces the same string.

    Args:
        talent_str: Original talent string.
        tree_nodes: OrderedDict of tree node data.

    Returns:
        (success, message) tuple.
    """
    try:
        spec_id, selections = decode_talent_string(talent_str, tree_nodes)
        reencoded = encode_talent_string(selections, tree_nodes, spec_id)

        if reencoded == talent_str:
            return True, "Round-trip successful"
        else:
            # Find first difference
            min_len = min(len(talent_str), len(reencoded))
            diff_pos = min_len
            for i in range(min_len):
                if talent_str[i] != reencoded[i]:
                    diff_pos = i
                    break
            return False, (
                f"Round-trip mismatch at position {diff_pos}.\n"
                f"  Original:  {talent_str[:80]}{'...' if len(talent_str) > 80 else ''}\n"
                f"  Reencoded: {reencoded[:80]}{'...' if len(reencoded) > 80 else ''}\n"
                f"  Original length:  {len(talent_str)}\n"
                f"  Reencoded length: {len(reencoded)}"
            )
    except Exception as e:
        return False, f"Error during round-trip: {e}"


# ---------------------------------------------------------------------------
# Standalone test with mock data
# ---------------------------------------------------------------------------

class _MockTraitData:
    """Minimal trait data object for testing."""
    def __init__(self, node_type=0, max_ranks=1, id_trait_node_entry=0, is_granted_val=False):
        self.node_type = node_type
        self.max_ranks = max_ranks
        self.id_trait_node_entry = id_trait_node_entry
        self.is_granted = is_granted_val


def _test_bitstream():
    """Test that BitWriter and BitReader are inverse operations."""
    print("Testing bitstream round-trip...")

    writer = BitWriter()
    writer.put_bits(8, 2)       # version
    writer.put_bits(16, 1234)   # spec_id
    writer.put_bits(128, 0)     # tree hash

    # A few test nodes
    writer.put_bits(1, 1)   # selected
    writer.put_bits(1, 1)   # purchased
    writer.put_bits(1, 0)   # full rank
    writer.put_bits(1, 0)   # not choice

    writer.put_bits(1, 0)   # not selected

    writer.put_bits(1, 1)   # selected
    writer.put_bits(1, 1)   # purchased
    writer.put_bits(1, 1)   # partial
    writer.put_bits(6, 3)   # rank=3
    writer.put_bits(1, 1)   # choice
    writer.put_bits(2, 1)   # choice_index=1

    encoded = writer.finish()
    print(f"  Encoded: {encoded}")

    reader = BitReader(encoded)
    assert reader.get_bits(8) == 2
    assert reader.get_bits(16) == 1234
    assert reader.get_bits(128) == 0

    assert reader.get_bits(1) == 1  # selected
    assert reader.get_bits(1) == 1  # purchased
    assert reader.get_bits(1) == 0  # full rank
    assert reader.get_bits(1) == 0  # not choice

    assert reader.get_bits(1) == 0  # not selected

    assert reader.get_bits(1) == 1  # selected
    assert reader.get_bits(1) == 1  # purchased
    assert reader.get_bits(1) == 1  # partial
    assert reader.get_bits(6) == 3  # rank
    assert reader.get_bits(1) == 1  # choice
    assert reader.get_bits(2) == 1  # choice_index

    print("  PASSED")


def _test_codec_roundtrip():
    """Test encode/decode round-trip with mock tree data."""
    print("Testing codec round-trip with mock data...")

    tree_nodes = OrderedDict()

    # Node 100: regular single-rank talent, purchased
    tree_nodes[100] = [(_MockTraitData(node_type=0, max_ranks=1, id_trait_node_entry=1001), 0)]
    # Node 200: not selected
    tree_nodes[200] = [(_MockTraitData(node_type=0, max_ranks=1, id_trait_node_entry=2001), 0)]
    # Node 300: 2-rank talent, full rank, purchased
    tree_nodes[300] = [(_MockTraitData(node_type=0, max_ranks=2, id_trait_node_entry=3001), 0)]
    # Node 400: 2-rank talent, partial rank (1 of 2)
    tree_nodes[400] = [(_MockTraitData(node_type=0, max_ranks=2, id_trait_node_entry=4001), 0)]
    # Node 500: choice node with 2 entries, choice_index=1
    tree_nodes[500] = [
        (_MockTraitData(node_type=NODE_CHOICE, max_ranks=1, id_trait_node_entry=5001), 0),
        (_MockTraitData(node_type=NODE_CHOICE, max_ranks=1, id_trait_node_entry=5002), 0),
    ]
    # Node 600: granted node (rank 1, not purchased)
    tree_nodes[600] = [(_MockTraitData(node_type=0, max_ranks=1, id_trait_node_entry=6001, is_granted_val=True), 0)]
    # Node 700: tiered node with 2 entries, both ranked
    tree_nodes[700] = [
        (_MockTraitData(node_type=NODE_TIERED, max_ranks=1, id_trait_node_entry=7001), 0),
        (_MockTraitData(node_type=NODE_TIERED, max_ranks=1, id_trait_node_entry=7002), 0),
    ]

    spec_id = 72  # Fury warrior

    selections = {
        100: (1, -1),    # full rank, not choice
        # 200: not selected
        300: (2, -1),    # full rank (2/2)
        400: (1, -1),    # partial rank (1/2)
        500: (1, 1),     # choice, index 1
        600: (1, -1),    # granted
        700: (2, -1),    # tiered, both ranks (2/2)
    }

    encoded = encode_talent_string(selections, tree_nodes, spec_id)
    print(f"  Encoded: {encoded}")

    dec_spec, dec_selections = decode_talent_string(encoded, tree_nodes)
    print(f"  Decoded spec_id: {dec_spec}")
    print(f"  Decoded selections: {dec_selections}")

    assert dec_spec == spec_id, f"spec_id mismatch: {dec_spec} != {spec_id}"
    assert dec_selections == selections, f"Selections mismatch:\n  {dec_selections}\n  {selections}"

    # Full round-trip
    reencoded = encode_talent_string(dec_selections, tree_nodes, dec_spec)
    assert reencoded == encoded, f"Re-encoded mismatch:\n  {encoded}\n  {reencoded}"

    print("  PASSED")


def _test_header_encoding():
    """Test that header bytes match expected pattern."""
    print("Testing header encoding...")

    # Version=2, spec_id=0, tree_hash=0, no nodes
    tree_nodes = OrderedDict()
    encoded = encode_talent_string({}, tree_nodes, 0)
    # 8 + 16 + 128 = 152 bits => ceil(152/6) = 26 chars
    assert len(encoded) == 26, f"Expected 26 chars, got {len(encoded)}"

    # First char should encode version=2 in LSB: bits 0-5 of value 2 = 000010 => index 2 => 'C'
    assert encoded[0] == 'C', f"Expected 'C', got '{encoded[0]}'"

    print(f"  Header-only string: {encoded}")
    print("  PASSED")


def _test_edge_cases():
    """Test edge cases."""
    print("Testing edge cases...")

    # Empty tree, non-zero spec
    tree_nodes = OrderedDict()
    encoded = encode_talent_string({}, tree_nodes, 577)  # Holy Paladin
    dec_spec, dec_sel = decode_talent_string(encoded, tree_nodes)
    assert dec_spec == 577
    assert dec_sel == {}
    print("  Empty tree: PASSED")

    # All nodes unselected
    tree_nodes = OrderedDict()
    for i in range(10):
        tree_nodes[i] = [(_MockTraitData(node_type=0, max_ranks=1, id_trait_node_entry=i*10), 0)]
    encoded = encode_talent_string({}, tree_nodes, 100)
    dec_spec, dec_sel = decode_talent_string(encoded, tree_nodes)
    assert dec_sel == {}
    print("  All unselected: PASSED")

    print("  PASSED")


if __name__ == "__main__":
    print("=" * 60)
    print("SimC Talent Codec Tests")
    print("=" * 60)

    _test_bitstream()
    _test_header_encoding()
    _test_codec_roundtrip()
    _test_edge_cases()

    print()
    print("All tests passed!")
