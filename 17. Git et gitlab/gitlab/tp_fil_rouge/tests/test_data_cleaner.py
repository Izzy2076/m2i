import pytest
import pandas as pd
import numpy as np
from src import data_cleaner


def test_remove_duplicates(dataframe_with_duplicates):
    result = data_cleaner.remove_duplicates(dataframe_with_duplicates)

    assert len(result) == 2
    assert len(dataframe_with_duplicates) == 3


def test_handle_missing_values_drop(dataframe_with_missing):
    strategy = {'Transaction Date': 'drop'}
    result = data_cleaner.handle_missing_values(dataframe_with_missing, strategy)

    assert result['Transaction Date'].isna().sum() == 0
    assert len(result) == 2


def test_handle_missing_values_mean(dataframe_with_missing):
    strategy = {'Price Per Unit': 'mean'}
    result = data_cleaner.handle_missing_values(dataframe_with_missing, strategy)

    assert result['Price Per Unit'].isna().sum() == 0


def test_handle_missing_values_median(dataframe_with_missing):
    strategy = {'Price Per Unit': 'median'}
    result = data_cleaner.handle_missing_values(dataframe_with_missing, strategy)

    assert result['Price Per Unit'].isna().sum() == 0


def test_handle_missing_values_mode(dataframe_with_missing):
    strategy = {'Payment Method': 'mode'}
    result = data_cleaner.handle_missing_values(dataframe_with_missing, strategy)

    assert result['Payment Method'].isna().sum() == 0


def test_handle_missing_values_default():
    df = pd.DataFrame({
        'Item': ['Coffee', None, 'Cake'],
        'Quantity': [1, 2, 3]
    })
    strategy = {'Item': 'Unknown'}
    result = data_cleaner.handle_missing_values(df, strategy)

    assert result['Item'].isna().sum() == 0
    assert 'Unknown' in result['Item'].values


def test_clean_dates(dirty_dataframe):
    result = data_cleaner.clean_dates(dirty_dataframe, 'Transaction Date')

    assert result['Transaction Date'][0] == '2024-01-15'
    assert result['Transaction Date'][1] == '2024-01-16'
    assert result['Transaction Date'][2] is None 
    assert result['Transaction Date'][3] == '2024-01-17'


def test_clean_dates_with_valid_dates():
    df = pd.DataFrame({
        'Transaction Date': ['15/01/2024', '2024-01-16', '17.01.2024', '01-18-2024']
    })
    result = data_cleaner.clean_dates(df, 'Transaction Date')

    assert result['Transaction Date'][0] == '2024-01-15'
    assert result['Transaction Date'][1] == '2024-01-16'
    assert result['Transaction Date'][2] == '2024-01-17'


def test_validate_prices():
    df = pd.DataFrame({
        'Price Per Unit': [2.50, -1.00, 3.50],
        'Total Spent': [5.00, -2.00, 7.00]
    })
    result = data_cleaner.validate_prices(df, ['Price Per Unit', 'Total Spent'])

    assert result['Price Per Unit'].isna().sum() == 1
    assert result['Total Spent'].isna().sum() == 1
    assert result['Price Per Unit'][0] == 2.50
    assert pd.isna(result['Price Per Unit'][1])


def test_validate_price_consistency():
    df = pd.DataFrame({
        'Quantity': [2, 1, 3],
        'Price Per Unit': [2.50, 3.50, 2.00],
        'Total Spent': [5.00, 3.50, 7.00] 
    })
    result = data_cleaner.validate_price_consistency(df)

    assert 'price_inconsistent' in result.columns
    assert result['price_inconsistent'][0] == False
    assert result['price_inconsistent'][1] == False
    assert result['price_inconsistent'][2] == True


def test_clean_text(dirty_dataframe):
    result = data_cleaner.clean_text(dirty_dataframe, ['Item'])

    assert result['Item'][0] == 'Coffee'
    assert '  ' not in result['Item'][0]


def test_clean_text_multiple_spaces():
    df = pd.DataFrame({
        'Item': ['  Coffee  ', 'Cake    Grande', '  Cookie  ']
    })
    result = data_cleaner.clean_text(df, ['Item'])

    assert result['Item'][0] == 'Coffee'
    assert result['Item'][1] == 'Cake Grande'
    assert result['Item'][2] == 'Cookie'


def test_normalize_case_title(dirty_dataframe):
    result = data_cleaner.normalize_case(dirty_dataframe, 'Item', 'title')

    assert result['Item'][1] == 'Cake'
    assert result['Item'][2] == 'Cookie'


def test_normalize_case_lower(dirty_dataframe):
    result = data_cleaner.normalize_case(dirty_dataframe, 'Payment Method', 'lower')

    assert all(cat == cat.lower() for cat in result['Payment Method'])


def test_normalize_case_upper():
    df = pd.DataFrame({
        'Payment Method': ['cash', 'Cash', 'CASH']
    })
    result = data_cleaner.normalize_case(df, 'Payment Method', 'upper')

    assert all(cat == 'CASH' for cat in result['Payment Method'])


def test_standardize_categories(dirty_dataframe):
    mapping = {
        'cash': 'Cash',
        'CASH': 'Cash',
        'credit card': 'Credit Card'
    }
    result = data_cleaner.standardize_categories(dirty_dataframe, 'Payment Method', mapping)

    assert result['Payment Method'][0] == 'Cash'
    assert result['Payment Method'][1] == 'Credit Card'


def test_standardize_categories_no_mapping():
    df = pd.DataFrame({
        'Payment Method': ['Cash', 'Credit Card', 'Digital Wallet']
    })
    result = data_cleaner.standardize_categories(df, 'Payment Method')

    assert len(result) == 3
    assert list(result['Payment Method']) == list(df['Payment Method'])
