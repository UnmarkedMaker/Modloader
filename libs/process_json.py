import json

def load_data(fname):
	with open(fname) as f:
		data = json.load(f)
	return data

def get_value(jsondata, item):
	return jsondata[item]

def change_value(jsondata, item, value):
	try:
		jsondata[item] = value
		return True #Success, probably this feature will be unused
	except Exception as e:
		print('Error:' , e)

def to_json(dict):
	return json.dumps(dict)
