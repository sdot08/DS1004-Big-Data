import sys
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark = SparkSession \
.builder \
.appName("task5-sql") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()

parking = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])

parking.createOrReplaceTempView("parking")
result_0 = spark.sql("SELECT P.plate_id, P.registration_state, count(P.summons_number) AS Pcount FROM parking P GROUP BY P.plate_id, P.registration_state")
result_0.createOrReplaceTempView("result_0")
result_1 = spark.sql("SELECT plate_id, registration_state, Pcount FROM result_0 ORDER BY Pcount DESC, plate_id ASC LIMIT 20")


result_1.select(format_string('%s, %s\t%d',result_1.plate_id, result_1.registration_state, result_1.Pcount)).write.save("task6-sql.out",format="text")
