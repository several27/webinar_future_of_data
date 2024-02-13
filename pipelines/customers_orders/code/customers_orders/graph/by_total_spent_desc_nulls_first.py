from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customers_orders.config.ConfigStore import *
from customers_orders.udfs.UDFs import *

def by_total_spent_desc_nulls_first(spark: SparkSession, total_spent_by_customer: DataFrame) -> DataFrame:
    return total_spent_by_customer.orderBy(col("TOTAL_SPENT").desc())
