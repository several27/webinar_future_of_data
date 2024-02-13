from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customers_orders.config.ConfigStore import *
from customers_orders.udfs.UDFs import *

def total_spent_by_customer(spark: SparkSession, customer_order_amount: DataFrame) -> DataFrame:
    df1 = customer_order_amount.groupBy(col("CUSTOMER_ID"), col("FIRST_NAME"), col("LAST_NAME"))

    return df1.agg(sum(col("amount")).alias("TOTAL_SPENT"))
