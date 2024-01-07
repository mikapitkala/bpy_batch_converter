# Batch 3D File Converter for Blender

This little Python script automates the conversion of 3D model files between `.fbx`, `.obj`, and `.stl` formats. It scans a specified directory for 3D models and converts anything that doesn't have a corresponding file in the other formats using the Blender Python API.

This is mostly for purchased asset and kitbash packs *somehow* always managing to be in the wrong format, when I try to use them in different apps (sculpting, CAD, modeling).

## Requirements

- Blender 2.80 or later. Will *probably* work in other versions, but that's what I was using at the time.

## Installation

No installation is required for the script. Simply run it within Blender or whatever you use for Python.


## Usage

1. Open Blender and go to the `Scripting` tab.
2. Open the script file `blender_fbx_obj_stl_converter.py` in Blender's text editor.
3. Press the `Run Script` button to execute the script.
4. When prompted (in the System console), enter the full path to the directory containing your `.fbx`, `.obj`, or `.stl` files.

Or just run it from your code editor of choice.

## Limitations

- Relies on Blender's Python API (`bpy`), so that needs to be there.
- It does not currently handle exceptions or errors during file operations.
- Geometry only. No UVs, textures, bones, animations or anything.

## License

This script is provided "AS IS", without warranty of any kind.
