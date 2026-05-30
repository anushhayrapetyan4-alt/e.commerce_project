from sqlalchemy import create_engine
from extract import extract_raw_data
from transform import clean_product_sizes
from load import load_to_database


engine = create_engine(
    "mysql+pymysql://root:password@localhost/ecommerce_db"
)

products = extract_raw_data("products", engine)

products = clean_product_sizes(products)

load_to_database(
    products,
    "products_clean",
    engine
)

print("Pipeline completed successfully.")
