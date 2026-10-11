"""Rebuild the preliminary trolley in a fresh Blender background process.
Run: blender --background --factory-startup --python build_blender.py
Source dimensions are mm; Blender mesh coordinates are metres.
This is a geometry prototype, not a contact simulation or fabrication release.
"""
import bpy, math, sys, json
from pathlib import Path
from mathutils import Vector
sys.path.insert(0, str(Path(__file__).parent))
import params as p
OUT = Path(__file__).resolve().parents[1] / 'blender'
OUT.mkdir(exist_ok=True)
PREVIEWS = OUT.parent / 'previews'
CHECKS = OUT.parent / 'checks'
PREVIEWS.mkdir(exist_ok=True)
CHECKS.mkdir(exist_ok=True)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.context.preferences.filepaths.save_version = 0
scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
scene.unit_settings.length_unit = 'MILLIMETERS'

def mat(name, color, metal=0, rough=.45):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    bs=m.node_tree.nodes.get('Principled BSDF'); bs.inputs['Base Color'].default_value=(*color,1)
    bs.inputs['Metallic'].default_value=metal; bs.inputs['Roughness'].default_value=rough
    return m
steel=mat('Painted steel - teal',(.025,.27,.29),.65)
plate=mat('E250 carriers - warm orange',(.95,.28,.045),.55)
metal=mat('Machined steel',(.43,.49,.55),.8,.27)
rubber=mat('Rubber tread',(.022,.027,.034),0,.8)
hubmat=mat('Wheel centre',(.15,.18,.21),.25)
deckmat=mat('Deck steel',(.25,.31,.35),.7)
loadmat=mat('Payload reference',(.62,.43,.23))
floor=mat('Studio floor',(.075,.095,.12))
stairmat=mat('Stair reference',(.36,.39,.42))

def collection(name):
    c=bpy.data.collections.new(name); scene.collection.children.link(c); return c
frame=collection('01 Frame and fixed axle')
left=collection('02 Left cluster'); right=collection('03 Right cluster')
payload=collection('04 Payload reference - hidden')
stairs=collection('05 Stair case B - hidden')
studio=collection('06 Presentation')

def finish(o,name,material,c):
    o.name=name
    for co in list(o.users_collection): co.objects.unlink(o)
    c.objects.link(o)
    if material:o.data.materials.append(material)
    return o
def cube(name,loc,size,material,c):
    bpy.ops.mesh.primitive_cube_add(size=1,location=Vector(loc)*.001)
    o=bpy.context.object; o.dimensions=Vector(size)*.001
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    return finish(o,name,material,c)
def cyl(name,loc,r,length,material,c,axis='Y',vertices=64):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r*.001,depth=length*.001,location=Vector(loc)*.001)
    o=bpy.context.object
    if axis=='Y':o.rotation_euler[0]=math.pi/2
    if axis=='X':o.rotation_euler[1]=math.pi/2
    return finish(o,name,material,c)
def boolean(o,tool,operation='DIFFERENCE'):
    bpy.context.view_layer.objects.active=o
    mod=o.modifiers.new(operation,'BOOLEAN');mod.operation=operation;mod.solver='EXACT';mod.object=tool
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(tool,do_unlink=True)
def ring(name,loc,ro,ri,length,material,c):
    o=cyl(name,loc,ro,length,material,c)
    boolean(o,cyl('tool',loc,ri,length+2,None,c));return o
def beam(name,a,b,size,wall,material,c):
    a,b=Vector(a),Vector(b); length=(b-a).length
    o=cube(name,(a+b)/2,(size,size,length),material,c)
    boolean(o,cube('tool',(a+b)/2,(size-2*wall,size-2*wall,length+2),None,c))
    o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler();return o
