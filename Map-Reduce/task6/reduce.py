#!/usr/bin/python





import sys
import string
import heapq
# input comes from STDIN (stream data that goes to the program)
heap = []
heap2 = []
heapq.heapify(heap)
udict = {}
for line in sys.stdin:
	
	#Remove leading and trailing whitespace
	line = line.strip() 
	#Get key/value 
	key, value = line.split('\t',1)
	if key in udict:
		udict[key] += int(value)
	else:
		udict[key] = int(value)
for key in udict:
	num = udict[key]
	heapq.heappush(heap, (num, key))
	heapq.heappush(heap2, (-num, key))
	if len(heap) > 20:
		heapq.heappop(heap)
heap = [(-j,k) for (j,k) in heap]
heapq.heapify(heap)
while len(heap) != 0:
	item = heapq.heappop(heap)			
	print(item[1] + '\t' + str(-item[0]))




