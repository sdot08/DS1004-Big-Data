import sys
from csv import reader
from pyspark import SparkContext
sc = SparkContext('local', 'task4')
park = sc.textFile(sys.argv[1], 1)
park = park.mapPartitions(lambda x: reader(x))
park_0 = park.map(lambda x: x[16])
park_1 = park_0.filter(lambda x: x == 'NY')
park_2 = park_0.filter(lambda x: x != 'NY')

park_1 = park_1.map(lambda x: (x, 1))
park_2 = park_2.map(lambda x: ('Other', 1))

park_1 = park_1.reduceByKey(lambda x, y: x + y)
park_2 = park_2.reduceByKey(lambda x, y: x + y)

park_1 = park_1.map(lambda x: (str(x[0]) + '\t' + str(x[1])))
park_2 = park_2.map(lambda x: (str(x[0]) + '\t' + str(x[1])))


result = park_1.union(park_2)

result.saveAsTextFile("task4.out")
