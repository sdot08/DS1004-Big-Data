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
#result_0 = spark.sql("SELECT P.plate_id, P.registration_state, count(P.summons_number) AS Pcount FROM parking P GROUP BY P.plate_id, P.registration_state having max(Pcount)")
result_0 = spark.sql("SELECT P.plate_id, P.registration_state, count(P.summons_number) AS Pcount FROM parking P GROUP BY P.plate_id, P.registration_state")
result_0.createOrReplaceTempView("result_0")
result_1 = spark.sql("SELECT plate_id, registration_state, Pcount AS Pmax FROM result_0 WHERE Pcount in (SELECT max(Pcount) FROM result_0)")
result_1.select(format_string('%s, %s\t%d',result_1.plate_id, result_1.registration_state, result_1.Pmax)).write.save("task5-sql.out",format="text")
