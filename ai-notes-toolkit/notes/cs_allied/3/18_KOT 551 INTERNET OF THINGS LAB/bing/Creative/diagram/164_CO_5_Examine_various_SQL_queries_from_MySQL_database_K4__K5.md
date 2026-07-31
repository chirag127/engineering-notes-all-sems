# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational database management systems (RDBMS) such as MySQL . SQL queries are commands that are used to retrieve, insert, update, delete, or modify data from a table in a database .

There are different types of SQL queries, depending on the purpose and the complexity of the operation. Some of the common types of SQL queries are:

- DDL (Data Definition Language): These are queries that define the structure and schema of the database, such as creating, altering, renaming, dropping, or truncating tables. Examples of DDL commands are:

```sql
CREATE TABLE students (id INT, name VARCHAR(50), age INT);
ALTER TABLE students ADD COLUMN email VARCHAR(50);
RENAME TABLE students TO learners;
DROP TABLE learners;
TRUNCATE TABLE students;
```

- DML (Data Manipulation Language): These are queries that manipulate the data in the database, such as inserting, updating, deleting, or selecting records. Examples of DML commands are:

```sql
INSERT INTO students (id, name, age, email) VALUES (1, 'Alice', 20, 'alice@example.com');
UPDATE students SET age = 21 WHERE id = 1;
DELETE FROM students WHERE id = 1;
SELECT * FROM students;
```

- DCL (Data Control Language): These are queries that control the access and permissions of the database, such as granting or revoking privileges or roles. Examples of DCL commands are:

```sql
GRANT SELECT, UPDATE ON students TO user1;
REVOKE UPDATE ON students FROM user1;
```

- TCL (Transaction Control Language): These are queries that manage the transactions in the database, such as committing, rolling back, or saving changes. Examples of TCL commands are:

```sql
BEGIN TRANSACTION;
UPDATE students SET age = 22 WHERE id = 2;
COMMIT;
ROLLBACK;
SAVEPOINT sp1;
```

- DQL (Data Query Language): These are queries that query the data from the database, such as selecting, joining, filtering, grouping, or ordering records. Examples of DQL commands are:

```sql
SELECT name, age FROM students WHERE age > 18;
SELECT s.name, c.name FROM students s INNER JOIN courses c ON s.id = c.student_id;
SELECT name, COUNT(*) FROM students GROUP BY name;
SELECT * FROM students ORDER BY age DESC;
```

To write and execute SQL queries from a MySQL database, one needs to have a database management application (such as MySQL Workbench, Sequel Pro, etc.) and a connection to the database. Then, one can use the application's interface to write and run SQL queries, or use the command-line tool `mysql` to interact with the database.