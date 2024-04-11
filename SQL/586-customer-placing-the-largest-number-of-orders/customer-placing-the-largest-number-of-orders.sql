# Write your MySQL query statement below
select customer_number
from orders
group by customer_number
order by count(*) desc
limit 1

-- SELECT customer_number
-- FROM orders
-- GROUP BY customer_number
-- HAVING COUNT(*) = (
--     SELECT MAX(order_count)
--     FROM (
--         SELECT COUNT(*) AS order_count
--         FROM orders
--         GROUP BY customer_number
--     ) AS max_counts
-- );
