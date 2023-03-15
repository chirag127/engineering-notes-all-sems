### DML in PL/SQL

- DML stands for Data Manipulation Language. These statements are mainly used to perform the manipulation activity on the data stored in the database tables or views .
- DML statements can be executed from within any PL/SQL block of code, such as procedures, functions, triggers, packages, etc.
- The most common DML statements are INSERT, UPDATE, DELETE, and MERGE .
- INSERT statement is used to insert new rows into a table or a view.
- UPDATE statement is used to modify the values of existing rows in a table or a view.
- DELETE statement is used to remove existing rows from a table or a view.
- MERGE statement is used to combine the data from two tables into one, based on a matching condition.
- DML statements can be executed using the EXECUTE IMMEDIATE statement, which allows dynamic SQL execution in PL/SQL.
- DML statements can also be executed using the cursor FOR loop, which allows iterating over the result set of a query and performing DML operations on each row.
- DML statements can be combined with transaction control statements, such as COMMIT, ROLLBACK, and SAVEPOINT, to manage the changes made to the database.
- DML statements can be affected by the integrity constraints, triggers, and exceptions defined on the database objects.
- DML statements can return the number of rows affected by using the SQL%ROWCOUNT attribute of the implicit cursor.
- DML statements can also return the values of the columns of the affected rows by using the RETURNING clause.