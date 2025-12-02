from pyspark.sql import SparkSession

spark = SparkSession.builder \
            .appName("DataCleaner") \
            .master("spark://spark-master:7077") \
            .config("spark.executor.memory", "1g") \
            .getOrCreate()

df = spark.read.csv("/data/raw/input.csv", header=True, inferSchema=True)

df_clean = df.dropna()
df_clean = df_clean.dropDuplicates()

df_clean.coalesce(1).write.mode("overwrite").csv("/data/clean/output.csv", header=True)

spark.stop()