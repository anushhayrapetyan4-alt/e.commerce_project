# e.commerce_project
# DataCamp-Style SQL Challenge: NewChic Customer Revenue Analysis

## 📌 Project Overview
This repository contains a practical, business-driven SQL challenge modeled after DataCamp's Associate and Professional Certification exams. The scenario is based on e-commerce transaction data from the global fashion platform **NewChic**.

## 📊 Database Schema
The analysis uses two relational tables:

### 1. `customers`
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `customer_id` | INT (Primary Key) | Unique identifier for each customer |
| `customer_name` | VARCHAR | Full name of the customer |

### 2. `orders`
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_id` | INT (Primary Key) | Unique identifier for each order |
| `customer_id` | INT (Foreign Key) | References `customers.customer_id` |
| `order_date` | DATE | The date the order was placed (e.g., '2025-04-12') |
| `total_amount` | NUMERIC | Total monetary value of the order in USD ($) |

---

## 📋 Business Requirement (The Problem)
The marketing team at NewChic wants to launch a loyalty campaign rewarding high-value customers. 

**Task:** Write an SQL query to identify all customers who spent a total of **more than $500** strictly on orders placed during the calendar year **2025**.

### Acceptance Criteria (DataCamp Rules):
1. Return exactly three columns: `customer_id`, `customer_name`, and `total_spent`.
2. Filter the raw data to include only orders from the year 2025.
3. Aggregate the results per customer and filter out any customer who spent $500 or less.

---

## 🛠️ SQL Solution

```sql
SELECT 
    c.customer_id, 
    c.customer_name, 
    -- Calculate the aggregated total amount spent per customer
    SUM(o.total_amount) AS total_spent
FROM customers c
-- Join customers with their respective orders
JOIN orders o ON c.customer_id = o.customer_id
-- Filter for orders placed only within the year 2025
WHERE o.order_date BETWEEN '2025-01-01' AND '2025-12-31'
-- Group by customer attributes to allow aggregation functions
GROUP BY c.customer_id, c.customer_name
-- Filter aggregated results to only show high-value customers (> $500)
HAVING SUM(o.total_amount) > 500;
