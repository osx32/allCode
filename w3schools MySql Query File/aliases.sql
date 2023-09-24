/*
-- The following SQL statement creates two aliases, one for the CustomerID column and one for the CustomerName column:
SELECT customerNumber AS ID, customerName AS Customer
FROM customers; 
*/

/*
-- The following SQL statement creates two aliases, one for the customerName column and one for
-- the customerName column and one for the contactFirstName column. Note: Single or double
-- quotation marks are required if the alias name contains spaces:
SELECT customerName AS Customer, contactFirstName AS "Contact Person"
FROM customers;
*/


/*
-- The following SQL statement creates an alias named "Address" that combine four
-- columns (Address, PostalCode, City and Country):
SELECT customerNAme, CONCAT_WS(', ', addressLine1, postalCode, city, country) AS Address
FROM customers; 
*/

/*
-- The following SQL statement selects all the orders from the customer with customerNumber=103
-- (Atelier graphique). We use the "Customers" and "Orders" tables, and give them the table
-- aliases of "c" and "o" respectively (Here we use aliases to make the SQL shorter
SELECT o.OrderNumber, o.orderDate, c.customerName
FROM customers AS c, orders AS o
WHERE c.customerName='Atelier graphique' AND
c.customerNumber=o.customerNumber;
*/
 

-- The following SQL statement is the same as above, but without aliases:
SELECT orders.orderNumber, orders.orderDate,
customers.customerName
FROM customers, orders
WHERE customers.customerName = 'Atelier graphique' AND
customers.customerNumber = orders.customerNumber;






