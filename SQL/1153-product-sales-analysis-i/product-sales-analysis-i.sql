/* Write your PL/SQL query statement below */
SELECT 
    (SELECT product_name FROM Product WHERE product_id = s.product_id) AS product_name,
    s.year,
    s.price
FROM 
    Sales s;
	