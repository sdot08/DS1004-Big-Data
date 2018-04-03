import sys
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark = SparkSession \
.builder \
.appName("task7-sql") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()

parking = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])
#parking = spark.read.format('csv').options(header='true',inferschema='true').load('/user/ecc290/HW1data/parking-violations-header.csv')

parking.createOrReplaceTempView("parking")

vc = spark.sql("SELECT DISTINCT P.violation_code FROM parking P")
vc.createOrReplaceTempView("vc")
weekend = spark.sql("SELECT P.violation_code, count(P.violation_code)/8 as weekend_count FROM parking P WHERE P.issue_date like '%2016-03-05%' OR P.issue_date like '%2016-03-06%' OR P.issue_date like '%2016-03-12%' OR \
	P.issue_date like '%2016-03-13%' OR P.issue_date like '%2016-03-19%' OR P.issue_date like '%2016-03-20%' OR P.issue_date like '%2016-03-26%' OR P.issue_date like '%2016-03-27%' GROUP BY P.violation_code  ")
weekend.createOrReplaceTempView("weekend")
weekday = spark.sql("SELECT P.violation_code, count(P.violation_code)/23 as weekday_count FROM parking P WHERE NOT (P.issue_date like '%2016-03-05%' OR \
	P.issue_date like '%2016-03-06%' OR P.issue_date like '%2016-03-12%' OR \
	P.issue_date like '%2016-03-13%' OR P.issue_date like '%2016-03-19%' OR P.issue_date like '%2016-03-20%' \
	OR P.issue_date like '%2016-03-26%' OR P.issue_date like '%2016-03-27%') GROUP BY P.violation_code  ")
weekday.createOrReplaceTempView("weekday")

result = spark.sql("SELECT vc.violation_code, COALESCE(weekend_count, 0) as weekend_count_, COALESCE(weekday_count, 0) as weekday_count_ FROM vc LEFT JOIN weekend on vc.violation_code = weekend.violation_code \
	LEFT JOIN weekday on vc.violation_code = weekday.violation_code")
#result = spark.sql("SELECT vc.violation_code, IIF(ISNULL(weekend_count), 0, weekend_count), IIF(ISNULL(weekday_count), 0, weekday_count) FROM vc LEFT JOIN weekend on vc.violation_code = weekend.violation_code \
#	LEFT JOIN weekday on vc.violation_code = weekday.violation_code")

#result = spark.sql("SELECT vc.violation_code, weekend_count, weekday_count FROM vc LEFT JOIN weekend on vc.violation_code = weekend.violation_code \
#	LEFT JOIN weekday on vc.violation_code = weekday.violation_code")


#result = spark.sql("SELECT violation_code, weekend_count, weekday_count FROM result_0 ")
#SELECT ISNULL(myColumn, 0 ) FROM myTable
result.select(format_string('%s\t%.2f, %.2f',result.violation_code,result.weekend_count_,result.weekday_count_)).write.save("task7-sql.out",format="text")
