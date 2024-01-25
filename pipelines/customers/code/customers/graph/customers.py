from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customers.config.ConfigStore import *
from customers.udfs.UDFs import *

def customers(spark: SparkSession, reformat_customers_data: DataFrame):
    reformat_customers_data.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable("`main`.`default`.`webinar_customers_silver`")
