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

The Windows build workflow (`.github/workflows/build.yml`) uses vcpkg to install dependencies. However, vcpkg's manifest mode requires a `builtin-baseline`, and the vcpkg version on the self-hosted runner enforces this. Trying to satisfy this requirement leads to complexity.

**Simpler solution:** Use the Qt installation already present on the Windows machine. SimulationCraft on Windows uses WinINet (built-in) for networking, so **no external dependencies are needed at all** for the CLI build. The GUI build only needs Qt, which is installed.

---

## Implementation Plan

1. Remove all vcpkg-related steps from both Windows jobs (CLI and GUI) in `.github/workflows/build.yml`:
   - Delete the "Install dependencies via vcpkg" steps.
   - Remove `-DCMAKE_TOOLCHAIN_FILE=.../vcpkg.cmake` and `-DVCPKG_TARGET_TRIPLET=x64-windows` from CMake configure commands.
2. Keep the rest of the workflow as-is.
3. Ensure the self-hosted runner has Qt installed and in PATH (per `how_to_build.md`).
4. Commit and push changes.

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
