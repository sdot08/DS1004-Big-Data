#!/usr/bin/python
 
import sys
import string
import csv

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
	entry = list(csv.reader([line], delimiter = ','))[0] 
	key = entry[16]
	key = key.strip()
	if len(key) < 1:
		continue
	value =  1
	if key == 'NY':	
		print(str(key) + '\t' + str(value))
	else:
		print('Other' + '\t' + str(value))
	
        
