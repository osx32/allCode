-- The CREATE TABLE statement is used to create a new table in a database.
-- The column parameters specify the names of the columns of the table.
-- The datatype parameter specifies the type of data the column can hold (e.g. varchar, 
-- integer, date, etc.).



/*
-- The following example creates a table called "Persons" that contains five columns: PersonID,
-- LastName, FirstName, Address, and City:
CREATE TABLE Persons(
	PersonID int,
    LastName varchar(255),
    Address varchar(255),
    City varchar(255)
);
-- The PersonID column is of type int and will hold an integer.
-- The LastName, FirstName, Address, and City columns are of type varchar and will hold characters, 
-- and the maximum length for these fields is 255 characters.
*/



-- Create Table Using Another Table
-- A copy of an existing table can also be created using CREATE TABLE.
-- The new table gets the same column definitions. All columns or specific columns can be selected.
-- If you create a new table using an existing table, the new table will be filled with the existing 
-- values from the old table.
CREATE TABLE TestTable AS
SELECT PersonID, LastName, Address
FROM persons;




