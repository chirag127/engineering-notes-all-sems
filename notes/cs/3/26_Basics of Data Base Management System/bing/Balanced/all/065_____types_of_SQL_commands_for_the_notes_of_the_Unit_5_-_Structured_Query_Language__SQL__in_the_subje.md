# Types of SQL Commands

SQL stands for Structured Query Language and it is a standard language for storing, manipulating and retrieving data in databases. SQL commands can be grouped into five broad categories based on their functionality:

- **Data Definition Language (DDL)**: These commands are used to create, modify or delete the database structure, such as tables, views, indexes, etc. Some examples of DDL commands are:

  - CREATE: This command is used to create a new table, view, index, etc. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a new table called students with three columns: id, name and age.
  - ALTER: This command is used to modify the existing database structure, such as adding, deleting or renaming columns, changing data types, etc. For example, `ALTER TABLE students ADD email VARCHAR(50);` adds a new column called email to the students table.
  - DROP: This command is used to delete an existing table, view, index, etc. For example, `DROP TABLE students;` deletes the students table and all its data.
  - RENAME: This command is used to rename an existing table, view, index, etc. For example, `RENAME TABLE students TO learners;` renames the students table to learners.
  - TRUNCATE: This command is used to delete all the data from an existing table, but not the table itself. For example, `TRUNCATE TABLE students;` deletes all the rows from the students table, but keeps the table structure.

- **Data Manipulation Language (DML)**: These commands are used to insert, update, delete or retrieve data from the database tables. Some examples of DML commands are:

  - INSERT: This command is used to insert new data into a table. For example, `INSERT INTO students (id, name, age, email) VALUES (1, 'Alice', 20, 'alice@example.com');` inserts a new row into the students table with the specified values.
  - UPDATE: This command is used to modify existing data in a table. For example, `UPDATE students SET age = 21 WHERE id = 1;` updates the age of the student with id 1 to 21.
  - DELETE: This command is used to delete existing data from a table. For example, `DELETE FROM students WHERE id = 1;` deletes the row with id 1 from the students table.
  - SELECT: This command is used to retrieve data from one or more tables. For example, `SELECT name, email FROM students WHERE age > 18;` retrieves the name and email of the students who are older than 18.

- **Data Query Language (DQL)**: This is another name for the SELECT command, which is used to query data from the database. DQL can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, etc. to filter, aggregate, sort or limit the data. For example, `SELECT name, COUNT(*) AS count FROM students GROUP BY name HAVING count > 1 ORDER BY count DESC LIMIT 10;` retrieves the name and number of students who have the same name, only for those who have more than one occurrence, sorted by the number of occurrences in descending order, and limited to the top 10 results.

- **Data Control Language (DCL)**: These commands are used to control the access and permissions of the database users and roles. Some examples of DCL commands are:

  - GRANT: This command is used to grant privileges or permissions to a user or role to perform certain actions on the database objects, such as tables, views, etc. For example, `GRANT SELECT, UPDATE ON students TO alice;` grants the SELECT and UPDATE privileges on the students table to the user alice.
  - REVOKE: This command is used to revoke or remove the privileges or permissions that were previously granted to a user or role. For example, `REVOKE UPDATE ON students FROM alice;` revokes the UPDATE privilege on the students table from the user alice.

- **Transaction Control Language (TCL)**: These commands are used to manage the transactions in the database, which are a set of logical operations that are performed as a single unit. Transactions ensure the consistency and integrity of the data by following the ACID properties (Atomicity, Consistency, Isolation, Durability). Some examples of TCL commands are:

  - BEGIN: This command is used to start a new transaction. For example, `