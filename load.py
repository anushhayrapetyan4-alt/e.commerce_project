import pandas as pd
from sqlalchemy import text


def load_to_mysql(categories_df, products_df, stats_df, engine):
    print("3. Load: Լցնում ենք նոր բազայի մեջ...")

    if categories_df.empty or products_df.empty:
        return

    categories_df.to_sql(
        'categories',
        con=engine,
        if_exists='append',
        index=False
    )

    with engine.connect() as conn:
        cat_id = conn.execute(
            text("SELECT LAST_INSERT_ID()")
        ).fetchone()[0]

    products_df['category_id'] = cat_id

    products_df.to_sql(
        'products',
        con=engine,
        if_exists='append',
        index=False
    )

    stats_df.to_sql(
        'product_stats',
        con=engine,
        if_exists='append',
        index=False
    )

    print("--- Տվյալները հաջողությամբ փոխանցվեցին! ---\n")
