import pytest
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType
from main import clean_emails, convert_age_to_int, clean_data_pipeline

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
            .appName("TDD spark") \
            .master("local[*]") \
            .getOrCreate()

@pytest.fixture
def data(spark):
    data = [
        ("1", "Toto", " toto@email.fr ", "25", "Lille"),
        ("2", "", " test@email.fr", "invalid", "Paris"),
        ("3", "Tata", "tata@email.fr", "45", "Lyon"),
        ("4", "Titi", None, "28", "Lille")
    ]

    schema = StructType([
        StructField("id", StringType(), True),
        StructField("nom", StringType(), True),
        StructField("email", StringType(), True),
        StructField("age", StringType(), True),
        StructField("ville", StringType(), True)
    ])

    return spark.createDataFrame(data, schema)

@pytest.fixture
def data_csv(spark):
    df = spark.read.csv("./data.csv", header=True, inferSchema=True)
    return df.limit(3)

"""
Tests pour nettoyage de données 

On test  notre logique metier, pas spark
"""

def test_clean_email_removes_spaces(data):
    result = clean_emails(data)
    email = result.filter(F.col("id") == "1").select("email").first()[0]
    assert email == "toto@email.fr"


def test_convert_age_to_int(data):
    result = convert_age_to_int(data)
    age = result.filter(F.col("id") == "1").select("age").first()[0]
    assert isinstance(age, int)
    assert age == 25

def test_clean_data_pipeline_end_to_end(data):
    result = clean_data_pipeline(data)

    assert result.count() == 4

    email = result.filter(F.col("id") == "1").select("email").first()[0]
    assert email == "toto@email.fr"

    age = result.filter(F.col("id") == "1").select("age").first()[0]
    assert isinstance(age, int)