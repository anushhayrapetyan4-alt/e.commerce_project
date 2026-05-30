import pandas as pd


def clean_product_sizes(products_df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize product size values.
    """

    products_df["size"] = (
        products_df["size"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    return products_df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate records.
    """

    return df.drop_duplicates()
