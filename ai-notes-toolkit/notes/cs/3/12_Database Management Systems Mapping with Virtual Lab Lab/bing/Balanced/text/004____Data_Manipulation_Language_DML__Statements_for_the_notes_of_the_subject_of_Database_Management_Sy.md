## Data Manipulation Language(DML) Statements

- Data manipulation language (DML) statements are used to access and manipulate data in existing schema objects, such as tables, views, or indexes  .
- DML statements can update, insert, delete, or select data from the database   .
- DML statements are part of a transaction, which is a sequence of one or more SQL statements that are treated as a unit by the database . A transaction can be committed (made permanent) or rolled back (undone) by the user or the database system .
- The most common DML statements are:
  - **SELECT**: retrieves data from one or more tables or views    . It can also perform calculations, aggregations, joins, filters, and other operations on the retrieved data    .
  - **INSERT**: adds one or more rows of data to a table or a view    . It can also specify the values for each column or use a subquery to get the values from another table or view    .
  - **UPDATE**: modifies one or more columns of data in a table or a view    . It can also use a subquery to get the new values from another table or view    .
  - **DELETE**: removes one or more rows of data from a table or a view    . It can also use a subquery to specify which rows to delete from another table or view    .
- Some other DML statements are:
  - **MERGE**: combines the functionality of INSERT and UPDATE statements by inserting new rows or updating existing rows based on a condition    .
  - **CALL**: invokes a stored procedure or a function    .
  - **EXPLAIN PLAN**: displays the execution plan of a SQL statement, which shows how the database will access the data    .
  - **LOCK TABLE**: locks one or more tables or views in a specified mode to prevent other users from modifying the data    .
- DML statements can be used in various contexts, such as interactive SQL tools, application programs, scripts, or stored procedures  .
- DML statements can be affected by various factors, such as constraints, triggers, indexes, privileges, or performance  .