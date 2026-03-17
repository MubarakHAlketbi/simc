# Task Dossier: Windows Build vcpkg Manifest

**Purpose:** Resolve GitHub Actions Windows build failure caused by missing vcpkg manifest. The error "Could not locate a manifest (vcpkg.json) above the current working directory" indicates vcpkg is running in manifest mode but cannot find a manifest file.

---

## Task Metadata

- **Issue/Row Reference:** Windows build workflow error (no row in project_progress.md)
- **Task Type:** Build System / Infrastructure
- **Target File(s):** `vcpkg.json` (new file at repository root)
- **Status:** Research → Implementation → Testing → Complete
- **Wowhead Build Date:** N/A (not a game data change)

---

## Problem Analysis

The Windows build workflow (`.github/workflows/build.yml`) uses the Visual Studio vcpkg toolchain. The self-hosted runner or vcpkg version appears to enforce manifest mode, requiring a `vcpkg.json` in the repository root or a parent directory. The current repository has no `vcpkg.json`, causing the build to fail.

### Required Dependencies

Based on the existing workflow:
- `curl` (needed for both CLI and GUI builds; networking library)
- `qtbase` (Qt6 base libraries for GUI)
- `qtwebengine` (Qt6 WebEngine for GUI)

Triplet: `x64-windows`

---

## Implementation Plan

1. Create `vcpkg.json` at repository root with the dependencies (curl, qtbase, qtwebengine) **and include `"builtin-baseline": "master"`** to satisfy vcpkg's reproducibility requirement.
2. **Update `.github/workflows/build.yml`** to use manifest mode:
   - Change `vcpkg install curl:x64-windows` to `vcpkg install --triplet x64-windows`
   - Change multiple `vcpkg install ...` lines to a single `vcpkg install --triplet x64-windows`
   - Keep `vcpkg integrate install` as is.
3. Commit both changes with a clear message.

---

## Verification

- **Local check:** Ensure `vcpkg.json` is valid JSON and at repository root.
- **CI:** Push the change and monitor Windows build jobs for success.
- **Expected:** The vcpkg steps (both manual install and CMake configure) should no longer error about missing manifest.

---

## Post-Implementation

**Commit Message:** [Midnight] Add builtin-baseline to vcpkg manifest  
**Files Modified:** `vcpkg.json` (updated), `.github/workflows/build.yml` (updated in previous commit), `task_dossiers/windows_build_vcpkg_manifest_2026-03-17.md` (updated)  
**project_progress.md Rows Updated:** None (build infrastructure)  
**Date Completed:** 2026-03-17

---
