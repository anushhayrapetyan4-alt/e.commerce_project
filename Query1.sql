USE ecommerce_db

-- QUERY 1: Top 5 Most Expensive Discounted Products in 'Men' Category
SELECT * FROM ecommerce_db.men 
WHERE discount > 0
ORDER BY current_price DESC 
LIMIT 5;