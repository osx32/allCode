-- The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.
-- The BETWEEN operator is inclusive: begin and end values are included.

/*
-- The following SQL statement selects all products with a price between 10 and 20:
SELECT * FROM products
WHERE buyPrice BETWEEN 10 AND 20;
*/

/*
-- To display the products outside the range of the previous example, use NOT BETWEEN:
SELECT * FROM products
WHERE buyPrice NOT BETWEEN 10 AND 20;
*/

/*
-- The following SQL statement selects all products with a price between 10 and 20. 
-- In addition; do not show products with a quantityInStock of 15 68 136:
SELECT * FROM products
WHERE buyPrice BETWEEN 10 AND 20
AND quantityInStock NOT IN (15, 68, 136);
*/

/*
-- The following SQL statement selects all products with a ProductName between 
-- '1969 Harley Davidson Ultimate Chopper' and '1972 Alfa Romeo GTA':
SELECT * FROM products
WHERE productName Between '1969 Harley Davidson Ultimate Chopper' AND '1972 Alfa Romeo GTA'
ORDER BY productName;
*/

/*
-- The following SQL statement selects all products with a productName not between
-- '1969 Harley Davidson Ultimate Chopper' and '1972 Alfa Romeo GTA':
SELECT * FROM products
WHERE productName NOT BETWEEN '1969 Harley Davidson Ultimate Chopper' and 
'1972 Alfa Romeo GTA'
ORDER BY productName;
*/


-- The following SQL statement selects all orders with an orderDate between '2003-07-01'
-- and '2003-07-9':
SELECT * FROM orders
WHERE orderDate BETWEEN '2003-07-01' AND '2003-07-9';


