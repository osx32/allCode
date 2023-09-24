/*
-- The IN operator allows you to specify multiple values in a WHERE clause.
-- The IN operator is a shorthand for multiple OR conditions
-- The following SQL statement selects all customers that are located in "Germany", "France" or "UK":
SELECT * FROM customers
WHERE country IN ('Germany', 'France', 'UK');
*/

/*
-- The following SQL statement selects all customers that are NOT located in 'Germany', 'France' or 'UK':
SELECT * FROM customers
WHERE country NOT IN ('Germany', 'France', 'UK');
*/

-- The following SQL statement selects all customers that are from the same countries as the suppliers:
SELECT * FROM customers
WHERE country IN(SELECT country FROM suppliers);

