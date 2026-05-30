def load_to_database(df, table_name: str, engine) -> None:
    """
    Load dataframe into database.
    """

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully.")
