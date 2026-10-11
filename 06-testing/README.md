# Testing and Improvements

Testing will show whether the built trolley achieves the intended stair-climbing performance. The main questions are whether it crosses repeated steps smoothly, stays controllable, carries the payload without excessive frame movement, and reduces manual pull force.

No measured results from the current rebuild have been recorded yet. Earlier reported outcomes are summarised below. Set the acceptance criteria in the [design requirements](../05-mechanical-work/design-requirements.md) before starting.

## Test sequence

| Test | What to do | What to record |
| --- | --- | --- |
| Assembly and unloaded movement | Check wheel and carrier rotation, alignment, fasteners, and stair clearances without a payload. | Binding, interference, looseness, and movement through each transition. |
| Wheel-first stair contact | After checking the geometry, approach a measured step slowly without payload under controlled restraint. Repeat at the intended trolley tilts and carrier positions. | First part to contact the stair, frame/toe/bracket clearance, axle-to-frame offset, approach direction, tilt and carrier angle. Stop on rigid-part contact; do not force the trolley past it. |
| Static payload test | Apply the planned secured load levels to the supported trolley. | Load, deflection at defined frame points, joint condition, and residual deformation after unloading. |
| Single-step trial | Begin with an unloaded trial, then use planned secured payloads. | Transition behaviour, handle force, catches, wheel contact, and load movement. |
| Full-flight ascent | Traverse the measured consecutive steps with the planned payload levels. | Completed steps, interruptions, peak and average pull force, tilt, and stability observations. |
| Dynamic payload trials | Repeat stair climbs with secured payloads and planned start-stop movements. | Transient force peaks, frame movement, payload shift, and changes after repeated runs. |
| Load-position checks | Test the planned payload positions within the chosen operating limits. | Changes in effort, balance, tilt, and wheel contact. |
| Controlled descent | Check lowering through the selected staircase under a defined procedure. | Operator control, catches, sudden movement, and load stability. |
| Post-test inspection | Inspect the trolley after the runs and compare with its initial condition. | Deformation, loosened joints, wear, cracks, or alignment changes. |

Dynamic payload testing here means testing with a payload while the trolley moves. It does not mean dropping weights onto the frame or leaving the load loose.

## Pull-force comparison

Compare the prototype with a regular trolley using the same payload, staircase, operator, and as closely matched a speed and handle-force direction as practical. Record differences in trolley mass, handle geometry, and load position that cannot be matched.

Use a suitable force gauge or load cell, record its range and measurement uncertainty, and define the sampling method. Repeat runs for both trolleys using the same repetition count and retain individual measurements.

Report peak and average force separately. For either metric, calculate the percentage reduction as:

`100 × (baseline force − prototype force) / baseline force`

Use the same metric and averaging method on both sides, with a nonzero baseline. A negative result means the prototype required more force. Discuss measurement spread and uncertainty before claiming an improvement.

## What counts as a useful result?

- **Smooth traversal:** record catches, interruptions, and abrupt transitions, with video where possible. Describe the conditions rather than simply writing “smooth.”
- **Structural rigidity:** compare measured deflection with the chosen limit and inspect for residual deformation after unloading.
- **Stability:** document load position, operator support, and any tipping tendency through the flight. Successful trials only support conclusions within the tested conditions.
- **Reduced effort:** report the matched force comparison with units, repeated results, and relevant differences between setups.

## Test setup and stopping conditions

Record how the load is secured, how the trolley is restrained if control is lost, and where the operator and any helper stand. Stop if the load shifts, the trolley becomes uncontrollable, a component deforms, or a joint loosens. Do not deliberately seek a rollover.

## Test record

- Date and test ID:
- Prototype configuration:
- Objective and acceptance criteria:
- Stair dimensions and surface:
- Payload, position, and restraint:
- Instruments and measurement uncertainty:
- Procedure, speed, and repetition count:
- Measurements and units:
- Photos or video:
- Result and limitations:
- Problem found and next action:

## Results

| Test ID | Payload and position | Conditions | Measurements | Outcome | Next action |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Keep unsuccessful trials alongside successful ones. Add new test entries as work progresses; routine trials do not need new project versions.

## What the earlier report records

| Area | Earlier reported outcome | Detail still needed |
| --- | --- | --- |
| Stair traversal | Successful movement over different staircase configurations and smooth transitions. | Stair dimensions, run count, payload per run, and motion records. |
| Manual effort | Reduced user effort. | Force measurements and a matched baseline comparison. |
| Payload | A 30–50 kg testing range and a platform described as designed for up to 50 kg. | Individual load records, procedure, and acceptance criteria. |
| Balance | Slight tilting with heavier loads. | Load position, mass, tilt direction, and stair conditions. |
| Traction | Wet or slippery surface performance needed improvement. | Surface details and observations for each trial. |

The photographs show the prototype at different stair-contact positions, but do not establish the load capacity, force reduction, or dynamic response. Keep these earlier reported outcomes separate from the new measurement tables above. Structural deflection and quantitative force data still need to be recovered or measured.
