#!/usr/bin/python





import sys
import string

# input comes from STDIN (stream data that goes to the program)
v_dict= {}
current_key = None
num = 0
for line in sys.stdin:
	
	#Remove leading and trailing whitespace
	line = line.strip() 
	#Get key/value 
	key, value = line.split('\t',1)
	key_array = key.split(' ',2)
	column = key_array[1]
	term = key_array[2]
	if key == current_key:
		num  += 1

	else:
		if current_key:
			key_array = current_key.split(' ',2)
			column_ = key_array[1]
			term_ = key_array[2]
			print(column_  + '\t' + term_ +', ' +str(num))
		current_key = key
		num = 0
		num += 1
print(column  + '\t' + term +', ' +str(num))
