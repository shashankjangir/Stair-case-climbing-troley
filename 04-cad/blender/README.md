# Blender trolley assembly

**10 October 2026 — first geometry model of the current design.**

Open [stair-trolley.blend](stair-trolley.blend) in Blender. The [assembly preview](../previews/assembly-preview.png) shows the upright, unloaded trolley on a flat floor. This is the start of modelling, not a fabrication-ready design.

## What is included

- Tubular frame, three cross-members, handle and toe platform with three supporting rails.
- One shared main axle, preliminary split-clamp and bracket envelopes.
- Two tri-star clusters, four carrier plates, six wheel envelopes and six wheel axles.
- Two flanges per central hub, bearing seats, four 6205 bearing envelopes and inner-race spacers.
- Separate, initially hidden collections for the reference payload and the twelve-riser nominal staircase.
- Named objects, steel/rubber appearances, a camera and lighting for the preview.

The staircase rises towards negative X. The trolley is on the lower level, clear of the first step; it is not posed as if a stair-climbing simulation has passed.

## Working with the file

The Outliner groups the frame, each cluster, payload, stairs and presentation objects into separate collections. The payload and stair collections start hidden; enable their viewport/render visibility to inspect them. Hide `06 Presentation` to work without the studio floor, camera and lights.

Rotate a `Cluster … - rotate Y independently` empty around Y to turn that carrier and its wheels. Rotate a `Wheel pivot … - rotate Y` empty to spin an individual wheel. These are editing controls, not automatic ground contact or mechanical constraints; rotating a cluster in place can move a wheel through the floor.

Geometry is stored in metres and displayed in millimetres. The axle centre remains the origin. The starting wheel phase places one wheel above the axle and two below, giving a 195 mm nominal axle height above the floor. Toe rails extend to z = −187 mm, so the flat-floor clearance is **8 mm**.

Core mechanism dimensions are in [params.py](../scripts/params.py). The generator also contains explicit initial layout and hardware-envelope dimensions; it is not yet a completely parameter-driven CAD system. Edit the relevant source values together and rerun [build_blender.py](../scripts/build_blender.py) to regenerate. The embedded parameter text is a source snapshot; changing it or a custom property inside Blender does not automatically rebuild objects. Manual mesh edits can be made directly, but regeneration replaces them—save an edited working file elsewhere before choosing to rebuild it.

## Checks and limits

[saved-model-checks.json](../checks/saved-model-checks.json) records checks run after reopening the saved file: component counts, main dimensions, carrier orientation, nominal floor clearance and cluster parenting. [geometry-checks.json](../checks/geometry-checks.json) records the initial layout.

The following remain unfinished:

- Exact carrier root fillets and outline refinement; the current curved-arm contour is preliminary.
- Mitred frame joints, welds, tube caps, detailed bracket attachment, clamp bolts, fastener threads and positive axle retention.
- Supplier-confirmed wheel geometry/mass, bearing fits, seals and tolerances.
- Payload restraints and their mounting details; the hidden payload is only a size reference with a nominal mass property.
- Complete mass/CG calculation, interference/contact study, all stair variants, load analysis and descent control.

The saved objects are meshes. No native SolidWorks parts, STEP solids, load rating, stress result or validated stair-climbing animation is claimed. Refer to the [corrected modelling plan](../modelling-plan.md) for the remaining work.
