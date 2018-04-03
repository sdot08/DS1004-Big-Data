import sys
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark = SparkSession \
.builder \
.appName("task4-sql") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()

parking = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])

parking.createOrReplaceTempView("parking")
result_0 = spark.sql("SELECT P.registration_state, count(P.registration_state) AS count_0 FROM parking P GROUP BY P.registration_state")
result_0.createOrReplaceTempView("result_0")
result_1 = spark.sql("SELECT 'Other' AS registration_state, sum(count_0) AS sum_other FROM result_0 WHERE registration_state not like '%NY%' ")
result_1.createOrReplaceTempView("result_1")
result_2 = spark.sql("SELECT registration_state, count_0 FROM result_0 WHERE registration_state like '%NY%' \
	UNION SELECT registration_state, sum_other AS count_0 FROM result_1")

result_2.select(format_string('%s\t%d',result_2.registration_state, result_2.count_0)).write.save("task4-sql.out",format="text")
