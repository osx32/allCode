/*
-- MySQL IFNULL() and COALESCE() Functions
-- Suppose that the "UnitsOnOrder" column is optional, and may contain NULL values.
--Look at the following SELECT statement:
SELECT ProductName, Price * Unit
FROM Products;
*/



/*
-- MySQL IFNULL() Function
-- The MySQL IFNULL() function lets you return an alternative value if an expression is NULL.
-- The example below returns 0 if the value is NULL:
SELECT ProductsName, Price * IFNULL(Unit, 0) 
FROM Products;
*/



-- MySQL COALESCE() Function
-- Or we can use the COALESCE() function, like this:
SELECT ProductName, Price * COALESCE(Unit, 0)
FROM Products;
