### DML in PL/SQL

- DML stands for Data Manipulation Language. It is a subset of SQL that is used to manipulate data in tables and views .
- DML statements can be executed from within any PL/SQL block of code, as long as the user has access to the schema objects.
- The main DML statements are:
  - INSERT: used to insert one or more rows into a table or a view .
  - UPDATE: used to modify one or more columns of one or more rows in a table or a view .
  - DELETE: used to remove one or more rows from a table or a view .
  - MERGE: used to merge data from a source table or view into a target table or view, based on a matching condition .
- DML statements can be combined with other SQL clauses, such as WHERE, ORDER BY, GROUP BY, HAVING, etc., to filter, sort, aggregate, or transform the data.
- DML statements can also use variables, expressions, functions, and subqueries to provide dynamic or complex values for the data manipulation.
- DML statements do not implicitly commit the current transaction, meaning that the changes made by the statements are not permanent until the user explicitly commits or rolls back the transaction.
- DML statements can raise exceptions if they encounter errors, such as invalid data, constraint violations, or insufficient privileges. The user can handle these exceptions using PL/SQL exception handlers.