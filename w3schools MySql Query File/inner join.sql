-- The INNER JOIN keyword selects records that have matching values in both tables.
-- In this tutorial we will use the well-known Northwind sample database.

--      MySQL INNER JOIN Example
-- The following SQL statement selects all orders with customer information:
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- Note : The INNER JOIN keyword selects all rows from both tables as long as there is a match
-- between the columns. If there are records in the "Orders" table that do not have matches 
-- in "Customers", these orders will not be shown

--     JOIN Three Tables
-- Thee following SQL statement selectss all orders with customer and shipper information:
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID =Shippers.ShipperID);




