### Manipulating data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- SQL stands for Structured Query Language, which is a language for storing, manipulating, and retrieving data in relational database management systems.
- Oracle and MySQL are two popular relational database management systems that use SQL as their standard database language.
- Data manipulation language (DML) is a subset of SQL that allows users to add, change, and delete data in the database tables .
- DML statements include INSERT, UPDATE, DELETE, and MERGE .
- A transaction is a sequence of one or more DML statements that are treated as a unit by the database system. A transaction can either be committed (applied to the database) or rolled back (undone) as a whole.
- Oracle and MySQL have some differences in their syntax and features for DML statements, such as:
  - Oracle supports the MERGE statement, which can insert or update data based on a condition, while MySQL does not .
  - MySQL supports the REPLACE statement, which can insert or delete and insert data based on a condition, while Oracle does not.
  - Oracle uses the dual table as a dummy table for queries that do not require a table name, while MySQL does not.
  - MySQL supports the LIMIT clause, which can limit the number of rows returned or affected by a query, while Oracle does not .
  - Oracle and MySQL have different ways of handling NULL values, date and time formats, and string concatenation .