class Main:
    def run(self, args):
        if(args != []): # If there is no arguments, args will be [] see cli.py line 29-30
            import cli
            import libs.load_mods
            for i in args:
                if(i == ''): continue # too many spaces
                currentModDir = cli.find_mod(i) #finding the mod.
                if(currentModDir):
                    #cli.findmod() return False if it founds nothing
                    data = currentModDir.jsondata
                    print('Name: ' + currentModDir.moddir)
                    print('    Help: ' + data['help'])
                    print('    Usage: ' + data['usage'])
                    print('    Region: ' + data['region'])
                    print('    Is it listed: ' + str(data['list'])) # str() needed because 'list' value is bool
                else:
                    print('Failed to find module named "' + i + '", try checking your spelling')
        else:
            print('No argument supplied.')
    def check(self):
        return True