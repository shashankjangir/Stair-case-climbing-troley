"""Read-only checks against the saved Blender assembly, not its input constants."""
import bpy, json, math, hashlib
from datetime import datetime, timezone
from pathlib import Path
from mathutils import Vector
out=Path(__file__).resolve().parents[1]/'blender'
checks=out.parent/'checks'
checks.mkdir(exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=str(out/'stair-trolley.blend'))
bpy.context.view_layer.update()
objs=list(bpy.context.scene.objects)
def group(prefix): return [o for o in objs if o.name.startswith(prefix)]
def bounds(o):
    vs=[o.matrix_world@Vector(v) for v in o.bound_box]
    return [[min(v[i] for v in vs)*1000,max(v[i] for v in vs)*1000] for i in range(3)]
def near(a,b): assert abs(a-b)<.05,(a,b)
assert len(group('Main axle -'))==1
assert len(group('Carrier '))==4
assert len(group('Wheel tread '))==6
assert len(group('6205 bearing '))==4
plates={}
for o in group('Carrier '):
    bb=bounds(o);near(bb[1][1]-bb[1][0],6);assert bb[2][1]-bb[2][0]>300
    plates[o.name]=bb
for side in [-1,1]:
    pivot=bpy.data.objects[f'Cluster {side} - rotate Y independently']
    wheel=bpy.data.objects[f'Wheel pivot {side} 0 - rotate Y']
    before=wheel.matrix_world.translation.copy()
    pivot.rotation_euler.y=math.radians(20);bpy.context.view_layer.update()
    assert (wheel.matrix_world.translation-before).length>.01
    pivot.rotation_euler.y=0;bpy.context.view_layer.update()
for o in group('Wheel tread '):
    bb=bounds(o);near(bb[0][1]-bb[0][0],200);near(bb[1][1]-bb[1][0],50)
near(bounds(group('Main axle -')[0])[1][1]-bounds(group('Main axle -')[0])[1][0],660)
near(min(bounds(o)[2][0] for o in group('Wheel tread ')),-195)
near(min(bounds(o)[2][0] for o in group('Toe rail ')),-187)
near(bounds(bpy.data.objects['Toe deck 400 x 300 x 2'])[2][1],-155)
result={'saved_file_reopened':True,'checks_passed':['1 shared axle','4 vertical carrier plates, 6 mm thick','6 wheels, 200 x 50 mm','4 cluster bearings','660 mm main axle','8 mm toe floor clearance','cluster pivots carry their wheels'],
'carrier_world_bounds_mm':plates,'scope':'Nominal geometry and parenting only. No stress, mass, contact or stair-motion validation.'}
result['checked_at_utc']=datetime.now(timezone.utc).isoformat()
result['model_sha256']=hashlib.sha256((out/'stair-trolley.blend').read_bytes()).hexdigest()
(checks/'saved-model-checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
