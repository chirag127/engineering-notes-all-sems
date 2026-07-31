# DML in PL/SQL

- DML stands for Data Manipulation Language. These statements are mainly used to perform the manipulation activity on the data stored in the database tables or views  .
- DML statements can be executed from within any PL/SQL block of code, such as procedures, functions, triggers, packages, etc.
- There are four types of DML statements: INSERT, UPDATE, DELETE, and MERGE .
- INSERT statement is used to insert new rows into a table or a view  .
- UPDATE statement is used to modify the existing rows in a table or a view  .
- DELETE statement is used to remove the existing rows from a table or a view  .
- MERGE statement is used to combine the data from two tables into one, based on a matching condition .
- DML statements can be executed either individually or in bulk, using the FORALL statement .
- DML statements can also use variables, expressions, and conditions to manipulate the data dynamically  .
- DML statements can be followed by the RETURNING clause, which returns the values of the affected rows into PL/SQL variables or collections .
- DML statements can be controlled by the transaction management commands, such as COMMIT, ROLLBACK, and SAVEPOINT, to ensure the data consistency and integrity  .
- DML statements can also use the hints, such as /*+ APPEND */, /*+ PARALLEL */, etc, to optimize the performance and execution plan of the statements  .