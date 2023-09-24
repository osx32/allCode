/*
-- SQL CROSS JOIN Keyword
-- The CROSS JOIN keyword returns all records from both tables (table1 and table2).
-- Note: CROSS JOIN can potentially return very large result-sets!
-- The following SQL statement selects all customers, and all orders:
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
CROSS JOIN Orders;
-- Note: The CROSS JOIN keyword returns all matching records from both tables whether the other
-- table matches or not. So, if there are rows in "Customers" that do not have matches
-- in "Orders", or if there are rows in "Orders" that do not have matches in "Customers", those
-- rows will be listed as well.
*/

-- If you add a WHERE clause (if table1 and table2 has a relationship), the CROSS JOIN will produce the same
-- result as the INNER JOIN clause:
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
CROSS JOIN Orders
WHERE Customers.CustomerID = Orders.CustomerID;
