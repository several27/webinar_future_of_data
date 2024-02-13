from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customers.config.ConfigStore import *
from customers.udfs.UDFs import *
from prophecy.utils import *
from customers.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers_raw = customers_raw(spark)
    df_reformat_customers_data = reformat_customers_data(spark, df_customers_raw)
    customers(spark, df_reformat_customers_data)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customers")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/customers", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/customers")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
