from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customers_orders.config.ConfigStore import *
from customers_orders.udfs.UDFs import *

def limit_50_customer_details(spark: SparkSession, limit_50: DataFrame) -> DataFrame:
    return limit_50.select(
        col("CUSTOMER_ID"), 
        concat(col("FIRST_NAME"), lit(" "), col("LAST_NAME")).alias("FULL_NAME"), 
        col("TOTAL_SPENT")
    )
