/*
-- Finds any values that start with "a"
WHERE CustomerName LIKE 'a%'

-- Finds any values that end with "a"
WHERE CustomerName LIKE '%a'

-- Finds any values that haev "or" in any position
WHERE CustomerName LIKE '%or%'

-- Finds any values that have "r" in the second position
WHERE CustomerName LIKE '_r%'

-- Finds any values that start with "a" and are at least 2 characters in length
WHERE CustomerName LIKE 'a_%'

-- Finds any values that start with "a" and are at least  characters in length
WHERE CustomerName LIKE 'a__%'

-- Finds any values that start with "a" and ends with "o"
WHERE contactFirstName LIKE 'a%o'
*/

/*
-- The following SQL statement selects all customers with a customerNAme starting with "a":
SELECT * FROM customers
WHERE customerName LIKE 'a%';
*/

/*
-- The following SQL statement selects all customers with a customerName ending with "s":
SELECT * FROM customers
WHERE customerName LIKE '%s';
*/

/*
-- The following SQL statement selects all customers with a customerName that 
-- have "or" in any position:
SELECT * FROM customers
WHERE customerName LIKE '%or%';
*/

/*
-- The following SQL statement selects all customers with a customerName that have "r" in
-- the second position:
SELECT * FROM customers
WHERE customerName LIKE '_r%';
*/

/*
-- The following SQL statement selects all customers with a customerName starts with "a" and 
-- are at least 3 characters in length: 
SELECT * FROM customers
WHERE customerName LIKE 'a__%';
*/

/*
-- The following SQL statement selects all customers with a contactFirstName that starts
-- with "a" ends with "o":
SELECT * FROM customers
WHERE contactFirstName LIKE 'a%o';
*/

-- The following SQL statement selects all customers with a customerName that does NOT start
-- with "a":
SELECT * FROM customers
WHERE customerName NOT LIKE 'a%';





