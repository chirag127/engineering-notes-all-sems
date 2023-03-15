Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Database Management System. Here is the content for the topic of Data Definition Language:

### Data Definition Language

- Data Definition Language (DDL) is a subset of SQL that is used to define and modify the structure of a database and its objects, such as tables, views, indexes, constraints, etc.
- DDL commands are executed by the database system to create, alter, or drop the database objects.
- Some of the common DDL commands are:

  - CREATE: This command is used to create a new database object, such as a table, view, index, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table named students with three columns: id, name, and age.
  - ALTER: This command is used to modify the structure or properties of an existing database object, such as adding, deleting, or renaming columns, changing data types, adding or dropping constraints, etc. For example, `ALTER TABLE students ADD email VARCHAR(50);` adds a new column named email to the students table.
  - DROP: This command is used to delete an existing database object, such as a table, view, index, etc. For example, `DROP TABLE students;` deletes the students table and all its data from the database.
  - RENAME: This command is used to change the name of an existing database object, such as a table, view, index, etc. For example, `RENAME TABLE students TO learners;` changes the name of the students table to learners.
  - TRUNCATE: This command is used to delete all the data from an existing table, but not the table itself. For example, `TRUNCATE TABLE students;` deletes all the rows from the students table, but the table structure remains intact.