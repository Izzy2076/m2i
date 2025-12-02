import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from pyspark.sql import functions as F
from pipeline_nettoyage import *


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .appName("Exercice 05") \
        .master("local[*]") \
        .getOrCreate()


@pytest.fixture
def sample_products(spark):

    data = [
        ("1", "  laptop dell xps  ", "ÉLECTRONIQUE", "999.99", "10"),
        ("2", "souris logitech", "ACCESSOIRES", "29.99", "50"),
        ("3", "clavier mécanique", "accessoires", "invalid", "5"),
        ("4", "écran samsung", "Électronique  ", "450.50", "-3"),
        ("5", "", "bureautique", "15.00", "100"),
        ("6", "Webcam HD", "accessoires", "89.99", "25"),
    ]
    
    schema = StructType([
        StructField("id", StringType(), True),
        StructField("nom", StringType(), True),
        StructField("categorie", StringType(), True),
        StructField("prix", StringType(), True),
        StructField("stock", StringType(), True),
    ])
    
    return spark.createDataFrame(data, schema)



def test_normalize_product_names_removes_spaces(sample_products):

    result = normalize_product_names(sample_products)
    
    nom = result.filter(F.col("id") == "1").select("nom").first()[0]

    assert nom == nom.strip()
    assert not nom.startswith(" ")
    assert not nom.endswith(" ")

def test_normalize_product_names_applies_title_case(sample_products):

    result = normalize_product_names(sample_products)

    nom = result.filter(F.col("id") == "2").select("nom").first()[0]
    assert nom == "Souris Logitech"

def test_normalize_product_names_handles_both_rules(sample_products):
    result = normalize_product_names(sample_products)

    nom = result.filter(F.col("id") == "1").select("nom").first()[0]
    assert nom == "Laptop Dell Xps"


def test_normalize_categories_converts_to_lowercase(sample_products):
    result = normalize_categories(sample_products)
    
    cat = result.filter(F.col("id") == "1").select("categorie").first()[0]
    assert cat == "électronique"
    
    cat = result.filter(F.col("id") == "2").select("categorie").first()[0]
    assert cat == "accessoires"

def test_normalize_categories_removes_spaces(sample_products):
    result = normalize_categories(sample_products)

    cat = result.filter(F.col("id") == "4").select("categorie").first()[0]
    assert cat == "électronique"
    assert cat == cat.strip()


def test_convert_price_to_float_converts_valid_prices(sample_products):
    result = convert_price_to_float(sample_products)
    
    prix = result.filter(F.col("id") == "1").select("prix").first()[0]
    assert isinstance(prix, float)
    assert prix == 999.99
    
    prix = result.filter(F.col("id") == "2").select("prix").first()[0]
    assert prix == 29.99

def test_convert_price_to_float_invalid_becomes_none(sample_products):

    result = convert_price_to_float(sample_products)
    
    prix = result.filter(F.col("id") == "3").select("prix").first()[0]
    assert prix is None

def test_fix_negative_stock_converts_to_integer(sample_products):
    result = fix_negative_stock(sample_products)
    
    stock = result.filter(F.col("id") == "1").select("stock").first()[0]
    assert isinstance(stock, int)

def test_fix_negative_stock_sets_negative_to_zero(sample_products):
    result = fix_negative_stock(sample_products)
    
    stock = result.filter(F.col("id") == "4").select("stock").first()[0]
    assert stock == 0

def test_fix_negative_stock_keeps_positive_values(sample_products):
    result = fix_negative_stock(sample_products)
    
    stock = result.filter(F.col("id") == "1").select("stock").first()[0]
    assert stock == 10
    
    stock = result.filter(F.col("id") == "2").select("stock").first()[0]
    assert stock == 50



def test_remove_products_without_name_filters_empty_names(sample_products):
    result = remove_products_without_name(sample_products)

    assert result.count() == 5

def test_remove_products_without_name_specific_id_removed(sample_products):
    result = remove_products_without_name(sample_products)
    
    count_id_5 = result.filter(F.col("id") == "5").count()
    assert count_id_5 == 0
    
    count_id_1 = result.filter(F.col("id") == "1").count()
    assert count_id_1 == 1


def test_clean_products_pipeline_end_to_end(sample_products):
    result = clean_products_pipeline(sample_products)
    
    assert result.count() == 5

    row = result.filter(F.col("id") == "1").first()
    
    assert row["nom"] == "Laptop Dell Xps" 
    assert row["categorie"] == "électronique"
    assert row["prix"] == 999.99
    assert isinstance(row["prix"], float)
    assert row["stock"] == 10 
    assert isinstance(row["stock"], int)

def test_clean_products_pipeline_handles_all_edge_cases(sample_products):
    result = clean_products_pipeline(sample_products)
    
    row_3 = result.filter(F.col("id") == "3").first()
    assert row_3["prix"] is None

    row_4 = result.filter(F.col("id") == "4").first()
    assert row_4["stock"] == 0
    
    row_6 = result.filter(F.col("id") == "6").first()
    assert row_6["nom"] == "Webcam Hd"