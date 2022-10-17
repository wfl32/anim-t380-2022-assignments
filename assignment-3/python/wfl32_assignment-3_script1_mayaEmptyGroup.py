import os
import maya.standalone
maya.standalone.initialize()
import maya.cmds as mc

asset = os.getenv('asset')

fileName = asset
fileNameExt = str(fileName + ".ma")
pathInput = 'assets'+os.sep+asset+os.sep+'maya'+os.sep+'scenes'
finalDirectory = str(pathInput) + fileNameExt

mc.group( em=True, name=asset )

mc.file(rename = finalDirectory)
mc.file(save=True, type="mayaAscii")

print("worked?")