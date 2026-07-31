### DML in PL/SQL

- DML stands for Data Manipulation Language. It is a subset of SQL that is used to manipulate data in tables and views .
- DML statements can be executed from within any PL/SQL block of code, as long as the user has access to the schema objects.
- The main types of DML statements are:
  - INSERT: used to insert new rows into a table or view .
  - UPDATE: used to modify existing rows in a table or view .
  - DELETE: used to remove existing rows from a table or view .
  - MERGE: used to combine the data from two tables or views based on a matching condition .
- DML statements can be used with variables, expressions, conditions, and subqueries to perform complex data manipulation operations .
- DML statements do not implicitly commit the current transaction, meaning that the changes made by them are not permanent until the user explicitly commits or rolls back the transaction.
- DML statements can be used with the RETURNING clause to return the values of the affected rows after the execution .
- DML statements can raise exceptions if they encounter errors or violations of constraints during the execution.
- DML statements can be combined with PL/SQL control structures, such as loops, conditional statements, and exception handlers, to create more dynamic and flexible programs.