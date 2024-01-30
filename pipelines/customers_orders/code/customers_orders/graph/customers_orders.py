from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customers_orders.config.ConfigStore import *
from customers_orders.udfs.UDFs import *

def customers_orders(spark: SparkSession, limit_50_customer_details: DataFrame):
    limit_50_customer_details.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable("`main`.`default`.`webinar_customers_orders`")