def prism(name,points,y,thick,material,c):
    n=len(points);verts=[(x*.001,(y+dy)*.001,z*.001) for dy in [-thick/2,thick/2] for x,z in points]
    faces=[tuple(reversed(range(n))),tuple(range(n,2*n))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
    mesh=bpy.data.meshes.new(name);mesh.from_pydata(verts,[],faces);mesh.update()
    o=bpy.data.objects.new(name,mesh);c.objects.link(o)
    if material:mesh.materials.append(material)
    # Recalculate winding for reliable booleans.
    bpy.context.view_layer.objects.active=o;o.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT');bpy.ops.mesh.select_all(action='SELECT');bpy.ops.mesh.normals_make_consistent(inside=False);bpy.ops.object.mode_set(mode='OBJECT');o.select_set(False)
    return o
def empty(name,c,loc=(0,0,0)):
    o=bpy.data.objects.new(name,None);c.objects.link(o);o.location=Vector(loc)*.001;return o
def parent_keep(o,root):
    matrix=o.matrix_world.copy();o.parent=root;o.matrix_world=matrix

# Tubular frame. Toe deck top remains -155; rails bottom is -187.
uy=(p.FRAME_EXT_WIDTH-p.FRAME_TUBE_SIZE)/2
for side in [-1,1]:
    y=side*uy
    beam(f'Upright {side}',(100,y,-157),(100,y,970),35,2,steel,frame)
    beam(f'Handle return {side}',(100,y,970),(40,y,1005),35,2,steel,frame)
    beam(f'Toe rail {side}',(100,side*175,-172),(400,side*175,-172),30,2,steel,frame)
    prism(f'Toe gusset {side}',[(117.5,-157),(217.5,-157),(117.5,-57)],side*175,4,steel,frame)
    # Sleeve-support bracket: preliminary envelope, split at z=0.
    for z in [-13,13]:
        o=cube(f'Split clamp {side} {z}',(0,side*195,z),(52,30,25),metal,frame)
        boolean(o,cyl('tool',(0,side*195,0),12.5,34,None,frame))
    beam(f'Axle bracket link {side}',(26,side*195,0),(82.5,side*195,0),35,2,steel,frame)
for z in [-130,350,900]:beam(f'Crossmember {z}',(100,-175,z),(100,175,z),35,2,steel,frame)
cube('Toe deck 400 x 300 x 2',(250,0,-156),(300,400,2),deckmat,frame)
beam('Intermediate deck support',(115,0,-172),(385,0,-172),30,2,steel,frame)
cyl('Handle bar',(40,0,1005),12.5,380,metal,frame)
for y in [-125,125]:ring('Handle grip',(40,y,1005),16,12.5,115,rubber,frame)
axle=cyl('Main axle - single shared shaft',(0,0,0),12.5,660,metal,frame)
axle['material_spec']='C45; certify yield >=300 MPa';axle['retention_status']='End hardware detail pending'

# One connected plate, copied to four locations. Profile fillets remain provisional.
base=cyl('Carrier template',(0,0,0),p.FLANGE_DIAMETER/2,p.PLATE_THICKNESS,plate,left)
angles=[math.radians(a+p.FLAT_PHASE_DEG) for a in p.WHEEL_ANGLES_DEG]
for a in angles:
    pts=[]
    centres=[]
    for i in range(13):
        t=i/12; rad=45+(p.CARRIER_RADIUS-45)*t;theta=a-math.radians(15)*(1-t)**2
        centres.append(Vector((rad*math.cos(theta),rad*math.sin(theta))))
    for i,pt in enumerate(centres):
        tangent=centres[min(i+1,12)]-centres[max(i-1,0)];normal=Vector((-tangent.y,tangent.x)).normalized()*(p.ARM_WIDTH/2)
        pts.append(tuple(pt+normal))
    for i in reversed(range(13)):
        pt=centres[i];tangent=centres[min(i+1,12)]-centres[max(i-1,0)];normal=Vector((-tangent.y,tangent.x)).normalized()*(p.ARM_WIDTH/2)
        pts.append(tuple(pt-normal))
    boolean(base,prism('arm tool',pts,0,p.PLATE_THICKNESS,None,left),'UNION')
    loc=(p.CARRIER_RADIUS*math.cos(a),0,p.CARRIER_RADIUS*math.sin(a))
    boolean(base,cyl('boss tool',loc,p.END_BOSS_DIAMETER/2,p.PLATE_THICKNESS,None,left),'UNION')
    boolean(base,cyl('axle hole tool',loc,p.WHEEL_AXLE_HOLE/2,10,None,left))
boolean(base,cyl('centre hole tool',(0,0,0),p.PLATE_CENTRE_BORE/2,10,None,left))
for i in range(6):
    a=i*math.tau/6
    boolean(base,cyl('bolt hole',(45*math.cos(a),0,45*math.sin(a)),4.5,10,None,left))
bpy.ops.object.select_all(action='DESELECT')
base.select_set(True);bpy.context.view_layer.objects.active=base
bpy.ops.object.transform_apply(location=False,rotation=True,scale=True)
template=base.data.copy();bpy.data.objects.remove(base,do_unlink=True)

for side,c in [(-1,left),(1,right)]:
    y=side*p.HALF_TRACK
    root=empty(f'Cluster {side} - rotate Y independently',c,(0,y,0))
    for off in [-35,35]:
        o=bpy.data.objects.new(f'Carrier {side} {off}',template);c.objects.link(o);o.location.y=(y+off)*.001
        o['profile_status']='Root blend and stress validation pending'
    # Two internal flanges: outer mating faces at +/-32, plates occupy 32..38.
    hub=ring(f'Hub sleeve {side}',(0,y,0),35,20,76,metal,c)
    for off in [-30.5,30.5]:boolean(hub,cyl('bearing seat',(0,y+off,0),26,15.02,None,c))
    for off in [-29,29]:
        fl=ring(f'Hub flange {side} {off}',(0,y+off,0),55,35,6,metal,c)
        for i in range(6):
            a=i*math.tau/6;x,z=45*math.cos(a),45*math.sin(a)
            boolean(fl,cyl('tap envelope',(x,y+off,z),3.4,10,None,c))
            cyl('M8 bolt head envelope',(x,y+(-41 if off<0 else 41),z),6.5,6,metal,c,vertices=6)
    for off in [-30.5,30.5]:ring(f'6205 bearing {side} {off}',(0,y+off,0),26,12.5,15,hubmat,c)
    ring('Inner race spacer',(0,y,0),18,12.6,46,metal,c)
    for i,a in enumerate(angles):
        x,z=p.CARRIER_RADIUS*math.cos(a),p.CARRIER_RADIUS*math.sin(a)
        spin=empty(f'Wheel pivot {side} {i} - rotate Y',c,(x,y,z))
        tyre=ring(f'Wheel tread {side} {i}',(x,y,z),p.WHEEL_RADIUS,65,p.WHEEL_TREAD_WIDTH,rubber,c)
        centre=ring(f'Wheel hub envelope {side} {i}',(x,y,z),65,p.WHEEL_BORE/2,p.WHEEL_HUB_LENGTH,hubmat,c)
        for ob in [tyre,centre]:parent_keep(ob,spin)
        cyl(f'Wheel axle {side} {i}',(x,y,z),10,88,metal,c)
        for off in [-31,31]:ring('Wheel spacing washer',(x,y+off,z),15,10.25,2,metal,c)
        for off in [-41,41]:cyl('Wheel retention envelope',(x,y+off,z),15,6,metal,c,vertices=6)
    bpy.context.view_layer.update()
    for ob in list(c.objects):
        if ob!=root and ob.parent is None:parent_keep(ob,root)
    root['phase_note']='Starting flat-floor phase; no collision solver or automatic stair traversal'

box=cube('Payload reference - illustrative 50 kg',(260,0,-5),(280,300,300),loadmat,payload)
box['assigned_payload_kg']=50
payload.hide_render=True;payload.hide_viewport=True
# Case B rises towards -X. First riser at x=-600, clear of trolley in initial stance.
for i in range(12):
    h=(i+1)*175
    cube(f'B tread {i+1}',(-600-(i+.5)*275,0,-195+h/2),(275,1000,h),stairmat,stairs)
cube('B lower landing',(0,0,-245),(1200,1200,100),stairmat,stairs)
cube('B upper landing',(-4500,0,1855),(1200,1200,100),stairmat,stairs)
stairs.hide_render=True;stairs.hide_viewport=True

# Helpful native notes and source parameters travel with the .blend.
notes=bpy.data.texts.new('READ ME - model status')
notes.write('Preliminary geometry assembly, 10 October 2026. Units displayed in mm.\n'
'Separate collections: frame, left/right clusters, hidden payload, hidden case-B stairs, studio.\n'
'Rotate each cluster empty about local Y; wheel pivot empties rotate each wheel. No motion/contact simulation is installed.\n'
'Edit scripts/params.py and rerun build_blender.py to regenerate dimensions. Custom properties are records, not live geometry drivers.\n'
'Flanges, split-clamp envelopes, carrier root blends, fastener retention and fits need detailed engineering.\n'
'Nominal ground clearance is 8 mm. Wheel mass, complete mass/CG, stair clearance, stresses and payload capacity are NOT verified.\n'
'No native SolidWorks/STEP solids are produced. Do not use as fabrication drawings.\n')
txt=bpy.data.texts.new('params.py - source snapshot');txt.write(Path(p.__file__).read_text(encoding='utf-8'))
scene['design_status']='Preliminary geometry only';scene['payload_target_kg']=50
scene['carrier_radius_mm']=190;scene['wheel_diameter_mm']=200;scene['toe_clearance_mm']=8
cube('Studio floor',(0,0,-210),(5000,5000,30),floor,studio)
bpy.ops.object.camera_add(location=(2.4,-3.1,1.9));cam=bpy.context.object;finish(cam,'Assembly camera',None,studio)
cam.rotation_euler=(Vector((.06,0,.4))-cam.location).to_track_quat('-Z','Y').to_euler()
cam.data.type='ORTHO';cam.data.ortho_scale=1.85;scene.camera=cam
for name,loc,power,size in [('Key',(1,-2,3),700,3),('Fill',(-2,-1,1.5),450,2),('Rim',(0,2,2),800,2)]:
    bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;finish(o,name,None,studio)
    o.data.energy=power;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(Vector((0,0,.4))-o.location).to_track_quat('-Z','Y').to_euler()
scene.render.engine='CYCLES';scene.cycles.samples=32
scene.render.resolution_x=1300;scene.render.resolution_y=1300;scene.render.resolution_percentage=100
scene.world.color=(.2,.2,.2)
bpy.ops.object.select_all(action='DESELECT')
for area in bpy.context.screen.areas:
    if area.type=='VIEW_3D':
        area.spaces.active.region_3d.view_distance=2
        area.spaces.active.region_3d.view_location=(0,0,.4)
        area.spaces.active.shading.type='MATERIAL'
scene.render.filepath=str(PREVIEWS/'assembly-preview.png')
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'stair-trolley.blend'))
report={'status':'geometry checks only','main_axles':sum(o.name.startswith('Main axle -') for o in scene.objects),
'carrier_plates':sum(o.name.startswith('Carrier ') for o in scene.objects),'wheels':sum(o.name.startswith('Wheel tread ') for o in scene.objects),
'cluster_bearings':sum(o.name.startswith('6205 bearing ') for o in scene.objects),'toe_ground_clearance_mm':p.TOE_GROUND_CLEARANCE,
'wheel_centres_mm':[[round(p.CARRIER_RADIUS*math.cos(a),4),side*280,round(p.CARRIER_RADIUS*math.sin(a),4)] for side in [-1,1] for a in angles],
'not_verified':['mass and CG','stress','contact motion','stair clearance','carrier root blends','fits and retention','descent control']}
assert report['main_axles']==1 and report['carrier_plates']==4 and report['wheels']==6 and report['cluster_bearings']==4
(CHECKS/'geometry-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
bpy.ops.render.render(write_still=True)
print('BUILD COMPLETE',str(OUT))
