### DML in PL/SQL

- DML stands for Data Manipulation Language. These statements are mainly used to perform the manipulation activity on the data stored in the database tables or views .
- DML statements can be executed from within any PL/SQL block of code, such as procedures, functions, triggers, packages, etc.
- The four types of DML statements are: INSERT, UPDATE, DELETE, and MERGE .
- INSERT statement is used to insert new rows into a table or a view .
- UPDATE statement is used to modify the existing rows in a table or a view .
- DELETE statement is used to remove the existing rows from a table or a view .
- MERGE statement is used to combine the data from two tables into one, based on a matching condition .
- DML statements can be executed using the EXECUTE IMMEDIATE statement, which allows dynamic SQL execution in PL/SQL.
- DML statements can also be executed using the cursor FOR loop, which allows iterating over the result set of a query and performing DML operations on each row.
- DML statements can be combined with the RETURNING clause, which allows returning the affected rows or expressions as a collection or a variable.
- DML statements can be controlled by the transaction management commands, such as COMMIT, ROLLBACK, and SAVEPOINT, which allow committing, undoing, or saving the changes made by the DML operations .
- DML statements can be affected by the integrity constraints, such as primary key, foreign key, unique, check, and not null, which enforce the rules on the data in the database .
- DML statements can also be affected by the triggers, which are stored procedures that are executed automatically in response to certain events, such as insert, update, delete, or merge .
- DML statements can be optimized by using hints, which are comments that provide additional information to the optimizer on how to execute the statement .