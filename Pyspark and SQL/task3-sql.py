import sys
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark = SparkSession \
.builder \
.appName("task1-sql") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()

openv = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])

openv.createOrReplaceTempView("openv")

result = spark.sql("SELECT O.license_type, sum(O.amount_due) as sum_amount, avg(O.amount_due) as avg_amount FROM openv O GROUP BY license_type")
result.select(format_string('%s\t%.2f, %.2f',result.license_type,result.sum_amount,result.avg_amount)).write.save("task3-sql.out",format="text")

