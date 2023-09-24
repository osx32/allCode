/*
-- The following SQL statement updates the first customer (customerNumber = 103) with a new contact person and a new city.
UPDATE customers
SET contactFirstName = 'Fatih', city='Istanbul'
WHERE customerNumber = 103;
*/

/*
-- It is the WHERE clause that determines how many records will be updated.
-- The following SQL statement will update the postalCode to 00000 for all records where country is 'France':
UPDATE customers
SET postalCode = 00000
WHERE country='France';
*/
SELECT * FROM customers;
