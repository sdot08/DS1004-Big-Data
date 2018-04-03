#!/usr/bin/python
# map function for matrix multiply
#Input file assumed to have lines of the form "A,i,j,x", where i is the row index, j is the column index, and x is the value in row i, column j of A. Entries of A are followed by lines of the form "B,i,j,x" for the matrix B. 
#It is assumed that the matrix dimensions are such that the product A*B exists. 

#Input arguments:
#m should be set to the number of rows in A, p should be set to the number of columns in B.
 
import sys
import string
import csv

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
	#Remove leading and trailing whitespace
	entry  = list(csv.reader([line], delimiter = ','))[0]
	if len(entry) != 18:
		continue    

	key = entry[2]
	value = entry[12]
	if len(key) < 2:
		continue	
	print(str(key) + '\t' + str(value))

	
        
