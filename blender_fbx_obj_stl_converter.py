import bpy
import os

# Let's ask for a folder
print("This little script will check a given folder for fbx, .obj and .stl files and convert anything that doesn't have a corresponding file to the other formats.")
folder = input("Please enter folder path: ")

# Let's gather some stats while we're at it.
new_files = []

# Check folder for .obj, .fbx, and .stl files
for file_name in os.listdir(folder):
    file_path = os.path.join(folder, file_name)
    
    if file_name.lower().endswith('.obj'):
        # Check if .obj file has corresponding .fbx and .stl files
        fbx_file_path = file_path[:-4] + '.fbx'
        stl_file_path = file_path[:-4] + '.stl'
    
        if not os.path.exists(fbx_file_path):
            # Convert .obj file to .fbx
            print(f"Converting {file_name} to .fbx...")
            bpy.ops.import_scene.obj(filepath=file_path, use_edges=False, use_smooth_groups=False)
            bpy.ops.export_scene.fbx(filepath=fbx_file_path, use_selection=True, object_types={'MESH'})
            print(f"Conversion completed: {file_name} -> {os.path.basename(fbx_file_path)}")
            new_files.append(fbx_file_path)
        if not os.path.exists(stl_file_path):
            # Convert .obj file to .stl
            print(f"Converting {file_name} to .stl...")
            bpy.ops.import_scene.obj(filepath=file_path, use_edges=False, use_smooth_groups=False)
            bpy.ops.export_mesh.stl(filepath=stl_file_path, use_selection=True)
            print(f"Conversion completed: {file_name} -> {os.path.basename(stl_file_path)}")
            new_files.append(stl_file_path)

    elif file_name.lower().endswith('.fbx'):
        # Check if .fbx file has corresponding .obj and .stl files
        obj_file_path = file_path[:-4] + '.obj'
        stl_file_path = file_path[:-4] + '.stl'
        if not os.path.exists(obj_file_path):
            # Convert .fbx file to .obj
            print(f"Converting {file_name} to .obj...")
            bpy.ops.import_scene.fbx(filepath=file_path)
            bpy.ops.export_scene.obj(filepath=obj_file_path, use_selection=True, use_materials=False)
            print(f"Conversion completed: {file_name} -> {os.path.basename(obj_file_path)}")
            new_files.append(obj_file_path)
        if not os.path.exists(stl_file_path):
            # Convert .fbx file to .stl
            print(f"Converting {file_name} to .stl...")
            bpy.ops.import_scene.fbx(filepath=file_path)
            bpy.ops.export_mesh.stl(filepath=stl_file_path, use_selection=True)
            print(f"Conversion completed: {file_name} -> {os.path.basename(stl_file_path)}")
            new_files.append(stl_file_path)

    elif file_name.lower().endswith('.stl'):
        # Check if .stl file has corresponding .obj and .fbx files
        obj_file_path = file_path[:-4] + '.obj'
        fbx_file_path = file_path[:-4] + '.fbx'
        if not os.path.exists(obj_file_path):
            # Convert .stl file to .obj
            print(f"Converting {file_name} to .obj...")
            bpy.ops.import_mesh.stl(filepath=file_path)
            bpy.ops.export_scene.obj(filepath=obj_file_path, use_selection=True, use_materials=False)
            print(f"Conversion completed: {file_name} -> {os.path.basename(obj_file_path)}")
            new_files.append(obj_file_path)
        if not os.path.exists(fbx_file_path):
            # Convert .stl file to .fbx
            print(f"Converting {file_name} to .fbx...")
            bpy.ops.import_mesh.stl(filepath=file_path)
            bpy.ops.export_scene.fbx(filepath=fbx_file_path, use_selection=True, object_types={'MESH'})
            print(f"Conversion completed: {file_name} -> {os.path.basename(fbx_file_path)}")
            new_files.append(fbx_file_path)

# Summary
if len(new_files) == 0:
    print("No files to convert.")

else:
    print("All done!")
    print("Conversion Summary:")
    print(f"Total conversions: {len(new_files)}")
    print("New files created:")
    for new_file in new_files:
        print(new_file)