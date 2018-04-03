#!/usr/bin/python





import sys
import string
num = 0
# input comes from STDIN (stream data that goes to the program)
current_key = None
for line in sys.stdin:
	
	#Remove leading and trailing whitespace
	line = line.strip() 
	#Get key/value 
	key, value = line.split('\t',1)
	value = int(value)
	if current_key == key:
		num += value
	else:
		if current_key:
			if current_key == 'NY':	
				print('NY' +'\t' + str(num))
			else:
				print('Other' + '\t' + str(num))		
		current_key = key
		num = 0
		num += value
if current_key == 'NY':
	print('NY' +'\t' + str(num))   
else:
	print('Other' + '\t' + str(num))
