#### CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on the data.

Some of the objectives of this topic are:

- To understand the basic syntax and structure of SQL queries.
- To learn how to create, use, and drop databases and tables in MySQL.
- To learn how to insert, update, delete, and select data from tables in MySQL.
- To learn how to use various clauses, operators, functions, and keywords in SQL queries to filter, sort, group, and aggregate data in MySQL.
- To learn how to join multiple tables and perform subqueries and nested queries in MySQL.

Some of the key points of this topic are:

- A SQL query is an expression that defines the set of data to be retrieved from the database. A SQL query consists of one or more keywords, clauses, operators, and identifiers that follow a specific syntax and order.
- A SQL query can be executed using a database management application (such as MySQL Workbench or Sequel Pro) or a command-line interface (such as mysql or mysqladmin).
- A database is a collection of related data organized in tables. A table is a structure that consists of rows and columns. A row is a record of data and a column is a field of data. A table can have one or more columns and zero or more rows.
- To create a database in MySQL, the CREATE DATABASE statement is used. For example, `CREATE DATABASE db1;` creates a database named db1.
- To use a database in MySQL, the USE statement is used. For example, `USE db1;` selects the database db1 as the current database.
- To drop a database in MySQL, the DROP DATABASE statement is used. For example, `DROP DATABASE db1;` deletes the database db1 and all its tables.
- To create a table in MySQL, the CREATE TABLE statement is used. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` creates a table named students with three columns: id, name, and age.
- To insert data into a table in MySQL, the INSERT INTO statement is used. For example, `INSERT INTO students (id, name, age) VALUES (1, 'Alice', 20);` inserts a row of data into the students table.
- To update data in a table in MySQL, the UPDATE statement is used. For example, `UPDATE students SET age = 21 WHERE id = 1;` updates the age of the student with id 1 to 21.
- To delete data from a table in MySQL, the DELETE FROM statement is used. For example, `DELETE FROM students WHERE id = 1;` deletes the row of data from the students table where id is 1.
- To select data from a table in MySQL, the SELECT statement is used. For example, `SELECT * FROM students;` selects all the data from the students table.
- To filter data from a table in MySQL, the WHERE clause is used. For example, `SELECT * FROM students WHERE age > 20;` selects the data from the students table where the age is greater than 20.
- To sort data from a table in MySQL, the ORDER BY clause is used. For example, `SELECT * FROM students ORDER BY name;` selects the data from the students table and sorts it by the name column in ascending order.
- To group data from a table in MySQL, the GROUP BY clause is used. For example, `SELECT age, COUNT(*) FROM students GROUP BY age;` selects the age and the number of students with that age from the students table and groups them by the age column.
- To aggregate data from a table in MySQL, various aggregate functions are used, such as SUM, AVG, MIN, MAX, COUNT, etc. For example, `SELECT AVG(age) FROM students;` selects the average age of the students from the students table.
- To join data from multiple tables in MySQL, various join types are used, such as INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, CROSS JOIN, etc. For example, `SELECT students.name, courses.name FROM students INNER JOIN courses ON students.id = courses.student_id;` selects the name of the students and the name of the courses they are enrolled in from the students and courses tables and joins them on the student_id column.
-