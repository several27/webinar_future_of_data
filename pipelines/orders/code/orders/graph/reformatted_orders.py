from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from orders.config.ConfigStore import *
from orders.udfs.UDFs import *

def reformatted_orders(spark: SparkSession, orders: DataFrame) -> DataFrame:
    return orders.select(
        col("order_id"), 
        col("customer_id"), 
        col("order_status"), 
        col("order_category"), 
        col("order_date"), 
        floor(col("amount")).alias("amount")
    )
