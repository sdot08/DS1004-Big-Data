#!/usr/bin/python





import sys
import string

# input comes from STDIN (stream data that goes to the program)
num_due = 0.0
current_key = None
num = 0.0
for line in sys.stdin:
	
	#Remove leading and trailing whitespace
	line = line.strip() 
	#Get key/value 
	key, value = line.split('\t',1)
	value = float(value)
	if key == current_key:
		num_due += value
		num  += 1.0

	else:
		if current_key:
			print("{0}\t{1: .2f}, {2: .2f}".format(current_key, num_due, num_due/num))
		current_key = key
		num_due = 0
		num = 0
		num_due += value
		num += 1
print("{0}\t{1: .2f}, {2: .2f}".format(current_key, num_due, num_due/num))
