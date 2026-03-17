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

1. Create `vcpkg.json` at repository root with the following content:
```json
{
  "$schema": "https://raw.githubusercontent.com/microsoft/vcpkg/master/docs/config/vcpkg.schema.json",
  "name": "simulationcraft",
  "version": "0.0.1",
  "dependencies": [
    "curl",
    "qtbase",
    "qtwebengine"
  ]
}
```

2. No changes to `build.yml` are strictly required; the manifest will satisfy vcpkg's lookup. The existing manual `vcpkg install` steps will still work (they will install the packages as requested, and the manifest provides a fallback).

3. Commit the new file with a clear message: "[Midnight] Add vcpkg manifest for Windows builds"

---

## Verification

- **Local check:** Ensure `vcpkg.json` is valid JSON and at repository root.
- **CI:** Push the change and monitor Windows build jobs for success.
- **Expected:** The vcpkg steps (both manual install and CMake configure) should no longer error about missing manifest.

---

## Post-Implementation

**Commit Message:** [Midnight] Add vcpkg manifest for Windows builds  
**Files Modified:** `vcpkg.json` (new)  
**project_progress.md Rows Updated:** None (build infrastructure)  
**Date Completed:** 2026-03-17

---
