#!/usr/bin/python
 
import sys
import string
import csv


# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
	entry = list(csv.reader([line], delimiter = ','))[0] 
	if len(entry) != 22:
		continue
 
	date  = entry[1]
	if len(date) < 1:
		continue
	code = entry[2]
	if len(code) < 1:
		continue
	print(str(code) + '\t' + str(date))

	
        
