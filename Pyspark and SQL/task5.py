import sys
from csv import reader
from pyspark import SparkContext


sc = SparkContext('local', 'task5')
park = sc.textFile(sys.argv[1], 1)
#park = sc.textFile("/user/ecc290/HW1data/parking-violations.csv", 1)

park = park.mapPartitions(lambda x: reader(x))
park_0 = park.map(lambda x: ((x[14], x[16]),1))

park_1 = park_0.reduceByKey(lambda x, y: x + y)

park_2 = park_1.map(lambda x : (x[1], x[0]))
park_3 = park_2.sortByKey(False)
park_4 = sc.parallelize(park_3.take(1))
result = park_4.map(lambda x: (str(x[1][0]) + ', ' + str(x[1][1]) +'\t' + str(x[0])))
result.saveAsTextFile("task5.out")
