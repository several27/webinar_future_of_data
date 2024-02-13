from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customers_orders.config.ConfigStore import *
from customers_orders.udfs.UDFs import *

def customer_order_amount(spark: SparkSession, customers: DataFrame, orders: DataFrame, ) -> DataFrame:
    return customers\
        .alias("customers")\
        .join(orders.alias("orders"), (col("customers.customer_id") == col("orders.customer_id")), "inner")\
        .select(col("customers.customer_id").alias("CUSTOMER_ID"), col("customers.first_name").alias("FIRST_NAME"), col("customers.last_name").alias("LAST_NAME"), col("orders.amount").alias("AMOUNT"))
