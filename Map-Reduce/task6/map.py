#!/usr/bin/python
 
import sys
import string
import csv

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
	entry = list(csv.reader([line], delimiter = ','))[0] 
	if len(entry) != 22:
		continue
 
	plate_id  = entry[14]
	state = entry[16]
	if len(plate_id) < 1:
		continue
	if len(state) < 1 :
		continue
	value =  1	
	print(str(plate_id) + ', ' + str(state) + '\t' + str(value))

	
        
