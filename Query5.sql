-- Query 5: Calculate savings customers receive from discounts.

SELECT
    name,
    brand,
    raw_price,
    current_price,
    (raw_price - current_price) AS savings
FROM men
ORDER BY savings DESC
LIMIT 10;