#!/usr/bin/env python3
"""Talent Optimizer — thin wrapper around talent_local_search.

This is the entry point for talent optimization. It delegates to
talent_local_search.optimize_spec() which implements the
seed + neighborhood hill-climb algorithm.

Usage:
    python3 scripts/talent_optimizer.py warrior_fury
    python3 scripts/talent_optimizer.py warrior_fury --fight-style Patchwerk
    python3 scripts/talent_optimizer.py --all
"""

# This module exists for backward compatibility and as a convenience
# entry point. The actual implementation is in talent_local_search.py.

from scripts.talent_local_search import main

if __name__ == "__main__":
    main()
