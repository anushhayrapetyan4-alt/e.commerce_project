USE ecommerce_db;

-- QUERY 2: Which product categories have the highest average prices and discounts?
SELECT 
    'Men' AS category_name, 
    COUNT(*) AS total_products, 
    ROUND(AVG(current_price), 2) AS average_sale_price, 
    ROUND(AVG(discount), 2) AS average_discount 
FROM ecommerce_db.men
UNION ALL
SELECT 
    'Bags', COUNT(*), ROUND(AVG(current_price), 2), ROUND(AVG(discount), 2) 
FROM ecommerce_db.bags
UNION ALL
SELECT 
    'Beauty', COUNT(*), ROUND(AVG(current_price), 2), ROUND(AVG(discount), 2) 
FROM ecommerce_db.beauty
ORDER BY average_sale_price DESC;