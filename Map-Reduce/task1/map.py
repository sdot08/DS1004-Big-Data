#!/usr/bin/python
 
import sys
import string
import csv

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
	entry = list(csv.reader([line],delimiter = ','))[0]
	#Remove 1leading and trailing whitespace
	leng = len(entry)
#	if len(entry[1]) < 1:
#		continue 
	if leng != 22 and leng != 18:
		continue
	if leng == 18:
		print(str(entry[0]) + '\t' + str(1))
	else:
		print(str(entry[0]) + '\t' + str(entry[14]) + ' ' + str(entry[6]) + ' ' + str(entry[2]) + ' ' + str(entry[1]))

	
        
