"""
Stair-climbing trolley — shared parameters for CAD generation.
All values from research document §7 (trolley-research-and-cad-design-basis.md).
Units: mm throughout.
"""

import math

# ── Wheel ──────────────────────────────────────────────────────────────
WHEEL_RADIUS       = 100.0      # r_wheel; Ø200
WHEEL_DIAMETER     = 200.0
WHEEL_BORE         = 20.0       # bore diameter
WHEEL_TREAD_WIDTH  = 50.0       # tread width
WHEEL_HUB_LENGTH   = 60.0       # hub length

# ── Carrier ────────────────────────────────────────────────────────────
CARRIER_RADIUS     = 190.0      # R; centre-to-centre distance to wheel axle
PLATE_THICKNESS    = 6.0        # carrier plate thickness
PLATE_GAP          = 64.0       # inner-face gap between paired plates
ARM_WIDTH          = 50.0       # minimum arm width
ARM_ROOT_RADIUS    = 25.0       # root blend radius
END_BOSS_DIAMETER  = 60.0       # boss at wheel centre
WHEEL_ANGLES_DEG   = [0.0, 120.0, 240.0]   # polar angles for wheel centres
ARM_START_RADIUS   = 55.0       # where each arm begins
ARM_OFFSET_DEG     = 15.0       # arm starts 15° behind its wheel

# ── Central hub ────────────────────────────────────────────────────────
HUB_OD             = 70.0       # outer diameter
HUB_LENGTH         = 76.0       # total length
HUB_SEAT_DIAMETER  = 52.0       # bearing seat diameter
HUB_SEAT_DEPTH     = 15.0       # bearing seat depth each end
FLANGE_DIAMETER    = 110.0      # flange OD
BOLT_PCD           = 90.0       # bolt pattern pitch circle
BOLT_COUNT         = 6          # number of M8 bolts
BOLT_HOLE_DIAMETER = 9.0        # clearance holes in carrier plate for M8
SPACER_LENGTH      = 46.0       # between inner races

# ── Bearings (6205-2RS) ───────────────────────────────────────────────
BEARING_BORE       = 25.0
BEARING_OD         = 52.0
BEARING_WIDTH      = 15.0

# ── Main axle ─────────────────────────────────────────────────────────
MAIN_AXLE_DIAMETER = 25.0
MAIN_AXLE_LENGTH   = 660.0

# ── Wheel axle ────────────────────────────────────────────────────────
WHEEL_AXLE_DIAMETER = 20.0
WHEEL_AXLE_SUPPORT_SPAN = 70.0  # support-centre span

# ── Track and positioning ─────────────────────────────────────────────
TRACK_WIDTH        = 560.0      # wheel-centre track (y = ±280)
HALF_TRACK         = 280.0
AXLE_SUPPORT_Y     = 195.0      # axle support centre from origin

# ── Frame ─────────────────────────────────────────────────────────────
FRAME_TUBE_SIZE    = 35.0       # 35 × 35 × 2 mm
FRAME_WALL         = 2.0
FRAME_INNER        = FRAME_TUBE_SIZE - 2 * FRAME_WALL   # 31 mm
FRAME_EXT_WIDTH    = 420.0      # external width
UPRIGHT_X          = 100.0      # upright centreline x position

# ── Toe platform ──────────────────────────────────────────────────────
TOE_TUBE_SIZE      = 30.0       # 30 × 30 × 2 mm
TOE_WALL           = 2.0
TOE_DEPTH          = 300.0      # x = 100 to 400
TOE_WIDTH          = 400.0
TOE_TOP_Z          = -155.0     # top of deck
DECK_THICKNESS     = 2.0
GUSSET_SIZE        = 100.0      # gusset leg length
GUSSET_THICKNESS   = 4.0

# ── Handle ────────────────────────────────────────────────────────────
HANDLE_Z           = 1005.0     # grip centre z
HANDLE_X           = 40.0       # grip centre x
HANDLE_GRIP_WIDTH  = 380.0      # grip width
HANDLE_TUBE_OD     = 25.0       # crossbar outer diameter (assumed)
HANDLE_SLEEVE_OD   = 32.0       # grip sleeve outer diameter (assumed)

# ── Stair cases ───────────────────────────────────────────────────────
STAIR_CASES = {
    "A": {"riser": 150.0, "tread": 300.0},
    "B": {"riser": 175.0, "tread": 275.0},   # nominal design case
    "C": {"riser": 190.0, "tread": 250.0},
    "D": {"riser": 150.0, "tread": 350.0},
    "E": {"riser": 190.0, "tread": 300.0},
}
N_RISERS           = 12
STAIR_WIDTH        = 1000.0
LANDING_SIZE       = 1200.0     # 1200 × 1200 mm landing

# ── Derived geometry ──────────────────────────────────────────────────
SWEPT_DIAMETER     = 2 * (CARRIER_RADIUS + WHEEL_RADIUS)  # 580 mm
WHEEL_SPACING      = math.sqrt(3) * CARRIER_RADIUS         # ~329.09 mm
WHEEL_GAP          = WHEEL_SPACING - 2 * WHEEL_RADIUS      # ~129.09 mm

# First Blender assembly choices, 10 October 2026. Dimensions remain preliminary.
PLATE_CENTRE_BORE = 70.5  # clearance around the sleeve, not a bearing fit
WHEEL_AXLE_HOLE = 20.5
FLANGE_THICKNESS = 6.0
HUB_MIDDLE_BORE = 40.0
FLAT_PHASE_DEG = 90.0  # one upper wheel, two lower wheels in the XZ plane
TOE_UNDERSIDE_Z = TOE_TOP_Z - DECK_THICKNESS - TOE_TUBE_SIZE
FLAT_AXLE_HEIGHT = CARRIER_RADIUS / 2 + WHEEL_RADIUS
TOE_GROUND_CLEARANCE = FLAT_AXLE_HEIGHT + TOE_UNDERSIDE_Z  # 8 mm
