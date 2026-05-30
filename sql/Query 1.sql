-- --QUERY 1: Top 5 Most Expensive Discounted Products in 'Men' Category--

SELECT * 
FROM ecommerce_db.men 
WHERE discount > 0
ORDER BY current_price DESC 
LIMIT 5;

-- QuERY 2: Which product categories have the highest average prices and discounts?

SELECT
    c.category_name,
    COUNT(p.product_id) AS total_products,
    ROUND(AVG(ps.sale_price), 2) AS average_sale_price,
    ROUND(AVG(ps.discount_rate), 2) AS average_discount
FROM categories c
JOIN products p
    ON c.category_id = p.category_id
JOIN product_stats ps
    ON p.product_id = ps.product_id
GROUP BY c.category_name
ORDER BY average_sale_price DESC;


-- Query 3: Which products receive the highest number of customer reviews?

SELECT
    p.product_name,
    c.category_name,
    ps.review_count
FROM products p
JOIN categories c
    ON p.category_id = c.category_id
JOIN product_stats ps
    ON p.product_id = ps.product_id
ORDER BY ps.review_count DESC
LIMIT 10;


-- Query 4: Which products have discounts greater than 50%?

SELECT
    p.product_name,
    ps.original_price,
    ps.sale_price,
    ps.discount_rate
FROM products p
JOIN product_stats ps
    ON p.product_id = ps.product_id
WHERE ps.discount_rate > 50
ORDER BY ps.discount_rate DESC;


-- Query 5: Which categories generate the largest number of customer reviews?

SELECT
    c.category_name,
    SUM(ps.review_count) AS total_reviews
FROM categories c
JOIN products p
    ON c.category_id = p.category_id
JOIN product_stats ps
    ON p.product_id = ps.product_id
GROUP BY c.category_name
ORDER BY total_reviews DESC;


-- Query 6: What are the most expensive products within each category?

SELECT
    p.product_name,
    c.category_name,
    ps.sale_price,
    DENSE_RANK() OVER (
        PARTITION BY c.category_name
        ORDER BY ps.sale_price DESC
    ) AS price_rank
FROM products p
JOIN categories c
    ON p.category_id = c.category_id
JOIN product_stats ps
    ON p.product_id = ps.product_id;


-- Query 7: Which categories have the highest average customer engagement?

SELECT
    c.category_name,
    ROUND(AVG(ps.review_count), 2) AS average_reviews
FROM categories c
JOIN products p
    ON c.category_id = p.category_id
JOIN product_stats ps
    ON p.product_id = ps.product_id
GROUP BY c.category_name
ORDER BY average_reviews DESC;
