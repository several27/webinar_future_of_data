from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customers_orders.config.ConfigStore import *
from customers_orders.udfs.UDFs import *

def orders(spark: SparkSession) -> DataFrame:
    return spark.read.table("`main`.`default`.`sko_orders`")
