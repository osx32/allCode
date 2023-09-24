-- The RIGHT JOIN keyword returns all records from the right table (table2), and the
-- matching records (if any) from the left table (table1).

-- The following SQL statement will return all employees, and any orders they might have placed:
SELECT Orders.OrderID, Employees.LastName,
Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = 
Employees.EmployeeID
ORDER BY Orders.OrderID;
