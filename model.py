#using blender 
import bpy
verts = [(0,0,0),(0,9,0),(9,9,0),(9,0,0),(0,0,9),(0,9,9),(9,9,9),(9,0,9)]
faces = [(0,1,2,3),(7,6,5,4),(0,4,5,1),(1,5,6,1),(2,6,7,3),(3,7,4,0)]

mymesh = bpy.data.meshes.new("Cube")
myobject = bpy.data.objects.new("Cube",mymesh)

myobject.location = bpy.context.scence.cursor_location
bpy.context.scene.objects.link(myobject)

mymesh.from_pydata(verts,[],faces)
mymesh.update(calc_edges=True)