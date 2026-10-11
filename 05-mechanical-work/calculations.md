# Preliminary engineering calculations

These calculations are original checks for the proposed rebuild. They are not results from the ten papers or the earlier prototype. Dimensions are nominal and results are rounded. Use steel `E = 200,000 MPa`, density `7850 kg/m³` as engineering model assumptions. Recalculate with actual section properties, measured mass and material certificates.

## 1 Loads and design factors

```text
Payload target mp = 50 kg
Trolley mass budget mt = 22 kg
Total m = 72 kg
Static weight W = mg = 706.32 N
Preliminary dynamic multiplier Kd = 2.0
Design vertical load Pd = Kd W = 1412.64 N
Normal symmetric side load = Pd/2 = 706.32 N
Asymmetric screening case: one cluster/wheel takes Pd = 1412.64 N
```

The multiplier is a selected design allowance, not a measured stair-impact factor. One-sided support also introduces chassis torsion and tipping; the component check does not make that operating condition stable. Use a minimum yield margin of 2 against the factored nominal stresses, then check local concentrations, welds and joint loads separately. Do not divide applied loads by a safety factor.

## 2 Wheel and carrier geometry

```text
R = 190 mm; wheel radius r = 100 mm; carrier arm half-width t = 25 mm
Adjacent wheel-centre spacing s = √3 × 190 = 329.09 mm
Wheel-to-wheel gap s − 2r = 129.09 mm
Swept cluster diameter = 2(R+r) = 580 mm
Axle height with two lower wheels on a flat floor = R/2+r = 195 mm
```

Substituting fixed `R = 190 mm` in the published clearance expression gives approximate minimum radii of 77.36, 78.67 and 76.18 mm for A/B/C; D/E give 79.63/82.49 mm. The chosen 100 mm radius exceeds these screening values. Because the formula assumes a specific arm shape and contact arrangement, this is only a useful starting check. The CAD requirement is **at least 10 mm nominal rigid-part clearance** throughout the motion, including axle brackets, hubs and toe plate. Wheel contact is intentional; tyre compression and manufacturing variation must also be allowed for.

## 3 Climbing work, force and torque

For a complete cycle with the same posture at both ends, energy conservation gives:

```text
Minimum work per step = W h
Nominal case B: 706.32 × 0.175 = 123.61 J
12 rises: 1483.27 J (before friction and impact losses)
Ideal equivalent force along the stair slope = W sinα
A: 315.88 N; B: 379.21 N; C: 427.38 N
```

These are ideal average forces for an uphill displacement along the slope, not predicted handle-force peaks. A tri-star mechanism can reduce difficult transition peaks compared with a plain wheel; it does not eliminate the work needed to raise the load.

At a particular stair contact, take moments about that contact:

```text
F_handle = (W × horizontal CG lever arm + resisting moment) / handle-force lever arm
M = force × perpendicular distance
Illustration: CG lever 0.25 m and handle lever 0.80 m → F = 220.73 N
With only a 0.40 m handle lever → F = 441.45 N, before losses
```

The illustration is a holding/contact snapshot, not a substitute for the cycle work calculation. CAD must calculate both lever arms at each position.

A cluster-centre screening moment `W_side R` is 67.10 N·m per side statically, 134.20 N·m per side with the factor of two, and 268.40 N·m for the factored one-sided case. These values help screen carriers; they are **not motor torque specifications**. The fixed main axle supports bearing reactions and bending; it does not transmit a drive torque in this architecture.

## 4 Main axle

Use a solid 25 mm C45 axle, clamped to the chassis. Cluster wheel centre planes are at `y = ±280 mm`; frame support centres at `y = ±195 mm`. Nominal outboard lever arm is 85 mm.

```text
Worst screening side load P = 1412.64 N
M = P × 85 = 120,074.4 N·mm
Z = πd³/32
σ_b = 32M/(πd³) = 78.28 MPa for d = 25 mm
```

Require certified yield strength of at least 300 MPa for the purchased shaft condition: nominal margin is then 3.83. C45 strength depends on heat treatment and size; the grade name alone is insufficient. Shoulders, grooves and clamp contact need local checks. Do not weld the C45 axle to the mild-steel frame.

## 5 Wheel axles and paired carriers

Each 20 mm wheel axle is supported by both plates. With a 70 mm support-centre span and a centred worst-case force:

```text
Wheel axle M = PL/4 = 1412.64 × 70/4 = 24,721.2 N·mm
σ_b = 32M/(π × 20³) = 31.48 MPa
Average double-shear stress = P/[2(πd²/4)] = 2.25 MPa

Carrier pair: two plates, each 6 mm thick, minimum arm width 50 mm
Combined in-plane section modulus Z = 2 × (6 × 50²/6) = 5000 mm³
Conservative arm moment = P × 190 = 268,401.6 N·mm
Nominal arm stress = M/Z = 53.68 MPa
Illustrative concentration multiplier 2 → 107.36 MPa
At 250 MPa yield: indicative margin = 2.33
Hole bearing stress per plate = (P/2)/(6 × 20) = 5.89 MPa
```

