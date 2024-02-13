from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from orders.config.ConfigStore import *
from orders.udfs.UDFs import *

def orders(spark: SparkSession, reformat_order_data: DataFrame):
    reformat_order_data.write.format("delta").mode("overwrite").saveAsTable("`main`.`default`.`sko_orders`")
