# Stair-climbing trolley: research and CAD design basis

**Research date: 10 October 2026. Status: selected concept and preliminary engineering calculations; CAD and physical validation are next.**

## 1. What we are going to design

The selected starting design is a **manually pulled trolley with two independently rotating tri-star clusters**, six rubber wheels, paired steel carrier plates, and a welded square-tube steel frame. The payload target is **50 kg**. This is a design target, not a tested capacity.

The main dimensions for the next CAD session are a **190 mm carrier radius, 200 mm wheel diameter, 560 mm wheel-centre track, 35 × 35 × 2 mm main-frame tube, 30 × 30 × 2 mm toe-support tube, 6 mm carrier plates and a 25 mm main axle**. The detailed parameter table below defines the assembly. These values are our engineering selections; they are not measurements of the old trolley.

This document reviews ten separate published trolley projects, including manual, powered tri-star and tracked designs. Their accessible full papers were read, including the calculation sections and relevant equation figures. This is a review of those ten publications, not a claim to have found every trolley ever built or every publication by their authors. Most are prototype papers with limited test records, so their load claims are treated cautiously.

The original MCP101 report and prototype photographs remain the record of the earlier build. Estimates in `project_study.md`, such as wheel size judged from a photograph, are not dimensional inputs for this design.

## 2. Ten published designs reviewed

Links lead to the original papers or an author-uploaded full text. Page numbers below refer to printed journal pages unless stated otherwise. All sources were accessed on the research date.

