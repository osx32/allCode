-- WHERE customerName LIKE 'a%' : Finds any values that starts with "a"
-- WHERE customerName LIKE '%a' : Finds any values that ends with "a"
-- WHERE customerName LIKE '%or%' : Finds any values that have "or" in any position 
-- WHERE customerName LIKE '_r%' : Finds any values that have "r" in the second position
-- WHERE customerName LIKE 'a_%_%' : Finds any values that starts with "a" and are at least 3
								  -- characters in length
-- WHERE customerName LIKE 'a%o' : Finds any values that starts with "a" and ends with "o"

/*
-- The following SQL statement selects all customers with a City starting with "ber":
SELECT * FROM customers
WHERE city LIKE 'ber%';
*/

/*
-- The following SQL statement selects all customers with a city containing the pattern "es":
SELECT * FROM customers
WHERE city LIKE '%es%';
*/

/*
-- The following SQL statment selects all customers with a city starting with any character, followed by "ondon":
SELECT * FROM customers
WHERE city LIKE '_ondon';
*/


-- The following SQL statement selects all customers with a city starting with "L", followed by any character, followed
-- by "n", followed by any character, followed by "on":
SELECT * FROM customers
WHERE city LIKE 'L_n_on';
