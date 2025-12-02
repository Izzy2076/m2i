from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType


def clean_emails(df):
    """
       on utilise trim pour implémenter notre logique  de normalisation 
       => on teste donc notre fonction 
    """
    return df.withColumn("email", F.trim(F.col("email")))

def convert_age_to_int(df):
    return df.withColumn("age", F.col("age").cast(IntegerType()))

def clean_data_pipeline(df):
    # Pipeline complète de nettoyage :
    return df \
            .transform(clean_emails) \
            .transform(convert_age_to_int)
