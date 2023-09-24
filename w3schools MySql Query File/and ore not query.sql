-- SELECT * FROM customers;

/*
-- The following SQL statement selects all fields from "Customers" where country is "Germany" AND city is "Berlin":
SELECT * FROM customers
WHERE country='Germany' AND city='Berlin';
*/

/*
-- The following SQL statements selects all fields from "Customers" where city is "Berlin" OR "Stuttgart":
SELECT * FROM customers
WHERE city='Berlin' OR city='Stuttgart';
*/

/*
-- The following SQL statement selects all fields from "Customers" where country is "Germany" OR "Spain" : 
SELECT * FROM customers
WHERE country='Germany' OR country='Spain';
*/

/*
-- The following SQL statement selects all fields from "Customers" where country is NOT "Germany" :
SELECT * FROM customers
WHERE NOT country='Germany';
*/

/*
-- The following SQL statement selects all fields from "Customers" where country is "Germany" AND city must be "Berlin"
-- OR "Stuttgart"(use parenthesis to form complex expressions) :
SELECT * FROM customers
WHERE country='Germany' AND (city='Berlin' OR city='Stuttgart');
*/

/*
-- The following SQL statement selects all fields from "Customers" where country is NOT "Germany" and NOT "USA" :
SELECT * FROM customers
WHERE NOT country='Germany' AND NOT country='USA';
*/