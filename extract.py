import pandas as pd


def extract_raw_data(table_name: str, engine) -> pd.DataFrame:
    """
    Extract data from a database table.
    """

    print(f"Extracting data from {table_name}...")

    query = f"SELECT * FROM ecommerce_db.{table_name}"

    dataframe = pd.read_sql(query, con=engine)

    return dataframe
