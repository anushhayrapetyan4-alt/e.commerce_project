
-- QUERY 3: Find products with the highest discounts.

SELECT
    name,
    brand,
    raw_price,
    current_price,
    discount
FROM men
ORDER BY discount DESC
LIMIT 10;