#!/usr/bin/env python3

import shutil 
import os
import distutils
from distutils import dir_util

DIR=os.path.dirname(os.path.realpath(__file__))
CamomileRoot='/Users/Shared/CamomileBin'
CamomileDir=CamomileRoot+'/Examples'
Vst3PluginFolder='/Library/Audio/Plug-Ins/VST3'

for PluginName in os.listdir(DIR):
    SourceCamomile=DIR+'/'+PluginName
    if os.path.isdir(SourceCamomile):
        os.system('cd '+CamomileRoot+' && ./camomile -f '+SourceCamomile+' -o '+Vst3PluginFolder+'/CamomileUtils'+' -v') 
