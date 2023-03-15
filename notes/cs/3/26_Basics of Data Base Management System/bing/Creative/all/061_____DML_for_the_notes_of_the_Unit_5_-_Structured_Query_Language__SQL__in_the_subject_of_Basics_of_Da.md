# DML

Data Manipulation Language (DML) is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views  . The main DML statements are:

- **SELECT**: retrieve data from one or more tables or views .
- **INSERT**: add new rows of data to a table or view  .
- **UPDATE**: modify existing rows of data in a table or view  .
- **DELETE**: remove existing rows of data from a table or view  .

DML statements can be used with various clauses, such as WHERE, ORDER BY, GROUP BY, HAVING, JOIN, etc., to filter, sort, aggregate, and combine data from different sources.

DML statements can also be used with subqueries, which are nested queries that return a set of rows or a single value to be used by the outer query.

DML statements can be executed interactively or embedded in a program, such as a stored procedure, a function, or a trigger.

DML statements can affect the data in the database, so they need to be executed within a transaction, which is a logical unit of work that ensures data consistency and integrity.

Some examples of DML statements are:

- SELECT * FROM Customers; -- retrieve all the data from the Customers table
- INSERT INTO Customers (CustomerID, Name, City) VALUES (101, 'Alice', 'New York'); -- insert a new row into the Customers table
- UPDATE Customers SET City = 'Los Angeles' WHERE CustomerID = 101; -- update the city of the customer with ID 101
- DELETE FROM Customers WHERE CustomerID = 101; -- delete the customer with ID 101 from the Customers table