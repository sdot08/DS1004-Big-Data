import sys
from csv import reader
from pyspark import SparkContext


sc = SparkContext('local', 'task7')

weekend_date = ['05', '06', '12', '13', '19', '20', '26', '27']

def is_weekend(x):
	if x[-2:] in weekend_date:
		return 1
	else:
		return 0

def is_not_weekend(x):
	if x[-2:] in weekend_date:
		return 0
	else:
		return 1

parking = sc.textFile(sys.argv[1], 1)
parking = sc.textFile("/user/ecc290/HW1data/parking-violations.csv", 1)

parking = parking.mapPartitions(lambda x: reader(x))
parking_0 = parking.map(lambda x:(x[2], x[1]))
parking_weekend_count = parking_0.map(lambda x: (x[0], is_weekend(x[1])))
parking_weekday_count = parking_0.map(lambda x: (x[0], is_not_weekend(x[1])))



parking_weekend_count  = parking_weekend_count.reduceByKey(lambda x, y: x + y)
parking_weekday_count  = parking_weekday_count.reduceByKey(lambda x, y: x + y)
parking_2 = parking_weekend_count.join(parking_weekday_count)

result = parking_2.map(lambda x: '%s\t%.2f, %.2f' % (x[0], x[1][0] / 8.0, x[1][1] / 23.0))

result.saveAsTextFile("task7.out")
