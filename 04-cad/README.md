# CAD

## Blender work started — 10 October 2026

The [first Blender assembly](blender/stair-trolley.blend) and [rendered preview](previews/assembly-preview.png) are now available. Read the [Blender notes](blender/README.md) for controls, checks and unfinished details. The [modelling plan](modelling-plan.md) now describes the active Blender workflow while retaining SolidWorks references for later use.

The model contains the frame, axle, both clusters, wheels, hub/bearing envelopes, toe and handle, plus hidden payload and stair references. It is a geometry prototype; motion, mass/CG and structural validation are still pending. Corrected nominal toe ground clearance is 8 mm after including the deck thickness.

## Starting design selected — 10 October 2026

Use sections 6–8 of the [research and CAD design basis](../03-research/trolley-research-and-cad-design-basis.md) for the selected materials, dimensions, coordinate system and checks. The starting assembly uses 200 mm wheels on 190 mm carriers, paired 6 mm steel plates, a 25 mm fixed axle and a 560 mm wheel-centre track. The initial Blender geometry is linked above.

Begin with the selected parameterised assembly and five stair cases. Resolve interference, load paths, CG and purchased-part fits before releasing fabrication drawings. The nominal 175 × 275 mm stair is a chosen modelling case, not a measured Indian average.

The CAD model will bring the tri-star mechanism and chassis together before fabrication. It should show how the trolley fits the intended stairs, how the parts move, and where the load is supported.

## Parts and assemblies to model

| Item | What to include |
| --- | --- |
| Chassis | Frame members, cross-members, mounting points, and joining details. |
| Load platform and restraints | Support surface, stops, and attachment points that keep the payload in place. |
| Tri-star carriers | Three-wheel layout, hub geometry, wheel axle positions, and clearances. |
| Wheels, axles, and bearings | Actual selected dimensions, fits, spacers, and retention details. |
| Handle | Grip position, height, angle, and connection to the frame. |
| Complete assembly | Both sides of the mechanism, all supports, and representative payloads. |
| Stair model | Measured riser, tread, width, and edge geometry for the intended test stairs. |

## Checks before fabrication

- Move the mechanism through a full wheel-cluster cycle and consecutive steps.
- Check wheel, carrier, frame, and stair clearances throughout the motion.
- Look at entry onto the first step and exit onto the upper landing.
- Assign appropriate materials and payload masses before reviewing mass properties.
- Record the combined centre of gravity for the trolley and each planned payload position.
- Relate the centre-of-gravity position to the changing support contacts and the operator's applied force.
- Confirm there is space for bearings, fasteners, tools, and assembly.
- Use the same dimensions in the CAD and mechanical calculations.

A motion model will help identify problems, but smooth motion in CAD alone will not establish prototype performance.

## Model details

- Software and release: SolidWorks (user's installed version)
- Units: mm–g–s (MMGS); record mass in kg and force in N separately.
- Main assembly: `stair-trolley-assembly.sldasm`
- Selected materials: IS 4923 YSt 240 (frame tubes), IS 2062 E250 (carrier plates, gussets, deck), C45 (main axle, wheel axles), solid rubber (wheel treads)
- Payload represented: 50 kg compact block, secured with two straps; test at 0, 10, 25, 40 and 50 kg
- Stair measurements used: Cases A–E from the research document; nominal Case B = 175 × 275 mm, 12 risers
- Related calculation files: [Research and CAD design basis §6–8](../03-research/trolley-research-and-cad-design-basis.md)

## Files to keep

Save editable parts and assemblies with their dependencies, STEP exports for sharing, and dimensioned manufacturing drawings. Drawings should identify materials, important fits, tolerances, and joining details.

Use descriptive names such as `chassis`, `tri-star-carrier`, and `main-assembly`. Update the current design as it develops. Preserve a separate complete design if the project later moves to a substantially different concept.

## Design notes

| Date | Part or assembly | Update | Reason or supporting calculation |
| --- | --- | --- | --- |
| | | | |

## Reference from the original prototype

The original report describes modelling the frame and tri-wheel assembly, along with simulation-based stress and strain analysis. It does not contain editable CAD, dimensioned drawings, mesh details, loading conditions, or numerical simulation results.

Use the [prototype photographs](../07-documentation/README.md#original-prototype-photographs) to understand the earlier layout: a rectangular frame, wheel clusters on both sides, triangular carrier plates, and three wheels per cluster. Recover or measure the actual dimensions before rebuilding the geometry; do not estimate manufacturing dimensions from the photographs alone.

The earlier modelling and analysis are recorded as part of the project history. The CAD and analysis files for the current work still need to be created or recovered.
