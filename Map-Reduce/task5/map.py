#!/usr/bin/python
 
import sys
import string


# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
	#Remove leading and trailing whitespace
	line = line.strip()
	entry = line.split(",")
	if len(entry) != 22:
		continue
 
	plate_id  = entry[14]
	state = entry[16]
	if len(plate_id) < 1 or plate_id == 'N/A':
		continue
	if len(state) < 1:
		continue
	value =  1	
	print(str(plate_id) + ', ' + str(state) + '\t' + str(value))

	
        
