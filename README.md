# e.commerce_project
# NewChic E-Commerce Data Ingestion & Analytics Pipeline

## Project Overview
This repository contains an end-to-end data pipeline designed to analyze transactional e-commerce data from NewChic using a structured Dimensional Model (Star Schema). The analytics layer is built using optimized MySQL queries focusing on multi-table aggregations, time-series trends, and window functions to answer critical business and marketing questions.

---

## Data Architecture & Schema Design
The project utilizes a Star Schema relational structure with the following tables:

### 1. customers 
* `customer_id` (INT, PK) — Unique identifier for each customer.
* `customer_name` (VARCHAR) — Full name of the user.
* `country` (VARCHAR) — Customer's geographical location (e.g., City/Region).
* `signup_date` (DATE) — Date the user registered.

### 2. products
* `product_id` (INT, PK) — Unique product SKU.
* `product_name` (VARCHAR) — Item description (e.g., "Vintage Linen Shirt").
* `category` (VARCHAR) — Product division (e.g., Clothing, Skincare, Footwear).
* `price` (NUMERIC) — Base price per unit in USD ($).
* `size` (VARCHAR) — Raw product size attributes (contains noisy data like ' xl ', 'L').

### 3. orders
* `order_id` (INT, PK) — Unique order transaction ID.
* `customer_id` (INT, FK) — References `customers.customer_id`.
* `product_id` (INT, FK) — References `products.product_id`.
* `quantity` (INT) — Units purchased per item.
* `total_amount` (NUMERIC) — Total monetary value of the line item.
* `traffic_source` (VARCHAR) — Marketing channel (e.g., Organic, Paid Ads).
* `order_date` (DATE) — Timestamp of the transaction.

---

## Repository Structure
```text
├── SQL_Scripts/
│   ├── 01_schema_setup.sql       # DDL scripts for Star Schema tables
│   ├── 02_data_cleaning.sql      # Trimming and casting scripts
│   └── 03_analytics_queries.sql  # Aggregations, Time-Series & Window Functions
└── README.md                     # Documentation
