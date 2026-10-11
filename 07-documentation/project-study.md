# Earlier project study — reference notes

**Status: earlier workspace assessment, retained for context.** Its folder map, next steps and completion statements describe an earlier point in the project. Photo-based dimensions and material/joint interpretations are unverified estimates. Use the [current project overview](../README.md), [progress log](PROGRESS.md) and [modelling plan](../04-cad/modelling-plan.md) for current status.

## Project Identity

| Field | Detail |
| --- | --- |
| **Author** | Shashank Jangir (GitHub: shashankjangir) |
| **Supervisor** | Prof. Sagar Sarkar |
| **Origin** | MCP101 first-year group project (Groups 37 & 38, six members), October 2024 |
| **Current effort** | Solo rebuild with proper documentation, started 10 October 2026 |
| **Mechanism** | Three-wheel tri-star cluster (rotating triangular carrier with three wheels) |
| **Goal** | Carry payload up/down stairs with less manual pull force and better control than a regular trolley |

---

## Folder Map (18 files, 4 photos, 1 .docx report)

```
Root/
├── AGENTS.md                          ← working rules for AI assistants
├── README.md                          ← master overview and folder table
├── .gitignore                         ← OS temp files excluded
├── mcp 101 my work.docx              ← original MCP101 report (~2.9 MB, unchanged)
│
├── 01-problems/
│   ├── README.md                      ← problem statement, existing solutions, earlier lessons
│   ├── evidence_photo_wooden_ramp.jpg ← real photo: wheelbarrow on plank ramp over stairs
│   ├── garden_cart.jpg                ← illustration (stock)
│   ├── hand_truck.jpg                 ← illustration (stock)
│   └── manual_lifting.jpg            ← illustration (stock)
│
├── 02-how-the-idea-came/
│   └── README.md                      ← project origin, questions to answer, decision table (empty)
│
├── 03-research/
│   └── README.md                      ← research questions table, source notes (empty), existing-design comparison (empty)
│
├── 04-cad/
│   └── README.md                      ← parts/assembly plan, pre-fabrication checks, model details (blank fields)
│
├── 05-mechanical-work/
│   ├── README.md                      ← mechanism, torque, load distribution, structural checks, BOM, fabrication steps
│   └── design-requirements.md         ← operating conditions & performance goals (all "to be decided")
│
├── 06-testing/
│   ├── README.md                      ← 8-test sequence, pull-force comparison method, result tables (empty)
│   └── image.png                      ← stock photo: delivery person with hand truck and boxes
│
└── 07-documentation/
    ├── README.md                      ← report outline, evidence table, photo/file guidelines
    ├── PROGRESS.md                    ← two log entries (both 10 Oct 2026)
    ├── project-background.md          ← original project history and what to achieve now
    ├── initial-workspace-notes.md     ← archived setup notes (superseded)
    └── prototype-photos/
        ├── original-frame.jpeg        ← full frame with tri-wheel clusters on floor
        ├── wheel-clusters-on-stairs.jpeg   ← both clusters visible on green-marble stairs
        ├── cluster-at-step-edge.jpeg       ← close-up: carrier at step edge
        └── cluster-contact-position.jpeg   ← another carrier orientation on stairs
```

---

## What the Prototype Photos Reveal

### Original frame ([original-frame.jpeg](original-prototype/photos/original-frame.jpeg))
- Rectangular mild-steel frame, all-welded, moderate rust on surfaces
- Frame is tall (handle-height) with a lower horizontal rail connecting the two wheel clusters
- Two triangular carrier plates, one on each side, each mounting three black plastic/rubber wheels
- A single diagonal brace acts as the handle (two square-section bars)
- No load platform, no payload restraint, no load-bearing shelf visible
- Wheel clusters sit on the floor — not engaged with stairs in this shot

### On-stairs shots ([wheel-clusters-on-stairs.jpeg](original-prototype/photos/wheel-clusters-on-stairs.jpeg), [cluster-at-step-edge.jpeg](original-prototype/photos/cluster-at-step-edge.jpeg), [cluster-contact-position.jpeg](original-prototype/photos/cluster-contact-position.jpeg))
- Stairs are polished green marble with a light-coloured tread nosing
- Carrier plates are cut sheet metal (possibly mild steel), roughly triangular, with a central welded hub and three bolted wheel axles
- Burn marks / weld spatter visible at carrier centre — that's the shaft connection point
- Wheels appear to be ~100–125 mm diameter, hard plastic/rubber, spoked
- In the on-stairs photos, one wheel rests on the tread while the carrier positions the next wheel to reach the upper step
- The handle bars are bare square-section mild steel — no grip, no ergonomic shaping

---

## Current Project Status

### What exists (completed)
- ✅ Full 7-folder workspace structure
- ✅ Problem statement with five difficulty categories and four existing-solution comparisons
- ✅ Idea origin and questions to answer
- ✅ Research framework (questions table, existing-design table, source-notes table)
- ✅ CAD plan (parts list, pre-fabrication checklist, model-details template)
- ✅ Mechanical work structure (geometry, torque, load distribution, structural, BOM, fabrication)
- ✅ Design requirements template with 10 operating conditions and 7 performance goals
- ✅ Testing plan with 8-test sequence, pull-force comparison formula, and stopping conditions
- ✅ Documentation outline (10-point report structure, evidence table)
- ✅ Progress log with two entries
- ✅ Project background document
- ✅ Original MCP101 report preserved unchanged
- ✅ 4 prototype photographs extracted and captioned
- ✅ AGENTS.md with working rules

