
#bunny.model.wmuto.2.ma

import maya.standalone
maya.standalone.initialize()

import maya.cmds as mc
import os

filepath = mc.file(q = True, sn = True)
filename = os.path.basename(filepath)

#*
rawName,ext = os.path.splitext(filename)
num = int(rawName.split(".")[-1])
num +=1

parts = rawName.split(".")
parts[-1] = str(num)
newName = ".".join(parts)
finalName = newName + "." + ext
#*

mc.file( rename = finalName )
