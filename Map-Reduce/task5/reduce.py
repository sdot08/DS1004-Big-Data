#!/usr/bin/python





import sys
import string

# input comes from STDIN (stream data that goes to the program)
violation_dict = {}
for line in sys.stdin:
	
	#Remove leading and trailing whitespace
	line = line.strip() 
	#Get key/value 
	key, value = line.split('\t',1)

	if key in violation_dict:
		violation_dict[key] += int(value)

	else:
		violation_dict[key] = int(value)
max_num = 0
key_output = []
num_output = []
for key in violation_dict:
	val = violation_dict[key]
	if val > max_num:
		key_output = []
		key_output.append(key)
		num_output = []
		num_output.append(val)
		max_num = val
	elif val == max_num:
		key_output.append(key)
		num_output.append(val)


		
for key in key_output:			
	print(str(key) + '\t' + str(violation_dict[key]))





