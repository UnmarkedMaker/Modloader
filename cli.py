import libs.load_mods as l
import libs.debug as debug

def find_mod(name):
    for i in range(len(l.mods)):
        debug.debug(__name__, 'find_mod()', 'Found a module, name:' + str(l.mods[i].jsondata['modName']), 'blue')
        if(str(l.mods[i].jsondata['modName']) == name):
            debug.debug(__name__, 'find_mod()', 'Found a module with the requested name.', 'green')
            return l.mods[i]
    return False

def main():
    l.init()
    debug.newline(times=2)
    debug.debug(__name__, 'main()', 'init() done!', 'green')
    debug.newline(times=2)

    print('listing mods:')
    l.listMods()
    print('Len of mods:', len(l.mods))
    #debug.debug(__name__, 'main()', 'searching for \'checkloading\' with find_mods()', 'magenta')
    #foundMod = find_mod('checkloading')
    print('The end')
    while True:
        command = input('>')
        if(command == 'exit' or command == 'quit'): return #There are two types of people: Who type 'exit' and who type 'quit'
        if(command != ''):
            # If the command is nothing, don't do anything with it
            requestedModule = str(command.split(' ')[0])
            arguments = command.split(' ')[1:]

            debug.debug(__name__, 'main()', 'Requested module: "' + requestedModule + '"', 'blue')
            debug.debug(__name__, 'main()', 'Arguments: ' + str(arguments), 'blue')

            foundMod = find_mod(requestedModule)
            if(not foundMod):
                #the module was not found (find_mod() returns False if it founds nothing)
                print('Error, "' + requestedModule + '" is not a module')
                continue
            debug.debug(__name__, 'main()', 'The module found is: ' + str(foundMod), 'green')
            importedModule = l.importExtra(foundMod)
            debug.newline()
            debug.debug(__name__, 'main()', 'Requested module successfully imported', 'green')
            l.runMod(importedModule, arguments)
if __name__ == "__main__":
    main()