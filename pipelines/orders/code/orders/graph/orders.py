from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from orders.config.ConfigStore import *
from orders.udfs.UDFs import *

def orders(spark: SparkSession, reformatted_orders: DataFrame):
    reformatted_orders.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable("`main`.`default`.`webinar_customers_customers`")
