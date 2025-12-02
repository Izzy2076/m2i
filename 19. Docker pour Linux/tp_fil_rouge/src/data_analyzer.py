import pandas as pd


def calculate_total_revenue(df, price_column = 'Total Spent'):
    if price_column not in df.columns:
        return 0.0
    return df[price_column].sum()


def sales_by_category(df, category_column = 'Item', price_column= 'Total Spent'):
    if category_column not in df.columns or price_column not in df.columns:
        return pd.Series(dtype=float)
    return df.groupby(category_column)[price_column].sum().sort_values(ascending=False)


def sales_by_period(df, date_column = 'Transaction Date',price_column = 'Total Spent', period = 'day') :
    if date_column not in df.columns or price_column not in df.columns:
        return pd.Series(dtype=float)

    df_copy = df.copy()
    df_copy[date_column] = pd.to_datetime(df_copy[date_column], errors='coerce')
    df_copy = df_copy.dropna(subset=[date_column])

    if period == 'day':
        df_copy['period'] = df_copy[date_column].dt.date
    elif period == 'week':
        df_copy['period'] = df_copy[date_column].dt.to_period('W')
    elif period == 'month':
        df_copy['period'] = df_copy[date_column].dt.to_period('M')

    return df_copy.groupby('period')[price_column].sum()


def top_products(df, product_column = 'Item', quantity_column = 'Quantity', top_n = 10) :
    if product_column not in df.columns or quantity_column not in df.columns:
        return pd.Series(dtype=float)
    return df.groupby(product_column)[quantity_column].sum().nlargest(top_n)


def calculate_average_ticket(df, price_column  = 'Total Spent') :
    if price_column not in df.columns or len(df) == 0:
        return 0.0
    return df[price_column].mean()


def sales_evolution(df, date_column = 'Transaction Date', price_column = 'Total Spent') :
    if date_column not in df.columns or price_column not in df.columns:
        return pd.Series(dtype=float)

    df_copy = df.copy()
    df_copy[date_column] = pd.to_datetime(df_copy[date_column], errors='coerce')
    df_copy = df_copy.dropna(subset=[date_column])
    df_copy = df_copy.sort_values(date_column)

    return df_copy.groupby(df_copy[date_column].dt.date)[price_column].sum()


def descriptive_stats(df, column) :
    if column not in df.columns:
        return {}

    stats = df[column].describe()
    return {
        'mean': stats['mean'],
        'median': df[column].median(),
        'std': stats['std'],
        'min': stats['min'],
        'max': stats['max']
    }


if __name__ == "__main__":
    df = pd.read_csv("./data/processed/clean_cafe_sales.csv")


    print(f"Revenu total: {calculate_total_revenue(df):.2f}€\n")

    print("Ventes par produit:")
    print(sales_by_category(df))

    print("Ventes par période (jour):")
    print(sales_by_period(df))

    print("Top 10 produits:")
    print(top_products(df))

    print(f"Panier moyen: {calculate_average_ticket(df):.2f}€\n")

    print("Évolution des ventes:")
    print(sales_evolution(df))

    print("Statistiques descriptives (Total Spent):")
    print(descriptive_stats(df, 'Total Spent'))
