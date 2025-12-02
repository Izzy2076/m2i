from pyspark.sql import SparkSession, functions as F, types as T
import re
import os

@F.udf(T.StringType())
def clean_text(s):
    if not s:
        return None
    return s.strip().capitalize()

@F.udf(T.StringType())
def clean_email(s):
    if not s:
        return None
    s = s.strip().lower()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return s if re.match(pattern, s) else None

@F.udf(T.DoubleType())
def clean_amount(amount, currency):
    if not amount:
        return None
    try:
        val = float(amount)
        if val <= 0:
            return None
        if currency and currency.strip().upper() == "USD":
            return round(val * 0.92, 2)
        return round(val, 2)
    except:
        return None

@F.udf(T.StringType())
def clean_currency(amount, currency):
    if not amount or float(amount) <= 0:
        return None
    return "EUR"

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[*]").getOrCreate()
        
    clients_df = spark.read.option("header", True).csv("data/clients.csv")
    commandes_df = spark.read.option("header", True).csv("data/commandes.csv")
    
    clients_clean = clients_df \
        .withColumn("nom", clean_text("nom")) \
        .withColumn("prenom", clean_text("prenom")) \
        .withColumn("email", clean_email("email")) \
        .withColumn("city", clean_text("city")) \
        .withColumn("country", clean_text("country")) \
        .withColumn("signup_date", F.to_date("signup_date")) \
        .withColumn("birthdate", F.to_date("birthdate")) \
        .withColumn("is_vip", F.when(F.lower(F.col("is_vip")) == "true", True).otherwise(False))
    
    commandes_clean = commandes_df \
        .withColumn("amount_clean", clean_amount("amount", "currency")) \
        .withColumn("currency_clean", clean_currency("amount", "currency")) \
        .withColumn("status", F.lower(F.trim("status"))) \
        .withColumn("payment_method", F.lower(F.trim("payment_method"))) \
        .withColumn("city_shipping", clean_text("city_shipping")) \
        .withColumn("country_shipping", clean_text("country_shipping")) \
        .withColumn("order_date", F.to_timestamp("order_date")) \
        .select("order_id", "client_id", "order_date", "status", 
                F.col("amount_clean").alias("amount"), 
                F.col("currency_clean").alias("currency"),
                "payment_method", "items_count", "coupon_code", 
                "city_shipping", "country_shipping")
    
    os.makedirs("data", exist_ok=True)
    
    clients_pandas = clients_clean.toPandas()
    commandes_pandas = commandes_clean.toPandas()
    
    clients_pandas.to_csv("data/clients_clean.csv", index=False)
    commandes_pandas.to_csv("data/commandes_clean.csv", index=False)
    
    spark.stop()