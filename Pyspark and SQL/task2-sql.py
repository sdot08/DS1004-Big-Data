import sys
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark = SparkSession \
.builder \
.appName("task2-sql") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()

parking = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])

parking.createOrReplaceTempView("parking")

result = spark.sql("SELECT P.violation_code, count(P.violation_code) AS count_v FROM parking P GROUP BY P.violation_code")
result.select(format_string('%s\t%d',result.violation_code, result.count_v)).write.save("task2-sql.out",format="text")

