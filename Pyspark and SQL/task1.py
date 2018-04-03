import sys
from csv import reader
from pyspark import SparkContext
sc = SparkContext('local', 'task1')
park = sc.textFile(sys.argv[1], 1)
park = park.mapPartitions(lambda x: reader(x))
park_0 = park.map(lambda x:(x[0], 1))
open = sc.textFile(sys.argv[2], 1)
open = open.mapPartitions(lambda x: reader(x))
open_0 = open.map(lambda x:(x[0], 1))

diff_0 = park_0.subtract(open_0)


park_12614 = park.map(lambda x: (x[0], (x[14], x[6], x[2], x[1])))
result = diff_0.join(park_12614).persist()
#result.take(1)

#result = result.map(lambda x : (x[0],x[1][1]))
result = result.map(lambda x: (str(x[0]) + '\t' + str(x[1][1][0]) + ', ' + str(x[1][1][1]) + ', ' + str(x[1][1][2]) + ', ' + str(x[1][1][3])))
result.saveAsTextFile("task1.out")
