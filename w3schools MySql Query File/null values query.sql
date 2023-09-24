use classicmodels;
/*
-- The IS NULL operator is used to test for empty values (Null values)
-- The following SQL lists all customers with a NULL value in the "Address" field:
SELECT customerName, contactFirstName, state
FROM customers
WHERE state IS NULL;
*/

-- The IS NOT NULL operator is used to test for non-empty values (NOT NULL values)
-- The following SQL lists all customers with a value in the "Address" field:
SELECT customerName, contactFirstName, addressLine2
FROM customers
WHERE addressLine2 IS NOT NULL;





