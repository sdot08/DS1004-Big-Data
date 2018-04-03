#!/usr/bin/python





import sys
import string

# input comes from STDIN (stream data that goes to the program)
v_dict= {}
current_key = None
weekend_date = ['05', '06', '12', '13', '19', '20', '26', '27']
for line in sys.stdin:
	
	#Remove leading and trailing whitespace
	line = line.strip() 
	#Get key/value 
	key, value = line.split('\t',1)
	date_last2 = value[-2:]
	if key == current_key:
		if date_last2 in weekend_date:
			v_dict['weekend'] += 1
		else:
			v_dict['week'] += 1

	else:
		if current_key:
			print("{0}\t{1: .2f}, {2: .2f}".format(current_key, v_dict['weekend']/8.0, v_dict['week']/23.))
		current_key = key
		v_dict['weekend'] = 0
		v_dict['week'] = 0
		if date_last2 in weekend_date:
			v_dict['weekend'] += 1
		else:
			v_dict['week'] += 1
print("{0}\t{1: .2f}, {2: .2f}".format(current_key, v_dict['weekend']/8.0, v_dict['week']/23.))
