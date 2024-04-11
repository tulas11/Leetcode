# Write your MySQL query statement below
SELECT c.name as Customers
FROM Customers c
WHERE id not in (
    Select CustomerId
    from Orders
)
