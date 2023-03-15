### DML in PL/SQL

- DML stands for Data Manipulation Language. These statements are mainly used to perform the manipulation activity on the data stored in the database tables or views .
- DML statements can be executed from within any PL/SQL block of code, such as procedures, functions, triggers, packages, etc.
- The four types of DML statements are: INSERT, UPDATE, DELETE, and MERGE .
- INSERT statement is used to insert new rows into a table or a view .
- UPDATE statement is used to modify the values of existing rows in a table or a view .
- DELETE statement is used to remove existing rows from a table or a view .
- MERGE statement is used to combine the data from two tables into one, based on a matching condition .
- DML statements can be executed either implicitly or explicitly in PL/SQL.
- Implicit execution means that the DML statement is executed automatically by the PL/SQL engine, without using the EXECUTE IMMEDIATE statement.
- Explicit execution means that the DML statement is executed by using the EXECUTE IMMEDIATE statement, which allows dynamic SQL execution.
- DML statements can also use bind variables, which are placeholders for actual values that are supplied at run time.
- Bind variables can improve the performance and security of DML statements, as they reduce the parsing overhead and prevent SQL injection attacks.
- DML statements can be followed by the RETURNING clause, which returns the values of the affected rows after the execution.
- The RETURNING clause can be used with bulk operations, such as FORALL, to return multiple rows at once.
- DML statements can also use the RETURNING BULK COLLECT INTO clause, which returns the values of the affected rows into a collection variable.
- DML statements can be combined with transaction control statements, such as COMMIT, ROLLBACK, and SAVEPOINT, to manage the changes made to the database.
- DML statements can also use the AUTONOMOUS_TRANSACTION pragma, which allows a subprogram to execute its own independent transaction, regardless of the main transaction.
- DML statements can raise exceptions, such as DUP_VAL_ON_INDEX, NO_DATA_FOUND, TOO_MANY_ROWS, etc, which can be handled by using the EXCEPTION section of the PL/SQL block.