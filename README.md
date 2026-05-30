# e.commerce_project
# E-Commerce Data Analysis Project

## Project Description

This project was created to practice database design, data cleaning, and SQL analysis using e-commerce sales data.

The database contains information about customers, products, and orders. After creating the database structure, several data cleaning operations are applied to improve data quality. Analytical SQL queries are then used to examine sales performance and customer activity.

## Database Tables

### customers

Stores customer information.

| Column        | Description                |
| ------------- | -------------------------- |
| customer_id   | Unique customer identifier |
| customer_name | Customer name              |
| country       | Country of residence       |
| signup_date   | Registration date          |

### products

Stores product information.

| Column       | Description               |
| ------------ | ------------------------- |
| product_id   | Unique product identifier |
| product_name | Product name              |
| category     | Product category          |
| price        | Product price             |
| size         | Product size              |

### orders

Stores order transactions.

| Column      | Description                   |
| ----------- | ----------------------------- |
| order_id    | Unique order identifier       |
| customer_id | Customer who placed the order |
| product_id  | Purchased product             |
| quantity    | Number of items purchased     |
| order_date  | Order date                    |

## Data Cleaning Tasks

The following cleaning operations are performed:

* Removing unnecessary spaces from text fields
* Standardizing product size values
* Checking for missing values
* Verifying data consistency between tables

## Analytical Queries

The project includes SQL queries for:

* Total sales calculation
* Most purchased products
* Customer order statistics
* Revenue analysis by category
* Customer retention analysis

## Project Structure

```text
SQL_Scripts/
│
├── 01_schema_setup.sql
├── 02_data_cleaning.sql
└── 03_analytics_queries.sql

README.md
```

## Conclusion

This project demonstrates the use of SQL for database creation, data preparation, and business analysis on e-commerce transaction data.
