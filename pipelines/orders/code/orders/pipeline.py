from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from orders.config.ConfigStore import *
from orders.udfs.UDFs import *
from prophecy.utils import *
from orders.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders_raw = orders_raw(spark)
    df_reformatted_orders = reformatted_orders(spark, df_orders_raw)
    orders(spark, df_reformatted_orders)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/orders")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/orders", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/orders")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
