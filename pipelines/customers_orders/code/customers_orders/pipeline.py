from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customers_orders.config.ConfigStore import *
from customers_orders.udfs.UDFs import *
from prophecy.utils import *
from customers_orders.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_customers = customers(spark)
    df_customer_order_amount = customer_order_amount(spark, df_customers, df_orders)
    df_total_spent_by_customer = total_spent_by_customer(spark, df_customer_order_amount)
    df_by_total_spent_desc_nulls_first = by_total_spent_desc_nulls_first(spark, df_total_spent_by_customer)
    df_limit_50 = limit_50(spark, df_by_total_spent_desc_nulls_first)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customers_orders")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/customers_orders", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/customers_orders")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
