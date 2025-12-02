import pandas as pd
import numpy as np
from dateutil import parser


def remove_duplicates(df):
    return df.drop_duplicates()


def handle_missing_values(df, strategy = None):
    if strategy is None:
        strategy = {}

    df_cleaned = df.copy()

    for column, action in strategy.items():
        if column not in df_cleaned.columns:
            continue

        if action == 'drop':
            df_cleaned = df_cleaned.dropna(subset=[column])
        elif action == 'mean':
            df_cleaned[column] = df_cleaned[column].fillna(df_cleaned[column].mean())
        elif action == 'median':
            df_cleaned[column] = df_cleaned[column].fillna(df_cleaned[column].median())
        elif action == 'mode':
            mode_value = df_cleaned[column].mode()[0] if not df_cleaned[column].mode().empty else None
            df_cleaned[column] = df_cleaned[column].fillna(mode_value)
        elif isinstance(action, (str, int, float)):
            df_cleaned[column] = df_cleaned[column].fillna(action)

    return df_cleaned


def clean_dates(df, date_column):
    df_cleaned = df.copy()

    def parse_date(date_str):
        if pd.isna(date_str):
            return None
        try:
            parsed_date = parser.parse(str(date_str), dayfirst=True)
            return parsed_date.strftime('%Y-%m-%d')
        except:
            return None

    df_cleaned[date_column] = df_cleaned[date_column].apply(parse_date)

    return df_cleaned


def validate_prices(df, price_columns):
    df_cleaned = df.copy()

    for column in price_columns:
        if column in df_cleaned.columns:
            df_cleaned[column] = pd.to_numeric(df_cleaned[column], errors='coerce')
            df_cleaned.loc[df_cleaned[column] < 0, column] = np.nan

    return df_cleaned


def validate_price_consistency(df, quantity_col = 'Quantity',
                               unit_price_col = 'Price Per Unit',
                               total_col = 'Total Spent',
                               tolerance = 0.01):
    df_cleaned = df.copy()

    if all(col in df_cleaned.columns for col in [quantity_col, unit_price_col, total_col]):
        calculated_total = df_cleaned[quantity_col] * df_cleaned[unit_price_col]
        diff = abs(df_cleaned[total_col] - calculated_total)
        df_cleaned['price_inconsistent'] = diff > tolerance

    return df_cleaned


def clean_text(df, text_columns) :
    df_cleaned = df.copy()

    for column in text_columns:
        if column in df_cleaned.columns:
            df_cleaned[column] = df_cleaned[column].str.strip()
            df_cleaned[column] = df_cleaned[column].str.replace(r'\s+', ' ', regex=True)

    return df_cleaned


def normalize_case(df, column, case_type = 'title') :
    df_cleaned = df.copy()

    if column in df_cleaned.columns:
        if case_type == 'title':
            df_cleaned[column] = df_cleaned[column].str.title()
        elif case_type == 'lower':
            df_cleaned[column] = df_cleaned[column].str.lower()
        elif case_type == 'upper':
            df_cleaned[column] = df_cleaned[column].str.upper()

    return df_cleaned


def standardize_categories(df, column, valid_categories = None) :

    df_cleaned = df.copy()

    if column not in df_cleaned.columns:
        return df_cleaned

    if valid_categories:
        df_cleaned[column] = df_cleaned[column].str.lower().map(
            {k.lower(): v for k, v in valid_categories.items()}
        ).fillna(df_cleaned[column])

    return df_cleaned


def clean_data(df):
    df = remove_duplicates(df)

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].replace(['ERROR', 'UNKNOWN'], None)

    text_columns = ['Item', 'Payment Method', 'Location']
    df = clean_text(df, text_columns)

    if 'Item' in df.columns:
        df = normalize_case(df, 'Item', 'title')


    price_columns = ['Price Per Unit', 'Total Spent']
    df = validate_prices(df, price_columns)

    if 'Quantity' in df.columns:
        df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

    strategy = {
        'Transaction Date': 'drop',
        'Item': 'drop',
        'Quantity': 'drop',
        'Price Per Unit': 'median',
        'Total Spent': 'drop',
        'Payment Method': 'Unknown',
        'Location': 'Unknown'
    }
    df = handle_missing_values(df, strategy)

    if 'Transaction Date' in df.columns:
        df = clean_dates(df, 'Transaction Date')

    return df
