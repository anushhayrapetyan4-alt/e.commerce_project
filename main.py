from sqlalchemy import create_engine

from extract import extract_raw_data
from transform import transform_data
from load import load_to_mysql


if __name__ == "__main__":

    # !!! ՓՈԽԻՐ PASSWORD-Ը ՔՈ MYSQL ԳԱՂՏՆԱԲԱՌՈՎ !!!
    db_connection_str = 'mysql+pymysql://root:PASSWORD@localhost:3306/'

    try:
        raw_engine = create_engine(
            db_connection_str + 'ecommerce_db'
        )

        analytics_engine = create_engine(
            db_connection_str + 'newchic_analytics'
        )

        tables = [
            'men',
            'bags',
            'beauty',
            'house',
            'jewelry',
            'kids',
            'shoes'
        ]

        print("=== ETL ՊԱՅՓԼԱՅՆԸ ՍԿՍՎԵՑ ===\n")

        for t in tables:
            raw_data = extract_raw_data(t, raw_engine)

            cats, prods, stats = transform_data(
                raw_data,
                category_name=t.capitalize()
            )

            load_to_mysql(
                cats,
                prods,
                stats,
                analytics_engine
            )

        print("=== ETL ՊԱՅՓԼԱՅՆԸ ՀԱՋՈՂՈՒԹՅԱՄԲ ԱՎԱՐՏՎԵՑ ===")

    except Exception as e:
        print(f"🔴 Սխալ տեղի ունեցավ. {e}")
