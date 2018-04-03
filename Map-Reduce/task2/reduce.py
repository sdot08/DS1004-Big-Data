#!/usr/bin/python





import sys
import string

# input comes from STDIN (stream data that goes to the program)
current_key = None
num = 0.0
for line in sys.stdin:
	
	#Remove leading and trailing whitespace
	line = line.strip() 
	#Get key/value 
	key, value = line.split('\t',1)
	value = int(value)
	if key == current_key:
		num += value

	else:
		if current_key:
			print(current_key + '\t' + str(num))
		current_key = key
		num = 0
		num += int(value)
print(current_key + '\t' + str(num)) 
