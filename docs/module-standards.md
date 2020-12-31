## How a standard module looks:

modulename.json:
```json
{
    "modName" : "module's name",
    "help"    : "Description and help about the module",
    "usage"   : "<usage of the module goes here>",
    "region"  : "what region it registers",
    "list"    : true
}
```
modulename.py
```python
class Main:
	def run(self, args=[]):
		print('Main function that gets called when the module\'s name is typed in the console')
	def check(self):
		return True
```

### What are the parts?

* modName    -> The name of the module
* help       -> Some quick help for the mod's usage in the default command line
* usage      -> Information on how to use this mod in the default command line
* region     -> Assigns a region to the mod, helps the default command line to categorize the mod
* list       -> *True* or *False*, whether to load the module on the modloader's init.
* Main       -> the main class **must** have and do **not** change its name.
* Main.run   -> the run function, the framework's default command line will run the mod with this
* Main.check -> a function that will **always** return *True*, indicating that the mod is working
