/*
-- The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.
-- The ALTER TABLE statement is also used to add and drop various constraints on an existing table.
-- The following SQL adds an "Email" column to the "Customers" table:
ALTER TABLE customers
ADD Email varchar(255);
*/



/*
-- To delete a column in a table, use the following syntax (notice that some database systems don't allow deleting a column):
-- The following SQL deletes the "Email" column from the "Customers" table:
ALTER TABLE Customers
DROP COLUMN Email;
*/



/*
-- To change the data type of a column in a table, use the following syntax:
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
*/



/*
-- Now we want to add a column named "DateOfBirth" in the "Persons" table.
ALTER TABLE employees
ADD DateOfBirth date;
*/



-- Now we want to change the data type of the column named "DateOfBirth" in the "employees" table.
ALTER TABLE employees
MODIFY COLUMN DateOfBirth year;
-- Notice that the "DateOfBirth" column is now of type year and is going to hold a year in a two- or four-digit format.

