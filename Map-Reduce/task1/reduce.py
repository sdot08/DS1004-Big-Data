#!/usr/bin/python





import sys
import string

# input comes from STDIN (stream data that goes to the program)
current_key = None
num = 0
flag = 0
value_array = []
value_array_pre = []
for line in sys.stdin:
	
	#Remove leading and trailing whitespace
	line = line.strip() 
	#Get key/value 
	key, value = line.split('\t',1)
	if key == current_key:
		if len(value) > 1:
			value_array = value.split()
		else:
			flag = 1		
		value_array_pre = value_array
	else:
		if current_key:
			if flag == 0 and len(value_array_pre) > 1:
				print(current_key  + '\t' + str(value_array_pre[0]) + ', ' +str(value_array_pre[1]) + ', ' + str(value_array_pre[2]) + ', ' + str(value_array_pre[3]))
		current_key = key
		flag = 0
		value_array = []
		value_array_pre = []
		if len(value) > 1:
			value_array = value.split()
		else:
			flag = 1
		value_array_pre = value_array
if flag == 0 and len(value_array_pre) > 1:
	print(current_key  + '\t' + str(value_array_pre[0]) + ', ' +str(value_array_pre[1]) + ', ' + str(value_array_pre[2]) + ', ' + str(value_array_pre[3]))
