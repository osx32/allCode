/*
-- The following SQL statement selects all the customers from "Germany":
SELECT * FROM customers
WHERE country='Germany';
*/

-- Equal
/*
SELECT * FROM customers
WHERE customerNumber=103;
*/

-- Equal
/*
SELECT * FROM customers
WHERE customerName="Atelier graphique";
*/

-- Greater than
/*
SELECT * FROM customers
WHERE creditLimit>100000;
*/


-- Less than
/*
SELECT * FROM customers
WHERE creditLimit<100000;
*/

-- Greater than or equal
/*
SELECT * FROM customers
WHERE creditLimit>=200000;
*/

-- Less than or equal
/*
SELECT * FROM customers
WHERE creditLimit<=200000;
*/

-- Not equal. Note: In some versions of SQL this operator may be written as !=
/*
SELECT * FROM customers
WHERE creditLimit <> 200000;
*/

-- Between a certain range
/*
SELECT * FROM customers
WHERE creditLimit BETWEEN 200000 AND 250000;
*/

-- Search for a pattern
/*
SELECT * FROM customers
WHERE city LIKE 'g%';
*/

-- To specify multiple possible values for a column
/*
SELECT * FROM customers
WHERE city IN('Paris','London');
*/