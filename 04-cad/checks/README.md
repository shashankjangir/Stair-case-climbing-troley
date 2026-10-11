# Geometry check records

- `geometry-checks.json` records the initial generated layout. It is not a fresh simulation or a mass/strength result.
- `saved-model-checks.json` records checks performed after reopening the current `.blend`. Its UTC timestamp and SHA-256 identify the file checked. A later edit changes that hash and requires checking again.

The check script does not save or overwrite the Blender model. It temporarily rotates cluster controls in memory to check parenting, restores them, and writes this report. It checks component counts and nominal dimensions; it does not establish stair clearance, load capacity, stability or fabrication readiness.

Run Blender in background mode with `--python 04-cad/scripts/check_blender.py` from the repository root. To rebuild instead, use `build_blender.py`, which replaces the generated model; preserve manual edits before deliberately rebuilding.
