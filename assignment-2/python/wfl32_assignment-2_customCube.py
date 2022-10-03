# Terminal statements for ease of use.
print("\n-----------------------------------------------------------")
print("Please enter your custom cube's WIDTH, HEIGHT, DEPTH, FILEPATH, and FILENAME")
print("Your input should look like this: \n" + r"12 6 190 C:\Users\<USERNAME>\Desktop\ customCube_v01")
print("-----------------------------------------------------------\n")

import maya.standalone
maya.standalone.initialize()

import argparse

parser = argparse.ArgumentParser(description='This script creates a bunch of cubes.')
parser.add_argument('cube_width', type=int, help="Value of cube width")
parser.add_argument('cube_height', type=int, help="Value of cube height")
parser.add_argument('cube_depth', type=int, help="Value of cube depth")
parser.add_argument('desktopPath', type=str, help="Copy a path of directory. Idealy the path to the Desktop")
parser.add_argument('fileName', type=str, help="Name of your file")
args = parser.parse_args()


import maya.cmds as mc

# User input to  declare variables
fileName = args.fileName
fileNameExt = str(fileName + ".ma")
pathInput = args.desktopPath
finalDirectory = str(pathInput) + fileNameExt

# Custom Cube tool starts here.
mc.polyCube(w = args.cube_width, h = args.cube_height, d = args.cube_depth)
print("Your custom cube has been created!")

# Creates your cube under custom file and location here.
mc.file(rename = finalDirectory)
mc.file(save=True, type="mayaAscii")
print("Your cube is saved as '" + fileNameExt + "' to this path: \n" + pathInput + "\n")