### What is empty / "to be decided"
- ❌ **Every numerical value** in [design-requirements.md](../05-mechanical-work/design-requirements.md) — payload, trolley mass, stair dimensions, budget, tools
- ❌ **Every table row** in research (existing designs, sources), CAD (design notes), mechanical work (torque, structural checks, BOM costs, fabrication log), and testing (results)
- ❌ **Decision table** in [02-how-the-idea-came](../02-how-the-idea-came/README.md) — no sketches, no dated decisions
- ❌ **No CAD files**, no drawings, no STEP exports
- ❌ **No calculations** — torque, pull force, CG, structural
- ❌ **No stair measurements**
- ❌ **No acceptance limits** set before testing
- ❌ **Original inspiration** story not yet written
- ❌ **Use case** not chosen (deliveries, household, construction?)
- ❌ **No external research sources** entered

---

## Key Information from the MCP101 Report (as summarised in the docs)

| Topic | What the report states | What it does NOT provide |
| --- | --- | --- |
| Build | Frame cutting and welding, mechanism assembly, spacing/handle adjustments | Material grades, member sizes, wheel diameters, bearing specs, weld details |
| Load | 30–50 kg testing range, platform designed for up to 50 kg | Individual load records, rated capacity, test procedure |
| Performance | "Smooth transitions," "reduced effort" | Force measurements, baseline comparison, stair dimensions |
| Issues | Slight tilting with heavier loads, traction on wet/slippery surfaces, material cost | Load at which tilting began, surface conditions, cost breakdown |
| Future ideas | Motor assist, folding, braking, improved traction, load restraints | None of these were built |
| CAD/Simulation | Stress and strain analysis mentioned | No CAD files, mesh details, loading conditions, or numerical results |

---

## Observations from the Photographs — Design Details

### Carrier plate geometry
- Equilateral triangle shape, three wheels at vertices
- Central hub is welded (not bolted) to the carrier plate
- Axles are bolted through the plate at each corner — visible nut-and-bolt fastening
- No bearings visible from the outside; unclear if the wheels spin on plain bushings or ball bearings

### Wheel specification
- Appear to be standard-catalogue caster wheels, ~100–125 mm OD
- Hard rubber or plastic tyre on a spoked plastic hub
- Ribbed tyre surface — may limit traction on smooth/wet marble
- No pneumatic wheels; rigid/semi-rigid

### Frame construction
- Square-section mild-steel tube, roughly 20–25 mm
- All-welded joints; no bolted connections on the frame itself
- Visible corrosion — no paint, no surface treatment
- Two long side rails + cross-members form a rigid rectangle
- Handle is two inclined bars welded to the top of the frame — no horizontal grip bar

### Stairs (test site)
- Green marble risers with light (cream/grey) stone treads
- Polished/smooth surface — relevant to traction concerns
- Nosing appears to be a slight bullnose radius, not sharp
- Outdoor stairs with plant pots — possibly a residential or campus building entrance

---

## Architecture of the Documentation

The project follows a clean **stage-gate** layout:

```mermaid
graph LR
    A["01 Problem"] --> B["02 Idea"]
    B --> C["03 Research"]
    C --> D["04 CAD"]
    D --> E["05 Mech Work"]
    E --> F["06 Testing"]
    F --> G["07 Documentation"]
```

Each folder has a self-contained README that:
1. States what the section covers
2. Provides structured tables for data entry
3. References the earlier prototype where relevant
4. Separates planned work from completed work
5. Cross-links to related folders

---

## Strengths of the Current Setup

1. **Honest about gaps** — every blank field says "to be decided" or "to be measured," never invented
2. **Earlier work preserved** — original report kept unchanged, photos extracted, context noted without treating old claims as validated
3. **Testing methodology is rigorous** — pull-force comparison formula defined, stopping conditions set, measurement uncertainty acknowledged
4. **Versioning rules are clear** — routine updates in place, new versions only for substantially different designs
5. **Good separation** — requirements in mechanical work (not problems), progress in documentation, design decisions tracked with date/reason

## Gaps and Risks

| Gap | Impact | Suggested next action |
| --- | --- | --- |
| No stair measurements | Cannot size wheels, carrier, or check clearances | Measure the test staircase (riser, tread, width, nosing, number of steps) |
| No payload target | Cannot start torque or structural calculations | Choose the intended use case and set a kg target |
| No acceptance limits | Testing results cannot be judged pass/fail | Set numerical limits before building |
| No external research | Mechanism sizing relies only on intuition | Find 2–3 tri-star geometry references or standards |
| No CAD software recorded | Can't plan the modelling workflow | Decide on SolidWorks, Fusion 360, FreeCAD, etc. |
| No budget set | Cannot make material or component trade-offs | Set a budget ceiling in INR |
| Carrier hub weld quality | Burn marks suggest possible incomplete fusion | Inspect or remake the hub connection |
| No tyre traction data | Marble stair traction is a known issue | Test grip or select rubber-compound wheels |
| Handle ergonomics | Bare steel bars, no grip, poor posture support | Design a horizontal grip with rubber sleeve |

---

## Immediate Next Steps (per the project's own progress log)

> "Next: choose the intended use and payload, measure the stairs, and develop the first mechanism sketch."

That translates to:

1. **Pick the use case** — who uses it, what they carry, where
2. **Measure the stairs** — fill in the operating conditions table in [design-requirements.md](../05-mechanical-work/design-requirements.md)
3. **Set the payload target** — kg, size, position
4. **Sketch the first tri-star geometry** — wheel radius vs. riser height, carrier radius, axle spacing
5. **Fill in 2–3 research sources** — academic papers or manufacturer data on tri-star mechanisms
