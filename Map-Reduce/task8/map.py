#!/usr/bin/python
 
import sys
import string
import csv

# input comes from STDIN (stream data that goes to the program)

for line in csv.reader(sys.stdin):
	#entry = list(csv.reader([line], delimiter = ','))[0]
	#if len(entry) != 22:
	#	continue
 
	make  = line[20]
	color = line[19]
	if len(make) < 1:
		print('a' + ' ' + 'vehicle_make' + ' ' + 'NONE' + '\t' + str(1))
	else:
		print('a' + ' ' + 'vehicle_make' + ' ' + str(make) + '\t' + str(1))
	if len(color) < 1:
		print('b' + ' ' + 'vehicle_color' + ' ' + 'NONE' + '\t' + str(1))
	else:
		print('b' + ' ' + 'vehicle_color' + ' ' + str(color) + '\t' + str(1))

	
        
