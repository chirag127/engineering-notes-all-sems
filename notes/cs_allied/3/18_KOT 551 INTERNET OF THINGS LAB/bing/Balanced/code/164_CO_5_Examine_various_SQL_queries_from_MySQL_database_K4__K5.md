# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and it is a standard language for accessing and manipulating data in relational databases. MySQL is an open-source relational database management system that uses SQL as its query language. SQL queries are expressions that define the set of data to be retrieved from the database. SQL queries can be classified into five types based on their purpose and syntax:

- DDL (Data Definition Language): These are queries that create, alter, rename, drop, or truncate the physical structure of the tables in the database. For example, `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, etc.
- DML (Data Manipulation Language): These are queries that insert, update, delete, or select the data in the tables. For example, `INSERT INTO`, `UPDATE`, `DELETE`, `SELECT`, etc.
- DCL (Data Control Language): These are queries that grant or revoke permissions and roles to users or groups. For example, `GRANT`, `REVOKE`, etc.
- TCL (Transaction Control Language): These are queries that control the transactions in the database, such as committing or rolling back the changes. For example, `COMMIT`, `ROLLBACK`, `SAVEPOINT`, etc.
- DQL (Data Query Language): These are queries that retrieve data from the database based on certain conditions and filters. For example, `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`, etc.

To write SQL queries in MySQL, one needs to have a database management application (such as MySQL Workbench, Sequel Pro, etc.) and connect to the database. Then, one needs to understand the database schema and the fields in the tables. Finally, one can write SQL queries in the query editor and execute them to see the results.

Some examples of SQL queries in MySQL are:

- To create a database named `db1`:

```sql
CREATE DATABASE db1;
```

- To use the database `db1`:

```sql
USE db1;
```

- To create a table named `students` with four columns: `id`, `name`, `age`, and `grade`:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT,
  grade CHAR(1)
);
```

- To insert a record into the `students` table:

```sql
INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
```

- To update the `grade` of the student with `id` 1 to 'B':

```sql
UPDATE students SET grade = 'B' WHERE id = 1;
```

- To delete the record of the student with `id` 1 from the `students` table:

```sql
DELETE FROM students WHERE id = 1;
```

- To select all the records from the `students` table:

```sql
SELECT * FROM students;
```

- To select only the `name` and `grade` of the students who are older than 18:

```sql
SELECT name, grade FROM students WHERE age > 18;
```

- To select the average age of the students grouped by their grade:

```sql
SELECT grade, AVG(age) FROM students GROUP BY grade;
```

- To select the name and grade of the students who have the highest grade in the table:

```sql
SELECT name, grade FROM students WHERE grade = (SELECT MAX(grade) FROM students);
```

- To select the first 10 records from the `students` table in descending order of their age:

```sql
SELECT * FROM students ORDER BY age DESC LIMIT 10;
```

These are some of the basic SQL queries that can be used to manipulate and retrieve data from a MySQL database. For more advanced queries and functions, one can refer to the official MySQL documentation or online tutorials.