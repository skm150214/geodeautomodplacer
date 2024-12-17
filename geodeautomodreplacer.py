import os
import shutil

SET_YOUR_OWN_GD_MODS_DIR =  "C:\Program Files (x86)\Steam\steamapps\common\Geometry Dash\geode\mods\ " #default #change for your own dir
SET_YOUR_MOD_DIR = "C:\Users\User123\example_mod\build\ " #replace for your own mod dir and build
SET_YOUR_GD_MOD_NAME = "example_mod_name.geode" #replace for your own mod name
os.remove(SET_YOUR_OWN_GD_MODS_DIR + SET_YOUR_GD_MOD_NAME)
shutil.copy(SET_YOUR_MOD_DIR + SET_YOUR_GD_MOD_NAME, SET_YOUR_OWN_GD_MODS_DIR + SET_YOUR_GD_MOD_NAME)
