# Write your MySQL query statement below
SELECT product_name, year, price FROM Product AS p
RIGHT JOIN Sales ON Sales.product_id=P.product_id