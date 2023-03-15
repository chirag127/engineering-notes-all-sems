## Data Manipulation Language(DML) Statements

- Data manipulation language (DML) statements are used to access and manipulate data in existing schema objects, such as tables and views  .
- DML statements can update, insert, and delete data from the tables  .
- DML statements are part of a transaction, which is a sequence of one or more SQL statements that are treated as a unit. A transaction can be committed or rolled back as a whole.
- The main DML statements are:
  - **SELECT**: retrieves data from one or more tables or views   .
  - **INSERT**: adds one or more rows of data to a table or view    .
  - **UPDATE**: modifies one or more columns of data in a table or view    .
  - **DELETE**: removes one or more rows of data from a table or view    .
  - **MERGE**: combines the data from two tables and updates or inserts the result into a third table   .
  - **CALL**: executes a stored procedure or function  .
  - **EXPLAIN PLAN**: displays the execution plan of a SQL statement .
  - **LOCK TABLE**: locks one or more tables or views in a specified mode .
- DML statements can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT, to filter, aggregate, sort, and limit the data that is returned or affected  .
- DML statements can also use subqueries, joins, and set operators to combine data from multiple tables or views  .
- DML statements can be executed interactively using tools such as SQL*Plus or SQL Developer, or embedded in programs written in languages such as Java, C#, or Python .