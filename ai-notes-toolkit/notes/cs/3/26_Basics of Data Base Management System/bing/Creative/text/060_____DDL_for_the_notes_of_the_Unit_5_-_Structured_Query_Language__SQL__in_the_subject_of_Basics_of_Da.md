### DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

- DDL stands for Data Definition Language, which is a subset of SQL commands that can be used to create, modify, and delete the structure of database objects, such as tables, views, indexes, etc.
- DDL commands do not affect the data stored in the database, but only the schema or the definition of the database objects.
- Some of the common DDL commands are:
  - CREATE: This command is used to create a new database object, such as a table, a view, an index, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table named students with three columns: id, name, and age.
  - ALTER: This command is used to modify an existing database object, such as adding, dropping, or renaming a column, changing the data type of a column, adding or dropping a constraint, etc. For example, `ALTER TABLE students ADD email VARCHAR(50);` adds a new column named email to the students table.
  - DROP: This command is used to delete an existing database object, such as a table, a view, an index, etc. For example, `DROP TABLE students;` deletes the students table and all the data stored in it.
  - RENAME: This command is used to change the name of an existing database object, such as a table, a view, an index, etc. For example, `RENAME TABLE students TO learners;` changes the name of the students table to learners.
  - TRUNCATE: This command is used to delete all the data from an existing table, but not the table itself. For example, `TRUNCATE TABLE students;` deletes all the rows from the students table, but keeps the table structure intact.
- DDL commands are normally executed by the database administrator or the developer, who should have the appropriate permissions to create, alter, or delete the database objects.