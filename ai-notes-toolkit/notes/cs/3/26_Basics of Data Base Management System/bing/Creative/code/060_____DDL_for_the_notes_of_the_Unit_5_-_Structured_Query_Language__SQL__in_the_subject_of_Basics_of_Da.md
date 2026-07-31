# DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- DDL stands for Data Definition Language, which is a subset of SQL commands that are used to create, modify, and delete database objects such as tables, views, indexes, and constraints .
- DDL commands are normally executed by database administrators or developers who need to define the structure and schema of the database.
- Some of the common DDL commands are :
  - CREATE: This command is used to create a new database object, such as a table, view, index, or constraint. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table named students with three columns: id, name, and age.
  - ALTER: This command is used to modify an existing database object, such as adding, dropping, or renaming columns, changing data types, or modifying constraints. For example, `ALTER TABLE students ADD email VARCHAR(100);` adds a new column named email to the students table.
  - DROP: This command is used to delete an existing database object, such as a table, view, index, or constraint. For example, `DROP TABLE students;` deletes the students table and all its data.
  - RENAME: This command is used to change the name of an existing database object, such as a table, view, index, or constraint. For example, `RENAME TABLE students TO pupils;` changes the name of the students table to pupils.
  - TRUNCATE: This command is used to delete all the data from an existing table, but not the table itself. For example, `TRUNCATE TABLE students;` removes all the rows from the students table, but keeps the table structure and schema.
- DDL commands are different from DML (Data Manipulation Language) commands, which are used to insert, update, delete, and query data from the database. DML commands affect the data, while DDL commands affect the structure and schema of the database.