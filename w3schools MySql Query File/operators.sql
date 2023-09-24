-- SELECT 30 + 20;
-- SELECT 30 - 20;
-- SELECT 30 * 20;
-- SELECT 30 / 10;
-- SELECT 17 % 5;
/*
SELECT * FROM Products
WHERE Price = 18;
*/
/*
SELECT * FROM Products
WHERE Price > 30;
*/
/*
SELECT * FROM Products
WHERE Price < 30;
*/
/*
SELECT * FROM Products 
WHERE PRICE >= 30;
*/
/*
SELECT * FROM PRODUCTS
WHERE PRICE <=30;
*/
/*
SELECT * FROM PRODUCTS
WHERE PRICE <> 18;
*/

/*
SELECT * FROM Products
WHERE Price > ALL (SELECT Price FROM Products WHERE Price > 500);
*/

/*
SELECT * FROM Customers
WHERE City = 'London' AND Country = 'UK';
*/

/*
SELECT * FROM Products
WHERE Price > ANY (SELECT Price FROM Products WHERE Price > 20);
*/

/*
SELECT * FROM Products
WHERE Price BETWEEN 50 AND 60;
*/

/*
SELECT * FROM Products
WHERE EXISTS (SELECT Price FROM Products WHERE Price > 50);
*/

/*
SELECT * FROM Customers
WHERE City IN ('Paris','London');
*/

/*
SELECT * FROM Customers
WHERE City LIKE 's%';
*/

/*
SELECT * FROM Customers
WHERE City NOT LIKE 's%';
*/

/*
SELECT * FROM Customers
WHERE City = 'London' OR Country = 'UK';
*/

/*
SELECT * FROM Products
WHERE Price > SOME (SELECT Price FROM Products WHERE Price > 20);
*/