The arm is curved, perforated and connected to a hub, so the straight-strip estimate cannot replace local FEA. Check unequal sharing between plates and out-of-plane bending. Keep threads outside bearing and shear planes; use shoulders/spacers so tightening does not pinch the wheel bearings.

## 6 Frame and toe support

For a nominal sharp-corner 30 × 30 × 2 mm square tube:

```text
A = 30² − 26² = 224 mm²
I = (30⁴ − 26⁴)/12 = 29,418.67 mm⁴
Z = I/15 = 1961.24 mm³
Mass per metre = 224 × 0.00785 = 1.7584 kg/m

Two 300 mm toe rails; half the factored total load at each rail tip:
P_rail = 706.32 N
M = P_rail × 300 = 211,896 N·mm
σ = M/Z = 108.04 MPa
δ_tip = PL³/(3EI) = 1.08 mm
Nominal yield margin for YSt 240 = 240/108.04 = 2.22
```

Actual corner radii and wall tolerance change the section properties. Add triangular gussets at both toe-to-upright joints. For the main frame, select **35 × 35 × 2 mm** tube: `I = 48,092 mm⁴`, `Z = 2748.11 mm³`, and nominal mass `2.0724 kg/m`. A 500 N horizontal handle force shared between two uprights at a 1000 mm lever gives `σ = (250 × 1000)/2748.11 = 90.97 MPa`, a nominal yield margin of 2.64. The smaller 30 mm section would give 127.47 MPa and miss the selected margin of two in that isolated case; retain it only for the toe supports. Do not add these results blindly or claim the frame passes: the assembled load cases must combine handle, payload and wheel reactions with their actual directions.

For an initial toe-joint weld-group estimate, two 30 mm weld lines with 2 mm effective throat and 30 mm separation have `A_w = 120 mm²`, `I_w ≈ 27,000 mm⁴`. The above moment gives `M×15/I_w ≈ 117.7 MPa`, plus approximately 5.9 MPa direct shear. This demonstrates why a small ungusseted end joint is not enough to approve from the tube calculation alone. Model 100 × 100 × 4 mm gussets, then size their welds from the final load path and welding procedure. Weld details remain a drawing-release check.

## 7 Cluster bearings

Use two 6205-size deep-groove bearings per cluster, four total: **25 mm bore × 52 mm outside diameter × 15 mm width**. Specify sealed equivalents and confirm the chosen suffix and fits. The [SKF 6205 data sheet](https://cdn.skfmediahub.skf.com/api/public/094f3ab4599ba988/pdf_preview_medium/094f3ab4599ba988_pdf_preview_medium.pdf) gives reference ratings `C = 14.8 kN`, `C0 = 7.8 kN` for its open bearing; do not silently transfer every detail to an unverified equivalent.

For a deliberately conservative screening load of 1.413 kN on one bearing, `C0/P = 5.52`. The elementary radial life calculation is `(14.8/1.413)³ ≈ 1150 million revolutions`. This is not a trolley service-life prediction: oscillation, impact, contamination, bearing fit, axial loads and unequal load sharing matter more than a large ideal life number here. Actual outer-ring rotation also needs the manufacturer's bearing selection method.

## 8 Centre of gravity and stability

Calculate the combined CG from actual CAD masses:

```text
xCG = Σ(mi xi)/Σmi; yCG = Σ(mi yi)/Σmi; zCG = Σ(mi zi)/Σmi
For backward tilt β: x' = x cosβ − z sinβ; z' = x sinβ + z cosβ
Static lateral tipping screen: tanγ = (B/2 − |e|)/H
```

`B` is the actual lateral support span, `e` lateral CG offset, and `H` CG height above the support plane. With `B = 560 mm`, `e = 25 mm`, `H = 600 mm`, the simplified lateral tipping angle is about 23.0°. This is **not an allowed operating slope**. Step transitions change contacts and may leave one side unsupported. CAD must check the changing support/contact geometry, handle reaction and payload placement through a full cycle. A hand trolley is operator-supported longitudinally, so an unsupported support-polygon test alone is insufficient.

Secure a compact load with two straps. Initially limit lateral payload-CG offset to ±25 mm, payload depth to 300 mm and height to 600 mm. These are selected test limits, to be narrowed if stability requires it.


Source context: [literature review and design basis](../03-research/trolley-research-and-cad-design-basis.md). Current geometry is described in the [modelling plan](../04-cad/modelling-plan.md). These screening calculations have not been replaced by analysis of the finished assembly.
