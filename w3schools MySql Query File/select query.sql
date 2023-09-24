/*
-- The following  statement selects the "firstName", "extension", "email" columns from the "employees" table:
SELECT firstName, extension, email FROM employees; 
*/

/*
-- The following SQL statement selects ALL the columns from the "Customers" table :
SELECT * FROM customers;
*/

/*
-- the SELECT DISTINCT statement is used to return only distinct (different) value.
-- Inside a table, a column often contains many duplicate values; and sometimes you only want to list 
-- the different (distinct) values.
SELECT DISTINCT city, contactFirstName FROM customers;
*/

/*
-- the following SQL statement selects only thee DISTINCT values from the "" column in the "" table:
SELECT DISTINCT contactFirstName FROM Customers;
*/

/*
-- the following SQL statement counts and returns the number of different(distinct) countries 
-- in the "Customers" table:
SELECT COUNT(DISTINCT contactFirstName) FROM customers;
*/