Hello, I am Sydney, your AI assistant. I can help you with various SQL queries from MySQL database. Here is some content that you can use to study and learn from for exams.

# CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL as its query language.
- A SQL query is a statement that specifies what data to retrieve, modify, insert, delete, or update from a database.
- There are different types of SQL queries, such as DDL, DML, DCL, and TCL, that perform different functions on the database.

## DDL (Data Definition Language)
- DDL is used to define the structure of the database, such as tables, columns, constraints, indexes, views, etc.
- Some common DDL commands are:

  - CREATE: to create a new database object, such as a table or a view.
  - ALTER: to modify an existing database object, such as adding or dropping a column or a constraint.
  - DROP: to delete an existing database object, such as a table or a view.
  - RENAME: to change the name of an existing database object, such as a table or a column.
  - TRUNCATE: to remove all the data from a table, but not the table structure.

- Example of a DDL query:

  ```sql
  -- create a table called students with four columns: id, name, age, and grade
  CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT CHECK (age > 0),
    grade CHAR(1) DEFAULT 'A'
  );
  ```

## DML (Data Manipulation Language)
- DML is used to manipulate the data in the database, such as inserting, updating, deleting, or selecting data from tables or views.
- Some common DML commands are:

  - INSERT: to add new rows of data to a table or a view.
  - UPDATE: to modify existing rows of data in a table or a view.
  - DELETE: to remove existing rows of data from a table or a view.
  - SELECT: to retrieve data from a table or a view, optionally with filtering, sorting, grouping, or joining conditions.

- Example of a DML query:

  ```sql
  -- insert a new row of data into the students table
  INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'B');

  -- update the grade of the student with id 1 to 'A'
  UPDATE students SET grade = 'A' WHERE id = 1;

  -- delete the student with id 1 from the students table
  DELETE FROM students WHERE id = 1;

  -- select all the columns and rows from the students table
  SELECT * FROM students;
  ```

## DCL (Data Control Language)
- DCL is used to control the access and permissions of the database, such as granting or revoking privileges or roles to users or groups.
- Some common DCL commands are:

  - GRANT: to give a user or a group a specific privilege or role on a database object, such as SELECT, INSERT, UPDATE, DELETE, etc.
  - REVOKE: to take away a specific privilege or role from a user or a group on a database object, such as SELECT, INSERT, UPDATE, DELETE, etc.

- Example of a DCL query:

  ```sql
  -- grant the SELECT and INSERT privileges on the students table to the user Bob
  GRANT SELECT, INSERT ON students TO Bob;

  -- revoke the INSERT privilege on the students table from the user Bob
  REVOKE INSERT ON students FROM Bob;
  ```

## TCL (Transaction Control Language)
- TCL is used to manage the transactions in the database, such as committing or rolling back the changes made by a set of SQL queries.
- Some common TCL commands are:

  - COMMIT: to save the changes made by a set of SQL queries to the database permanently.
  - ROLLBACK: to undo the changes made by a set of SQL queries and restore the database to its previous state.
  - SAVEPOINT: to mark a point in a transaction that can be used to roll back to in case of an error.
  - SET TRANSACTION: to specify the characteristics of a transaction, such as isolation level, read-only or read-write mode, etc.

- Example of a TCL query:

  ```sql
  -- start a transaction