import os
asset = os.getenv('asset')
if not os.path.isdir('assets'):
    os.mkdir('assets')
if not os.path.isdir('assets'+os.sep+asset):
    os.mkdir('assets'+os.sep+asset)
if not os.path.isdir('assets'+os.sep+asset+os.sep+'maya'):
    os.mkdir('assets'+os.sep+asset+os.sep+'maya')
if not os.path.isdir('assets'+os.sep+asset+os.sep+'maya'+os.sep+'scenes'):
    os.mkdir('assets'+os.sep+asset+os.sep+'maya'+os.sep+'scenes')
