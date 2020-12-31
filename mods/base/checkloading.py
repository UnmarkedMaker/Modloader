class Main:
	def run(self, args=[]):
		import libs.debug
		libs.debug.debug(__name__, 'Main.run()', 'Successful execution', 'green')
		print('__name__:', __name__)
		if(args != []): # If there is no arguments, args will be [] see cli.py line 29-30
			import cli
			import libs.load_mods
			for i in args:
				if(i == ''): continue # too many spaces
				currentModDir = cli.find_mod(i) #finding the mod.
				if(currentModDir):
					#cli.findmod() return False if it founds nothing
					try:
						modName = libs.load_mods.importExtra(currentModDir)
						result = modName.Main.check(None)
					except:
						result = False
					if(result):
						print('"' + currentModDir.moddir + '" was successfuly imported and ran')
					else:
						print(currentModDir.moddir + ' Failed to import/run')
				else:
					print('Failed to find module named "' + i + '", try checking your spelling')

	def check(self):
		return True