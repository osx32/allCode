-- The LEFT JOIN keyword returns all records from the left table (table1), and the
-- matching records (if any) from the right table (table2).

-- The following SQL statement will select all customers, and any orders they might have
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

-- Note: The LEFT JOIN keyword returns all records from the left table (Customers), 
-- even if there are no matches in the right table (Orders).