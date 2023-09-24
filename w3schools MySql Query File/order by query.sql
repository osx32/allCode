
/*
-- The following SQL statement selects all customers from the "Customers" table, sorted by the "Country" column:
SELECT * FROM customers
ORDER BY country;
*/

/*
-- The following SQL statement selects all customers from the "Customers" table, sorted DESCENDING by the "Country" column:
SELECT * FROM customers
ORDER BY country DESC;
*/

/*
-- The following SQL statement selects all customers from the "Customers" table, sorted by the "Country" and the "CustomersName"
-- column. This meaans that if orders by Country, but if some rows have the same Country, it orders them by CustomerName:
SELECT * FROM customers
ORDER BY country, customerName;
*/

SELECT * FROM customers
ORDER BY country ASC, customerName DESC;





