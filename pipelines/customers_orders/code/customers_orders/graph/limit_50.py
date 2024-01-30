from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customers_orders.config.ConfigStore import *
from customers_orders.udfs.UDFs import *

def limit_50(spark: SparkSession, by_total_spent_desc_nulls_first: DataFrame) -> DataFrame:
    return by_total_spent_desc_nulls_first.limit(50)
