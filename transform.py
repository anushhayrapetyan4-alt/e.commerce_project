import pandas as pd


def transform_data(raw_df, category_name):
    print(f"2. Transform: Մաքրում ենք '{category_name}' տվյալները...")

    if raw_df.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    categories_df = pd.DataFrame([
        {"category_name": category_name}
    ])

    name_col = (
        'product_name'
        if 'product_name' in raw_df.columns
        else ('name' if 'name' in raw_df.columns else raw_df.columns[1])
    )

    id_col = (
        'product_id'
        if 'product_id' in raw_df.columns
        else ('id' if 'id' in raw_df.columns else raw_df.columns[0])
    )

    products_df = raw_df[[id_col, name_col]].copy()

    products_df.columns = [
        'product_id',
        'product_name'
    ]

    products_df = (
        products_df
        .drop_duplicates(subset=['product_id'])
        .dropna()
    )

    price_col = (
        'price'
        if 'price' in raw_df.columns
        else ('sale_price' if 'sale_price' in raw_df.columns else raw_df.columns[2])
    )

    stats_df = pd.DataFrame()

    stats_df['product_id'] = raw_df[id_col]

    stats_df['original_price'] = raw_df[price_col].fillna(0)
    stats_df['sale_price'] = raw_df[price_col].fillna(0)

    stats_df['discount_rate'] = (
        raw_df['discount'].fillna(0)
        if 'discount' in raw_df.columns
        else 0
    )

    stats_df['review_count'] = (
        raw_df['review_count'].fillna(0)
        if 'review_count' in raw_df.columns
        else 0
    )

    stats_df['product_id'] = stats_df['product_id'].astype(int)
    stats_df['discount_rate'] = stats_df['discount_rate'].astype(int)
    stats_df['review_count'] = stats_df['review_count'].astype(int)

    stats_df = stats_df[
        stats_df['product_id'].isin(products_df['product_id'])
    ]

    return categories_df, products_df, stats_df
