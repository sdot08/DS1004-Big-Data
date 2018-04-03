import sys
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
spark = SparkSession \
.builder \
.appName("task1-sql") \
.config("spark.some.config.option", "some-value") \
.getOrCreate()

parking = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])
openv = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[2])

parking.createOrReplaceTempView("parking")
openv.createOrReplaceTempView("openv")

result = spark.sql("SELECT P.summons_number, P.plate_id, P.violation_precinct, P.violation_code, P.issue_date FROM parking P LEFT JOIN openv O ON \
	P.summons_number = O.summons_number WHERE O.amount_due IS NULL")
result.select(format_string('%d\t%s, %d, %d, %s',result.summons_number,result.plate_id,result.violation_precinct,result.violation_code,date_format(result.issue_date,'yyyy-MM-dd'))).write.save("task1-sql.out",format="text")


