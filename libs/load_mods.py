import os.path
import importlib

class Modstruct:
	"""Class for storing information about a module, required"""
	def __init__(self, jsondata, moddir):
		self.jsondata = jsondata
		self.moddir = moddir

demo_modstruct = Modstruct('{}', 'mods')

scriptDir = os.path.dirname(os.path.abspath(__file__))
print('Scriptdir = ', scriptDir)
import sys
sys.path.append(scriptDir)
import process_json as j
import debug
mods = []
loaded_mods = []

def import_mod(path, modpath, filename,):
	debug.debug(__name__, 'rec_dir()', 'Found a module file, filename : ' + filename + '. Importing it...', 'green')

	data = j.load_data(path + '/' + filename)
	mod_dir = modpath + '.'.join(filename.split('.')[0:-1])
	mod = Modstruct(data, mod_dir)

	if (j.get_value(data, 'list') == True): #if it's enabled (For testing periods, you can disable modules)
		mods.append(mod)
		debug.debug(__name__, 'rec_dir()', 'DONE', 'green')
	else:
		debug.debug(__name__, 'rec_dir()', 'not loading '+ j.get_value(data, 'modName') +' because it\'s disabled.', 'yellow')

def rec_dir(path, modpath):
	"""Discovering and adding modules"""
	debug.debug(__name__, 'rec_dir()', ' rec_dir was called', 'magenta')

	for file in os.listdir(path):
		debug.debug(__name__, 'rec_dir()', 'found a file, name : "' + file + '"', 'blue')
		debug.debug(__name__, 'rec_dir()', 'os.path.isdir() for the file is : ' + str(os.path.isdir(path+'/'+file)), 'blue')
		if(os.path.isdir(path+'/'+file)):
			debug.debug(__name__, 'rec_dir()', 'found a directory name : ' + path+'/'+file, 'magenta')
			newmod = rec_dir(path+'/'+file, modpath+file+'.')
			if(type(newmod) == type(demo_modstruct)):
				mods.append(newmod)
		if (file[-5:] == '.json' and os.path.isfile(path + '/' + file[:-5]+'.py')):
			import_mod(path, modpath, file)
		else:
			debug.debug(__name__, 'rec_dir()', 'file not a module, file\'s name : ' + file, 'yellow')
	return mods

def init():
	mod_dir = scriptDir + '/../' + j.get_value(j.load_data(scriptDir + '/../config.json'), 'mods-dir')
	global mods
	mods = rec_dir(mod_dir, 'mods.')


def listMods():
	#This function should print the names of all loaded modules.
	for i in mods:
		debug.debug(__name__, 'listMods()', 'found a module, its name : ' + j.get_value(i.jsondata, 'modName'), 'green')
		debug.debug(__name__, 'listMods()', 'module data : ' + str(i.jsondata), 'cyan')
		debug.debug(__name__, 'listMods()', 'module path : ' + i.moddir, 'cyan')
		
def importExtra(mod):
	#mod is the type of 'Modstruct'
	importedMod = importlib.import_module(mod.moddir)
	loaded_mods.append(importedMod)
	return importedMod
def runMod(mod, args):
	mod.Main.run(None, args)
def importAndRun(mod, args):
        name = importExtra(mod)
	runMod(name, args)
