from pyspark.sql import SparkSession, functions as F, types as T

@F.udf(T.StringType())
def clean_city(s):
  if not s:
    return None
  return s.strip().capitalize() # " PaRis " => "Paris"

@F.udf(T.DoubleType())
def clean_price(s):
  if not s:
    return None
  s = str(s).replace(",", ".")
  try:
    val = float(s)
    return val if val >= 0 else None
  except:
    return None
  
if __name__ == "__main__":
  spark = SparkSession.builder.master("local[*]").getOrCreate()
  
  # PERMISSIVE (par défaut) : Les lignes invalides sont gardées, les colones impossible à parser deviennent null
  # DROPMALFORMED : Les lignes invalides sont supprimées
  # FAILFAST : L'exécution stoppe immédiatement dès la détection d'une ligne invalide
  df = spark.read.option("header", True).option("sep", ";").option("mode", "DROPMALFORMED").csv("data/data.csv")
  
  df_clean = df.withColumn("city_clean", clean_city("city")) \
              .withColumn("price_clean", clean_price("price")) \
              .select("id", "city_clean", "price_clean")
         
  # écriture en csv    
  # df_clean.repartition(1).write.mode("overwrite").option("header", True).csv("output/clean")
  
  # Solution altérnative
  import pandas as pd 
  import os
  
  pandas_df = df_clean.toPandas()
  
  os.makedirs("output", exist_ok=True)
  
  pandas_df.to_csv("output/clean_data.csv", index=False)
  
  spark.stop()