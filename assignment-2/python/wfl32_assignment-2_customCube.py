import maya.standalone
maya.standalone.initialize()

import argparse

parser = argparse.ArgumentParser(description='This script creates a bunch of cubes.')
parser.add_argument('cube_width', type=int, help="Value of cube width")
parser.add_argument('cube_height', type=int, help="Value of cube height")
parser.add_argument('cube_depth', type=int, help="Value of cube depth")
args = parser.parse_args()

import maya.cmds as mc

mc.polyCube(w = args.cube_width, h = args.cube_height, d = args.cube_depth)
print("Your custom cube has been created!")

#The "r" before the path converts string from a normal string to a RAW string.

customPth = r"C:\Users\willr\Desktop\yourCube_01.ma"

mc.file(rename=customPth)
mc.file(save=True, type="mayaAscii")
print("Your cube is saved as 'yourCube_01.ma' to your desktop.")

