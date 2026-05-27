import pandas as pd


def extract_raw_data(table_name, engine):
    print(f"1. Extract: Վերցնում ենք տվյալները '{table_name}' աղյուսակից...")

    df = pd.read_sql(
        f"SELECT * FROM ecommerce_db.{table_name}",
        con=engine
    )

    return df
