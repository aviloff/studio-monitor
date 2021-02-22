#!/usr/bin/env python3

# import time
import shutil 
import os
import distutils
from distutils import dir_util

DIR=os.path.dirname(os.path.realpath(__file__))
CamomileRoot='/Users/Shared/CamomileBin'
CamomileDir=CamomileRoot+'/Examples'
Vst3PluginFolder='/Library/Audio/Plug-Ins/VST3'
# print(os.listdir(DIR))

for PluginName in os.listdir(DIR):
    SourceCamomile=DIR+'/'+PluginName
    if os.path.isdir(SourceCamomile):

        # distutils.dir_util.copy_tree(SourceCamomle, CamomileDir+'/'+PluginName) 
        # print('cd '+CamomileRoot+' && ./camomile -f '+SourceCamomile+' -o '+Vst3PluginFolder+'/CamomileUtils'+' -v')
        os.system('cd '+CamomileRoot+' && ./camomile -f '+SourceCamomile+' -o '+Vst3PluginFolder+'/CamomileUtils'+' -v') 
        # os.system('cd '+CamomileRoot+' && ./camomile') 

        # shutil.rmtree(CamomileDir+'/'+PluginName)
        
        # print(CamomileRoot+'/builds/'+PluginName+'.vst3')

        # distutils.dir_util.copy_tree(CamomileRoot+'/builds/'+PluginName+'.vst3', Vst3PluginFolder+'/CamomileUtils/'+PluginName+'.vst3') 
        # shutil.rmtree(CamomileRoot+'/builds')

