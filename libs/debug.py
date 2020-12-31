#############################
# ANSI color codes
#
# Black   : \u001b[30m
# Red     : \u001b[31m
# Green   : \u001b[32m
# Yellow  : \u001b[33m
# Blue    : \u001b[34m
# Magenta : \u001b[35m
# Cyan    : \u001b[36m
# White   : \u001b[37m
#############################


#############################
# Debug coloring:
#
# Red     : Error
# Yellow  : Warning
# Blue    : info
# Cyan    : Valuable info
# Green   : Success
# Magenta : Debug info
#############################

import process_json as pj

def get_codebycolor(colorcode, color):
	if(color):
		switcher = {
			'black'   : '\u001b[30m',
			'red'     : '\u001b[31m',
			'green'   : '\u001b[32m',
			'yellow'  : '\u001b[33m',
			'blue'    : '\u001b[34m',
			'magenta' : '\u001b[35m',
			'cyan'    : '\u001b[36m',
			'white'   : '\u001b[37m',
			'reset'   : '\u001b[0m'
		}
		return switcher.get(colorcode, 'Invalid color')
	return '' #the fuction was asked not to color.
def newline(times=1):
	if(not pj.load_data('config.json')['debug']): #MAGIC to determine if it's debuging is enabled in 'config.json'	
		return
	for _ in range(times):
		print()
def debug(filename, function, text, colorcode):
	if(not pj.load_data('config.json')['debug']): #MAGIC to determine if it's debuging is enabled in 'config.json'
		return
	color = pj.load_data('config.json')['color']
	if(filename == '' or filename == ' '):filename = 'unspecified file'
	if(function == '' or function == ' '):function = 'unspecified function'
	if(get_codebycolor(colorcode, color) != 'Invalid color'): # If the suplied color is a valid color and not an ANSI code
		colorcode = get_codebycolor(colorcode, color)
	print(colorcode + ' DEBUG : ' + function + ' in ' + filename + ' : ' + text + '\u001b[0m') # '\u001b[0m' is resetting the color
	
