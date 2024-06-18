import bpy
import math

if __name__ == '__main__':
    mat = bpy.data.materials.get('Material')
    cubes = list()
    scene = bpy.context.scene
    frame_num = 0
    
# A
    for i in range(-50, 50):
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
        bpy.context.active_object.data.materials.append(mat)

        base = 15 - (i**2)*0.05
       
        bpy.ops.transform.resize(value=(base, base, 0.5))
        bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)
        
        cubes.append(bpy.context.active_object)
        
    for cube in cubes:
        scene.frame_set(frame_num)
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
        frame_num += 1
        scene.frame_set(frame_num)
        cube.rotation_euler[2] = 0
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
# B

    for i in range(-55, 55):
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
        bpy.context.active_object.data.materials.append(mat)

        base = 150 - (i**2)*0.05
        
        bpy.ops.transform.resize(value=(base, base, 0.5))
        bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)
        
        cubes.append(bpy.context.active_object)

# C
    for i in range(0, 51):
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
        bpy.context.active_object.data.materials.append(mat)
        base = i + ( i**2)*0.05
        bpy.ops.transform.resize(value=(base, base, 0.5))
        bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)
       
        cubes.append(bpy.context.active_object)
    for cube in cubes:
        scene.frame_set(frame_num)
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
        frame_num += 1
        scene.frame_set(frame_num)
        cube.rotation_euler[2] = 0
        cube.keyframe_insert(data_path="rotation_euler", index=-1)
