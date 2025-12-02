from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from pyspark.sql import functions as F

def normalize_product_names(df):
    return df.withColumn("nom", 
                        F.initcap(F.trim(F.col("nom"))))


def normalize_categories(df):
    return df.withColumn("categorie", 
                        F.lower(F.trim(F.col("categorie"))))


def convert_price_to_float(df):
    return df.withColumn("prix", 
                        F.col("prix").cast(DoubleType()))


def fix_negative_stock(df):
    return df.withColumn("stock", 
                        F.col("stock").cast(IntegerType())) \
             .withColumn("stock",
                        F.when(F.col("stock") < 0, 0)
                         .otherwise(F.col("stock")))


def remove_products_without_name(df):
    return df.filter(
        (F.col("nom").isNotNull()) & 
        (F.trim(F.col("nom")) != "")
    )


def clean_products_pipeline(df):
    return (df
            .transform(normalize_product_names)
            .transform(normalize_categories)
            .transform(convert_price_to_float)
            .transform(fix_negative_stock)
            .transform(remove_products_without_name))
