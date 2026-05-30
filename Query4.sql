-- QUERY 4: Find products priced above the average product price.

SELECT
    name,
    brand,
    current_price
FROM men
WHERE current_price >
(
    SELECT AVG(current_price)
    FROM kids
)
ORDER BY current_price DESC;