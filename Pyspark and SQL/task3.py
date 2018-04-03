import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext('local', 'task3')
open = sc.textFile(sys.argv[1], 1)
open = open.mapPartitions(lambda x: reader(x))
open_0 = open.map(lambda x:(x[2], float(x[12])))
open_1 = open.map(lambda x:(x[2],  1))
open_0 = open_0.reduceByKey(lambda x, y: x + y)
open_1 = open_1.reduceByKey(lambda x, y: x + y)
open_2 = open_0.join(open_1)
result = open_2.map(lambda x: '%s\t%.2f, %.2f' % (x[0], x[1][0], x[1][0] / x[1][1]))

result.saveAsTextFile("task3.out")
