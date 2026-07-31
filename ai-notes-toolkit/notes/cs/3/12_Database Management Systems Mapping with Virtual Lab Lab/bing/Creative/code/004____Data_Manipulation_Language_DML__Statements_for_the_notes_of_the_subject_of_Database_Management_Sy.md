## Data Manipulation Language(DML) Statements

- Data manipulation language (DML) statements are used to access and manipulate data in existing schema objects, such as tables, views, or indexes  .
- DML statements can update, insert, delete, or select data from the database   .
- DML statements are part of a transaction, which is a sequence of one or more SQL statements that are treated as a unit by the database .
- A transaction can be committed, which means the changes made by the DML statements are made permanent in the database, or rolled back, which means the changes are undone and the database is restored to its previous state .
- The most common DML statements are:
  - `SELECT`, which retrieves data from the database based on specified criteria    .
  - `INSERT`, which adds new rows of data to a table    .
  - `UPDATE`, which modifies existing rows of data in a table    .
  - `DELETE`, which removes existing rows of data from a table    .
- Some other DML statements are:
  - `MERGE`, which combines the data from two tables into one table based on a matching condition  .
  - `CALL`, which executes a stored procedure or a function  .
  - `EXPLAIN PLAN`, which displays the execution plan of a SQL statement  .
  - `LOCK TABLE`, which locks one or more tables or views to prevent concurrent access by other users  .
- The syntax and usage of DML statements may vary depending on the database system and version .
- DML statements can be used in conjunction with other SQL statements, such as data definition language (DDL) statements, data control language (DCL) statements, or transaction control language (TCL) statements  .
- DML statements can also be embedded in other programming languages, such as Java, C#, or Python, to interact with the database  .