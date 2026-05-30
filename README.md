# e.commerce_project
# NewChic E-Commerce Data Ingestion & Analytics Pipeline

## Project Overview
This project implements an end-to-end data pipeline designed to ingest, clean, and analyze transactional data from the NewChic e-commerce platform. The goal is to transform raw sales and customer logs into structured, analytics-ready tables to drive business intelligence and marketing strategies.

The pipeline handles data definition, automated cleaning constraints, and advanced analytics including cohort retention.

---

## Tech Stack
* **Database/Warehouse:** PostgreSQL / AWS Redshift
* **Language:** SQL (DDL & DML)
* **Core Concepts:** Schema Design, Data Cleaning, Window Functions, Common Table Expressions (CTEs)

---

## Data Architecture & Schema Design
The project utilizes a Star-Schema relational structure to maintain high performance during analytical querying.



### 1. `customers` (Dimension Table)
* `customer_id` (INT, PK) — Unique identifier for each customer.
* `customer_name` (VARCHAR) — Full name of the user.
* `country` (VARCHAR) — Customer's geographical location.
* `signup_date` (DATE) — Date the user registered on NewChic.

### 2. `products` (Dimension Table)
* `product_id` (INT, PK) — Unique product identifier.
* `product_name` (VARCHAR) — Item description (e.g., "Vintage Linen Shirt").
* `category` (VARCHAR) — Clothing/Accessory category.
* `price` (NUMERIC) — Price per unit in USD.
* `size` (VARCHAR) — Raw product size attributes (contains noisy data like ' xl ', 'L').

### 3. `orders` (Fact Table)
* `order_id` (INT, PK) — Unique order transaction ID.
* `customer_id` (INT, FK) — References `customers`.
* `product_id` (INT, FK) — References `products`.
* `quantity` (INT) — Total units purchased.
* `order_date` (DATE) — Timestamp of the transaction.

---

## Repository Structure
```text
├── SQL_Scripts/
│   ├── 01_schema_setup.sql       # DDL scripts for table generation
│   ├── 02_data_cleaning.sql      # Trimming and casting scripts
│   └── 03_analytics_queries.sql  # Window functions & aggregations
└── README.md                     # Documentation