| ID | Publication | Mechanism and useful evidence | What it contributes |
| --- | --- | --- | --- |
| P01 | Senthil Kumar G et al., **Design and Fabrication of Stair Climbing Trolley**, IRJET 5(3), 2018, pp. 685–687. [Full paper](https://www.irjet.net/archives/V5/i3/IRJET-V5I3154.pdf) | Manual tri-star; fabrication description; bending calculation. | Simple construction, but its shaft sizing is unsuitable to copy directly. |
| P02 | More Pawan Ashok et al., **Design and Manufacturing of Stair Climbing Trolley**, IRJET 6(2), 2019, pp. 2646–2648. [Full paper](https://www.irjet.net/archives/V6/i2/IRJET-V6I2508.pdf) | Manual curved carriers and a movable/folding loading base. A 100 kg objective is discussed without a reproducible load-test record. | Carrier clearance and storage features; no worked structural calculation. |
| P03 | Eeshan Nandkumar Chaudhari et al., **Application of E-Bike Chain-Drive Transmission in Stair Climbing Trolley**, IRJET 7(7), 2020, pp. 2610–2619. [Full paper](https://www.irjet.net/archives/V7/i7/IRJET-V7I7463.pdf) | Motorised tri-star, paired plates, chain transmission; reports 40 kg on stairs and 100 kg on flat ground. | Most extensive calculation set, but motor and chain calculations contain major inconsistencies. |
| P04 | Rakesh Nath, **Design and Parametric Evaluation of a Staircase Climbing Forklift**, IRJET 7(7), 2020, pp. 2832–2839. [Full paper](https://www.irjet.net/archives/V7/i7/IRJET-V7I7499.pdf) | A fabricated forklift/trolley hybrid with tri-star stair mechanism and motorised lifting. | Contact-force equations and a different load-handling arrangement. |
| P05 | Omkar Chodankar et al., **Design of Stair Climbing Trolley**, IJSRD 7(2), 2019, pp. 907–909. [Full paper](https://www.ijsrd.com/articles/IJSRDV7I20755.pdf) | Manual tri-star; shaft and wheel sizing; fabricated assembly shown. | Useful worked geometry, with typographical and terminology errors. |
| P06 | Suraj Nayak and Saurya Pratap Singh, **Design and Fabrication of Stair Climber Trolley**, IJAEM 3(8), 2021, pp. 165–173. [Full paper](https://ijaem.net/issue_dcp/Design%20and%20Fabrication%20of%20Stair%20Climber%20Trolley.pdf) | Manual trolley with paired stainless carrier plates and rubber wheels. | Includes trolley self-weight, although its reaction calculation does not balance. |
| P07 | Snehita Kilari et al., **Design & Fabrication of Tri-Wheel Stair Case Climbing Hand Trolley**, IJETT 67(7), 2019, pp. 54–57. [Full paper](https://ijettjournal.org/assets/Volume-67/Issue-7/IJETT-V67I7P211.pdf) | Manual curved carriers, CATIA design and fabrication; reports 120–150 kg capability without detailed logs. | Shows why radius, diameter and centre spacing must be distinguished. |
| P08 | Adhyanth G Ajay et al., **Design and Development of Light Weight Mechanical Staircase Climbing Trolley with Better Stress Distribution**, JCHPS, Special Issue 7, May 2017, pp. 192–194. [Full paper](https://www.jchps.com/specialissues/Special%20issue%207/MERS-42.pdf) | Acrylic carriers, nylon wheels, aluminium handles and wood platform; reports a 10 kg trial on 150 × 250 mm stairs. | A useful lightweight comparison, not evidence for a 50 kg acrylic carrier. |
| P09 | P. V. Sanjeeva Kumar, A. Hemanth Kumar and P. Varaprasad, **Design and Fabrication of Motorised Stair Case Climbing Trolley**, IJAER 13(17), 2018, pp. 13380–13385. [Author-uploaded full text](https://www.researchgate.net/publication/334963679_Design_and_Fabrication_of_Motorised_Stair_Case_Climbing_Trolley) | Stepper-motor tri-star, Arduino/TB6600 control and chain drive; describes descent vibration. | Motor sizing and geometry need correction; descent control deserves explicit attention. |
| P10 | Nitin Goyal et al., **Automatic Stair Climbing Trolley**, IJRASET, 2023, DOI 10.22214/ijraset.2023.49612. [Full article](https://www.ijraset.com/research-paper/automatic-stair-climbing-trolley) | Motor-driven belt/crawler arrangement and adjustable frame; fabrication described. | A genuine alternative mechanism, but no worked traction or payload calculation. |

These are ten published project descriptions, not ten independently certified products. P09's publisher PDF was inaccessible; its author-uploaded full text was used. An ordinary luggage-cart paper encountered during searching was excluded because it did not describe stair climbing.

## 3. Calculation ledger from the papers

This ledger records the engineering equations and worked numerical calculations found in the selected papers, including results we should **not** reuse. Algebra is restated in consistent notation where possible. General background prose, duplicated equations and unrelated application claims are omitted.

### Shared geometry notation

- `h` = riser height; `b` = horizontal tread going; `R` = distance from carrier centre to a wheel centre.
- `r` = individual wheel radius; `s` = distance between adjacent wheel centres.
- `t` in the published clearance equations is an **in-plane arm half-width/holder dimension**. It is not the through-thickness of the steel plate.
- `g = 9.81 m/s²`; `1 N/mm² = 1 MPa`; `1 kgf·cm = 0.0980665 N·m`.

The repeated first-pass geometry is:

```text
s = √3 R
R = √[(h² + b²)/3]                  (matching an adjacent-step diagonal)
r_max = √(h² + b²)/2               (non-overlap limit under that matching assumption)
r_min = [6Rt + h(3b − √3h)] / [(3 − √3)h + (3 + √3)b]
```

The last expression belongs to a particular illustrated arm/contact geometry. It is not proof that any curved arm will clear a staircase. When `R` is fixed independently of the stair diagonal, wheel-to-wheel non-overlap must instead use `r < √3 R / 2`. Actual step contact and interference need a motion study.

### P01 — shaft bending, p. 686

```text
Span = 600 mm; loads at 40 and 560 mm
Two loads = 100 × 9.81 = 981 N each; total = 1962 N
RA = RB = 981 N
M_max = 981 × 40 = 39,240 N·mm
σ_allow = σ_y / FS = 1300 / 3 = 433.3 MPa
M = (π/32)d³σ_allow
d = 9.749 mm → selected 10 mm
```

**Audit:** the assumed 1300 MPa yield strength has no adequate material specification. The equation is for a solid circular section even though the text calls the member a pipe. The result omits impact and fatigue. One equilibrium expression also mislabels a load term. The symmetric reaction result itself is consistent with the stated loads.

### P02 — no worked numerical analysis

The paper describes three wheels at 120° and a 100 kg design objective, but provides no worked torque, shaft, bearing, CG or force calculation. Its curved-arm and folding-base ideas are qualitative design references.

### P03 — geometry, shaft, bearings, transmission and FEA, pp. 2613–2618

```text
Stair: h = 150 mm, b = 280 mm
R = √[(150² + 280²)/3] ≈ 184 mm
Published r_min = 64.7 mm, rounded to about 70 mm
Published r_max = √[(h² + b²)/2] = 224.6 mm
Published t_max = [hr(3−√3) + br(3+√3) + h(√3h−√3b)]/(6R)
Published t_max result = 69.4 mm
Actual selected wheel radius = 101.6 mm

Shaft: D = 25 mm
M = 245.25 × 0.381 = 93.44 N·m; T = 180.31 N·m
Te = √[(Kb M)² + (Kt T)²], Kb = 1.5, Kt = 1.25
Te = 265.42 N·m
τ = 16Te/(πD³) = 86.51 MPa
τ_allow = 0.5 × 360 / 1.5 = 120 MPa

Bearing: 6005-2Z; 25 × 47 × 12 mm
P = XVFr + YFa; Fa = 0, V = 1 → P = 490.5 N
L10 = 60nLh/10⁶ = 144 million revolutions for n = 300 rpm, Lh = 8000 h
L10 = (C/P)³ → C_required = 2570.94 N
Paper's catalogue C = 11.9 kN

Motor/transmission: 24 V, 350 W, 300 rpm motor output; 9:45 sprockets
n_output = 300 × 9/45 = 60 rpm
Pitch p = 12.7 mm; initial centre distance a = 40p = 508 mm
Chain speed v = z₂ p n₂ / 60 = 0.5715 m/s
ω = 2πn/60 = 31.42 rad/s at 300 rpm
Paper uses T = 175 N·m: power N = Tω = 5497 W
Published chain pull Pt = 1020N/v → 1981.46 N (units/substitution inconsistent)
Pc = wv²/g = 0.22 N, using chain weight w = 6.86 N/m
Ps = kwa = 3.50 N
PT = Pt + Pc + Ps = 1985.18 N
Design pull = Ks PT = 1.9 × 1985.18 = 3771.84 N
Breaking load = 17,854.2 N → reported FS = 4.73

ap = a/p = 40
Lp = 2ap + (z₁+z₂)/2 + [(z₂−z₁)/(2π)]²/ap = 107.82 pitches
Selected Lp = 110; chain length = 110 × 12.7 = 1397 mm
q = [(z₂−z₁)/(2π)]² = 32.83
e = Lp − (z₁+z₂)/2
a = (p/4)[e + √(e²−8q)]
Sprocket pitch diameters: p/sin(180°/z) ≈ 37.1 and 182.1 mm

FEA reported: carrier maximum displacement 0.01987 mm; stress 10.985 MPa
Shaft maximum displacement 0.88174 mm; reported maximum stress 61.828 MPa
```

**Audit:** correct geometric `r_max` is 158.8 mm. The printed `t_max` is not the algebraic inverse of the stated `r_min`. A 350 W shaft at 300 rpm can provide only 11.14 N·m ideally, not 35 N·m. Input/output torque and speed are mixed; chain load and FS are consequently unreliable. Selecting 110 links changes the calculated centre distance to approximately **522.0 mm**, not 508 mm. `2Z` is shielded, not open. Shaft stress is inconsistently named; the FEA lacks sufficient verification for transfer to our trolley.

### P04 — contact forces, bearing and axle, pp. 2834–2838

Geometry uses the shared `R`, `r_min`, `r_max` equations and the same questionable `t_max` expression as P03.

```text
h = 150 mm, b = 350 mm → R = 219.85 ≈ 220 mm
r_max = √(150² + 350²)/2 = 190.39 mm
r_min printed as “820 mm = 8.2 cm”
With t = 25 mm, shared r_min gives 82.05 mm

Holding moment: Fx = Wy → F = Wy/x
Contact equilibrium:
[(W₁+W₂)/2 − F sinθ] k = F cosθ √(R²−k²)
Re cosφ = F cosθ
Published vertical equation: Re sinφ + F cosθ = (W₁+W₂)/2
Re = √[(F cosθ)² + ((W₁+W₂)/2 − F sinθ)²]
tanφ = (W₁+W₂ − 2F sinθ)/(2F cosθ)

Bearing example: Fr = 40 × 9.81 = 392.4 N; speed 10 rpm
L10 = 500 million revolutions
C = P L10^(1/3) = 3114.5 N
Selected 6002, 15 mm bore; paper quotes C = 5590 N

Axle relations: M/I = σ/y = E/ρ; I = πd⁴/64
Published I = 3.21 × 10⁻⁹ m⁴; y = 0.008 m
Published M = wl²/8 = 245.25 × 0.65²/8 = 12.95 N·m
Paper divides this by 1.5 → 8.63 N·m → σ ≈ 21.5 MPa
```

**Audit:** the clearance substitution/units conflict. The vertical equilibrium equation needs `F sinθ` to match the following equations. `I` corresponds to a **16 mm diameter**, despite a radius label. Dividing the applied moment by a safety factor reduces demand incorrectly; using its original moment gives about 32.3 MPa. The meaning of `w` is unresolved: `wl²/8` requires force per length. Motor torque specifications also conflict. Holding force is not a complete climbing-force prediction.

### P05 — shaft and wheel sizing, pp. 908–909

```text
Payload = 100 kg → W = 981 N
Span = 650 mm; two 490.5 N loads at 100 and 550 mm
RA = RB = 490.5 N
M_max = 490.5 × 100 = 49,050 N·mm
σ_allow = 350/2 = 175 MPa
d = [32M/(πσ_allow)]^(1/3) = 14.18 mm → 15 mm

h = 160 mm, b = 310 mm, t = 20 mm
R = √[(h²+b²)/3] = 201.41 mm
r_min = 77.03 mm
r_max = √(h²+b²)/2 = 174.43 mm
Paper's average radius = 125.28 mm → selected 125 mm; wheel diameter 250 mm
```

**Audit:** the printed shear values ±1962 N conflict with the loads; they should be ±490.5 N in the outer loaded segments. A solid-shaft equation is used despite “hollow” terminology. The printed `R` expression conflicts with its numerical result. Averaging the printed radius limits gives approximately **125.73 mm**, not 125.28 mm. Taking that average is a design choice, not an optimisation proof.

### P06 — self-weight and axle, pp. 171–172

```text
Axle length = 0.44 m; connection spacing = 0.40 m
Payload = 30 kg → 294.3 N → two loads of 147.15 N
Trolley self-weight = 20 kg → 196.2 N, treated as distributed
Published R₁ = R₂ = 190.314 N
Published maximum bending moment = 6.7155 N·m
Factored moment = 1.5 × 6.7155 = 10.07 N·m
Allowable bending stress = 0.66 × yield = 165 MPa
Holding balance: Fx = Wy → F = Wy/x
Bearing specification: 6006, 30 × 55 × 13 mm
```

**Audit:** total applied load is 490.5 N, but the reactions sum to 380.628 N. A symmetric arrangement would require 245.25 N at each support. Thus the reported bending result cannot be adopted. No completed diameter/stress check establishes safety. The bearing sealing description is inconsistent.

### P07 — geometric calculation, p. 55

```text
h = 140 mm, b = 300 mm, t = 25 mm
R = √[(h²+b²)/3] = 191.14 mm
r_min ≈ 75.59 mm (paper rounds to 75.5)
Paper gives r_max ≈ 165 mm, beside an inconsistent /√3 expression
Correct non-overlap value under matching assumption = √(h²+b²)/2 = 165.53 mm
Paper's mean radius = (75.5 + 165)/2 = 120.25 mm
Published maximum height relation h_max = √(3R² − r²) ≈ 308 mm
```

**Audit:** the text also gives 120 mm wheel diameter, then 60 mm outside/40 mm inside diameter elsewhere. These cannot all describe the calculated wheel. A 191 mm carrier radius implies about 331 mm adjacent wheel-centre spacing, not 190 mm. The maximum-height relation alone does not establish climbability or clearance. Its steel density unit is also wrong. Do not adopt the reported capacity as verified.

### P08 — material and simulation results, pp. 192–194

No worked shaft, torque or CG equations are provided. Numerical analysis/evidence consists of:

- PMMA compressive yield quoted as 18,000 psi, approximately 120 MPa; unit conversion gives 124.1 MPa.
- Carrier leg length 200 mm and width 50 mm; another 370 mm overall dimension is not a sufficiently clear definition of `R`.
- Figure-read simulation maxima are approximately 0.565 MPa stress and 0.00119 mm displacement; loads/restraints are insufficiently specified for independent verification.
- A reported physical 10 kg trial on 150 mm risers and 250 mm treads.

Compression strength alone does not qualify an acrylic carrier for bending, bolt-hole stress or stair impacts.

### P09 — stepper motion, geometry and power, pp. 13381–13384

```text
Stepper angle relations:
θ = 90°/Nr
θ = 360°/(m Nr), or θ = 360°(Ns−Nr)/(Ns Nr), for the described motor arrangements
1.8° full step / 10 microsteps = 0.18° per microstep

h = 15 cm, b = 29 cm → R = √[(h²+b²)/3] = 18.85 cm
Published r_min uses a +√3h term instead of the usual −√3h; result 8.43 cm
Published r_max = √[(h²+b²)/2] = 23.08 cm
Selected wheel radius appears as both 3.5 and 4 cm
Published t₁,max = [hr(3−√3)+br(3+√3)+h(√3h−√3b)]/(6R) = 5.17 cm
h_max = √(h²+b²−r²) = 32.4037 cm for r = 4 cm
t₂,max = r[r+√(3(h²+b²−r²))]/[2√(h²+b²)] = 3.68 cm

Motor power: P = mgv; m = 30 kg; v = 5 cm/s
Paper reports 147 W and refers to a “150 W battery”
```

**Audit:** correct `r_max` is 16.325 cm. The selected wheel is below even the paper's own minimum. At a **vertical** speed of 0.05 m/s, `mgv = 14.715 W`, before losses; a speed along the staircase needs a slope factor. Battery energy needs Wh/Ah and voltage. Reported speeds and stair-load claims lack a consistent test record. Microstepping resolution does not establish available loaded torque.

### P10 — specifications, no worked load analysis

The full article specifies an approximately 12 kg assembly, 30 rpm geared motor, 19 kgf·cm torque, 12 V battery, 48 mm pulleys, 22 mm shaft, and a 520 × 10 mm timing belt. It gives no worked force, power, shaft, bearing-life or CG calculations.

Our unit check gives `19 kgf·cm = 1.863 N·m`; at 30 rpm that is approximately **5.85 W mechanical output**, if torque and speed apply simultaneously. This is our calculation, not a reported output test. The “rack and pinion” description conflicts with its belt/pulley fabrication account, and its bearing dimensions do not match the shaft clearly. Its general statement about 1000 kg tracked machines is not a rating for its prototype.

## 4. What the comparison tells us

| Option | Benefit for this project | Cost or limitation | Decision |
| --- | --- | --- | --- |
| Manual tri-star, paired steel plates | Straightforward fabrication; replaceable wheels; no motor or battery integration | Pull-force peaks and step impacts remain; operator must control tilt | **Selected for CAD** |
| Powered tri-star | Can supply climbing work through a drive | Requires valid torque/speed sizing, transmission, braking and controls | Keep as a future major alternative if manual effort fails the target |
| Tracked trolley | Longer contact region and potential powered control | Belt tensioning, traction, turning and landing transitions add complexity | Not selected for this build |
| Acrylic/lightweight carrier | Can reduce mass in a small demonstrator | Brittle/notch-sensitive behaviour; reviewed evidence only demonstrates a small load | Not selected for the 50 kg target |
| Forklift hybrid | Adds lifting as well as stair transport | Larger mechanism and additional load cases | Outside this project's immediate purpose |

The recurring useful features are rubber wheels, replaceable bearings, two plates supporting each wheel axle, a low secured load, and clearance between the carrier and the step. Curved arms are worth modelling, but no paper establishes one universally suitable profile. We should not copy a published “safe” shaft diameter, motor power or maximum stair height without its actual load path.

## 5. Stair dimensions in India

### What the official reference establishes

The [TCPO Model Building Bye-Laws 2016](https://tcpo.gov.in/sites/default/files/MODEL-BUILDING-BYE-LAWS-2016.pdf), clause **4.17**, printed p. 57 / PDF p. 75, specifies:

| Building category | Minimum tread excluding nosing | Maximum riser | Minimum clear staircase width |
| --- | --- | --- | --- |
| Residential dwellings | 250 mm | 190 mm | 1000 mm; a 750 mm exception is stated for two-storey row housing |
| Other buildings | 300 mm | 150 mm | Varies: hotels/educational/other buildings 1500 mm; assembly/institutional 2000 mm |

It also states a limit of 12 risers per flight and 2.2 m clear headroom. These are **model regulatory dimensions, not a measured national average**, and local adopted rules and existing staircases may differ.

I did not find a representative national measurement dataset that justifies calling one riser/tread pair the “average Indian staircase.” Therefore **175 mm riser × 275 mm tread is our chosen nominal CAD case**, not an asserted Indian average.

### Stair models for CAD

| Case | Riser × tread, mm | Slope `atan(h/b)` | Matching `R = √((h²+b²)/3)` | Purpose |
| --- | --- | --- | --- | --- |
| A | 150 × 300 | 26.57° | 193.65 mm | Model-bye-law non-residential limiting pair |
| B | 175 × 275 | 32.47° | 188.19 mm | Chosen nominal design case |
| C | 190 × 250 | 37.23° | 181.29 mm | Model-bye-law residential limiting pair |
| D | 150 × 350 | 23.20° | 219.85 mm | Deep-tread sensitivity check |
| E | 190 × 300 | 32.35° | 205.02 mm | Mixed-dimension sensitivity check |

Model 12 consecutive risers, plus lower and upper landings. Use 0 and 25 mm nosing projections, and 0 and 10 mm nose radii as **chosen test cases**, not Indian-standard values. Begin with 1000 mm clear width and a 1200 × 1200 mm landing; check actual site dimensions before claiming access. A nominal 660 mm trolley leaves 170 mm per side in a 1000 mm passage, but only 45 mm per side in a 750 mm passage. Landing turning space also depends on trolley tilt and the operator.

Record every step's rise/going, nosing, surface, slope across the stair, handrail restrictions and landing turns at the intended site. The selected carrier is a compromise; cases D/E must be checked, not assumed compatible simply because their slope is lower.

## 6. Preliminary calculations for our selected design

Our own load, geometry, shaft, carrier, frame, bearing and CG calculations are now maintained in [Mechanical work: calculations](../05-mechanical-work/calculations.md). The published calculation ledger remains in section 3 above.

## 7. CAD parameters and material decisions

### Coordinate system

Use the main axle centre as the origin. `y` runs across the trolley, `z` points upward when the frame is upright, and `+x` points toward the payload. The operator/stair ascent direction is toward the back, `−x`. Dimensions below are in millimetres. Give the model named parameters so a clearance correction does not require rebuilding it.

| Part/parameter | Initial CAD value | Material or assembly decision |
| --- | --- | --- |
| Mechanism | Two independent clusters; three wheels per cluster at 120° | Manual, freely rotating clusters and wheels; no gears or drive motor |
| Carrier radius | 190 centre-to-centre | Same on all six arms |
| Individual wheels | Ø200 × 50 tread width; 20 bore; 60 hub length | Elastic solid rubber tread; bearing hub |
| Wheel procurement reference | Blickle POEV 200/20K dimensional envelope | Manufacturer lists 500 kg at 4 km/h on its stated test basis; this is not stair-impact certification or a trolley rating |
| Wheel acceptance requirement | Supplier-rated dynamic capacity ≥150 kg per wheel, verified bore/hub dimensions | Reference model or a documented compatible alternative; availability/price not yet quoted |
| Track | 560 between left/right wheel centre planes (`y = ±280`) | Overall hardware envelope target ≤660 |
| Carrier plates | Four plates, 6 thick; paired inner-face gap 64 | IS 2062 E250 steel; 50 minimum arm width; ≥25 root blend radius |
| Carrier contour | Three swept arms; wheel centres at polar angles 0°, 120°, 240° | Start each arm at radius 55 and angle 15° behind its wheel; smooth centreline to wheel centre, 50-wide envelope; Ø60 end bosses. Mirror handed profiles as needed |
| Carrier clearance | ≥10 to stairs and fixed structure throughout motion | Contour is adjustable within the chosen concept after motion checking |
| Central hub | Turned steel sleeve initial Ø70 × 76 long, 52 bearing seats at both ends | 15 seat depth each, central relief/shoulder geometry and inner-race spacer; turn seats after any welding |
| Hub attachment | Bolted plates to flanged hub; initial 6 × M8 on 90 PCD, Ø110 flange | CAD-check ligament and fastener clearance; hub flange/weld and bolt-group checks before drawings |
| Bearing spacer | Nominal 46 between inner races for the 76-long hub | Exact stack, shoulders, seals and end retention to follow selected bearing drawing |
| Main axle | Solid Ø25; initial overall length 660 including end retention envelope | C45, certified yield ≥300 MPa; machined seats, positive end retention; no axle welding |
| Axle supports | Centres `y = ±195`; cluster lever arm 85 | Split clamps on reinforced chassis brackets; bracket geometry must carry the calculated bending load |
| Wheel axles | Six Ø20 shoulders, about 70 support-centre span | C45 or specified equivalent; positive locking; final length from bearing/washer stack |
| Frame | 420 external width; two uprights and cross-members, 35 × 35 × 2 tube | IS 4923 YSt 240 minimum; use certified actual section properties |
| Frame plane | Upright centreline at `x = 100` | Main axle sits behind the load frame |
| Toe platform | 400 wide × 300 deep, front from `x = 100` to 400; top `z = −155` | 2 mm E250 deck supported on two 30 × 30 × 2 toe rails; add intermediate deck support if needed |
| Toe ground clearance | Rail underside `z = −187`, giving 8 above floor in the nominal two-wheel stance | Corrected during Blender layout: include the 2 mm deck above the 30 mm rails. Check all phases; this is not constant stair clearance |
| Toe gussets | Two 100 × 100 × 4 triangular gussets | E250; weld group to be verified |
| Handle | Grip centre `z = 1005`, `x = 40`; approximately 1200 above nominal floor; grip width 380 | Round grip sleeve on steel crossbar; smooth closed ends |
| Load restraint | Two straps and four reinforced attachment points | Model strap paths and load movement; hardware working loads must be verified |
| Surface finish | Deburr, prepare, prime and paint fabricated steel | Keep bearing fits, wheel contact surfaces and threaded seats free of paint |
| Mass budget | ≤22 kg assembled | CAD mass is a required check, not a result already achieved |

The [Blickle wheel table](https://www.blickle.com/wheels-castors/standard-range/premium-rubber-wheels/premium-rubber-wheels-poev-series) confirms the reference wheel dimensions. [APL Apollo's structural tube catalogue](https://new.aplapollo.com/files/Column_Brochure.pdf), PDF p. 28, lists YSt 240 minimum yield 240 MPa and tensile strength 410 MPa. [SAIL's structural-steel data](https://www.sail.co.in/sites/default/files/product-brochure/2020-03/Structurals.pdf) identifies IS 2062 grades by minimum yield strength. [Ovako's C45 data](https://steelnavigator.ovako.com/steel-grades/c45/) shows why shaft supply condition must be specified. These references support material selection; supplier certificates still define what is actually bought.

### Why these materials

Use mild structural steel for the frame and carriers because the project needs weldable, repairable parts with a clear material specification. Stainless steel is unnecessary for the whole structure at this stage. Aluminium could reduce mass, but weld details and local availability would need a separate comparison. Rubber is selected for tread compliance and traction; the earlier build's reported wet-surface difficulty makes hard plastic wheels a poor starting assumption. Grip still needs measurement on the intended surface.

### What is decided, and what is not yet released

The architecture, payload target, material families, nominal component sizes and modelling cases above are **selected for the next CAD session**. They are sufficient to start a parameterised assembly.

Final carrier outline, axle-support brackets, bearing fits/retention, fastener lengths, deck support and weld sizes are **drawing-release details** dependent on the assembly checks. The selected contour and hub dimensions are starting geometry, not validated manufacturing drawings. A CAD motion study may change these dimensions within this same design; that routine development does not need a new project version.

Descent control is still an unresolved operating requirement. Locking only a carrier does not lock its individual wheels, so a carrier pin alone is not a complete brake. Include space near both hubs for a future control mechanism, but do not label the assembly self-braking. Begin prototype trials with a controlled test restraint. Unrestrained loaded descent is not approved by this research.

## 8. What the CAD session must establish

1. Build the frame, both carrier assemblies, wheel axles, hub/bearing stack, toe plate and representative payload from the parameters above.
2. Measure assembled mass and CG for empty, 10, 25, 40 and 50 kg loads, including lateral offsets and tall/forward loads.
3. Run a complete contact sequence, including first-step engagement, repeated steps and the top landing. Check stair cases A–E, nosings and both cluster phases. Test unequal left/right phasing because the clusters rotate independently.
4. Plot the handle lever arm, load moment and predicted contact forces against carrier angle. Reject positions requiring negative contact reactions, unrealistic friction or interference.
5. Check normal two-side loading, factored one-side loading, toe-tip load, handle pull, frame torsion and local holes/welds. Refine mesh around transitions and demonstrate convergence rather than relying on one coloured stress plot.
6. Check grip access, pinch points, payload retention and turning on landings. Resolve descent control before claiming a complete operational design.
7. Produce the final parts list and fabrication drawings only after these checks and confirmation of purchased wheel/bearing dimensions.

## 9. Proposed test targets

These are project targets selected before tests, not published ergonomic limits or measured achievements.

| Check | Initial acceptance target |
| --- | --- |
| Payload progression | Empty, 10, 25, 40, then 50 kg; proceed only after inspection at each level |
| Stair traversal | Ten complete ascents of a measured 12-riser flight at each accepted load; no catches, uncontrolled reversals, loose joints or payload movement |
| Structural response | No cracks or permanent set above 0.5 mm measurement resolution; toe deflection target ≤3 mm at the static 50 kg payload |
| Pull force | Working target: mean ≤450 N and peak ≤500 N at 50 kg; measure direction and speed. These relatively high forces may make the 50 kg manual operating target unsuitable |
| Comparison | Aim for ≥20% reduction in measured peak pull versus a conventional trolley at the same payload/stairs/speed; report mean force as well |
| Stability | No unplanned lateral lift, payload slip or loss of operator control; record wheel-contact sequence and handle reactions |
| Descent | A defined restraint/braking method and controlled trials are required before releasing loaded descent |
| Surface | Establish dry-surface baseline first; any wet-surface capability needs its own evidence |

Force reduction calculation: `100 × (F_regular − F_tristar)/F_regular`. Record instrument range, calibration, sampling rate and uncertainty. If the manual force target fails, reduce the demonstrated operating payload or develop the powered alternative; do not change the reported measurements to match the target.

## 10. Decision record

**10 October 2026:** selected the manual paired-plate tri-star concept and the nominal dimensions above to begin CAD. The research supports this as a practical prototype direction, but it does not establish a safe 50 kg rating, universal stair compatibility, reduced pull force or controlled descent. Those are the specific outcomes the next modelling and testing stages must demonstrate. Earlier project records remain accessible and unchanged.
