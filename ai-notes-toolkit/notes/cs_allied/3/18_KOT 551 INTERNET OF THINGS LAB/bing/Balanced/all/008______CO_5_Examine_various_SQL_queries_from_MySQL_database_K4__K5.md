#### CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular and widely used open-source relational database management systems (RDBMS) that supports SQL. 

To examine various SQL queries from MySQL database, one needs to:

- Have a database management application (such as MySQL Workbench, Sequel Pro, etc.) installed and connected to the MySQL server.
- Understand the database schema and its hierarchy, which consists of databases, tables, columns, rows, and values .
- Know the basic SQL syntax and keywords, such as SELECT, FROM, WHERE, GROUP BY, ORDER BY, etc. that define the data to be retrieved from the database .
- Write SQL queries in the database management application or in a text editor and execute them on the MySQL server to get the desired data .
- Analyze the results of the SQL queries and modify them as needed to get more specific or accurate data.

Some examples of SQL queries from MySQL database are:

- To create a database named db1:

```sql
CREATE DATABASE db1;
```

- To select and use the database db1:

```sql
USE db1;
```

- To create a table named students with four columns: id, name, age, and grade:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  grade CHAR(1)
);
```

- To insert a record into the students table:

```sql
INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
```

- To update the grade of the student with id 1 to 'B':

```sql
UPDATE students SET grade = 'B' WHERE id = 1;
```

- To delete the record of the student with id 1 from the students table:

```sql
DELETE FROM students WHERE id = 1;
```

- To select all the records from the students table:

```sql
SELECT * FROM students;
```

- To select only the name and grade of the students who are older than 18:

```sql
SELECT name, grade FROM students WHERE age > 18;
```

- To select the average age of the students grouped by grade and ordered by grade in descending order:

```sql
SELECT grade, AVG(age) FROM students GROUP BY grade ORDER BY grade DESC;
```

- To drop the table students:

```sql
DROP TABLE students;
```

- To drop the database db1:

```sql
DROP DATABASE db1;
```

These are some of the basic SQL queries from MySQL database. There are many more types and variations of SQL queries that can be used to perform different operations and functions on the data in MySQL database . One can learn more about SQL queries from MySQL by reading the official documentation, online tutorials, or books on SQL and MySQL.