import pytest
import pandas as pd


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        'Transaction ID': ['TXN_001', 'TXN_002', 'TXN_003'],
        'Transaction Date': ['2024-01-15', '2024-01-16', '2024-01-17'],
        'Item': ['Coffee', 'Cake', 'Cookie'],
        'Quantity': [2, 1, 3],
        'Price Per Unit': [2.50, 3.50, 2.00],
        'Total Spent': [5.00, 3.50, 6.00],
        'Payment Method': ['Cash', 'Credit Card', 'Digital Wallet'],
        'Location': ['In-store', 'Takeaway', 'In-store']
    })


@pytest.fixture
def dirty_dataframe():
    return pd.DataFrame({
        'Transaction ID': ['TXN_001', 'TXN_002', 'TXN_003', 'TXN_004'],
        'Transaction Date': ['15/01/2024', '2024-01-16', 'invalid', '17.01.2024'],
        'Item': ['  Coffee  ', 'CAKE', 'cookie', 'Coffee'],
        'Quantity': [2, -1, 3, 2],
        'Price Per Unit': [2.50, 3.50, 2.00, 2.50],
        'Total Spent': [5.00, 3.50, 6.00, 5.00],
        'Payment Method': ['Cash', 'Credit Card', 'ERROR', 'Cash'],
        'Location': ['In-store', 'Takeaway', 'UNKNOWN', 'In-store']
    })


@pytest.fixture
def dataframe_with_duplicates():
    return pd.DataFrame({
        'Transaction ID': ['TXN_001', 'TXN_001', 'TXN_002'],
        'Transaction Date': ['2024-01-15', '2024-01-15', '2024-01-16'],
        'Item': ['Coffee', 'Coffee', 'Cake'],
        'Quantity': [2, 2, 1],
        'Price Per Unit': [2.50, 2.50, 3.50],
        'Total Spent': [5.00, 5.00, 3.50],
        'Payment Method': ['Cash', 'Cash', 'Credit Card'],
        'Location': ['In-store', 'In-store', 'Takeaway']
    })


@pytest.fixture
def dataframe_with_missing():
    return pd.DataFrame({
        'Transaction ID': ['TXN_001', 'TXN_002', 'TXN_003'],
        'Transaction Date': ['2024-01-15', None, '2024-01-17'],
        'Item': ['Coffee', 'Cake', None],
        'Quantity': [2, 1, 3],
        'Price Per Unit': [2.50, None, 2.00],
        'Total Spent': [5.00, 3.50, 6.00],
        'Payment Method': ['Cash', None, 'Credit Card'],
        'Location': ['In-store', 'Takeaway', None]
    })