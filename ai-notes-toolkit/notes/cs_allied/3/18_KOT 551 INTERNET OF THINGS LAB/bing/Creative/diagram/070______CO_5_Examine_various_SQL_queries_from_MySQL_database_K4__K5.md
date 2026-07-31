#### CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on the data.

Some of the objectives of this topic are:

- To understand the basic syntax and structure of SQL queries.
- To learn how to create, use, and drop databases and tables in MySQL.
- To learn how to insert, update, delete, and select data from tables in MySQL.
- To learn how to use various clauses, operators, functions, and keywords in SQL queries to filter, sort, group, and aggregate data in MySQL.
- To learn how to join multiple tables and perform subqueries and nested queries in MySQL.

Some of the key concepts and terms of this topic are:

- Database: A collection of related data organized in a structured way.
- Table: A set of data elements arranged in rows and columns in a database.
- Column: A vertical group of data elements of the same type in a table.
- Row: A horizontal group of data elements that represent a single record in a table.
- Primary key: A column or a combination of columns that uniquely identifies each row in a table.
- Foreign key: A column or a combination of columns that references the primary key of another table to establish a relationship between the tables.
- Query: An expression that defines the set of data to be retrieved from the database.
- Statement: A complete SQL command that ends with a semicolon (;).
- Clause: A part of a SQL statement that specifies a condition or an action.
- Operator: A symbol that performs a logical or mathematical operation on one or more values.
- Function: A predefined or user-defined routine that performs a specific task on one or more values and returns a result.
- Keyword: A reserved word that has a special meaning and purpose in SQL.

Some of the examples of SQL queries from MySQL database are:

- To create a database named `db1`:

```sql
CREATE DATABASE db1;
```

- To use the database `db1`:

```sql
USE db1;
```

- To create a table named `students` with four columns: `id` (primary key), `name`, `age`, and `grade`:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  grade CHAR(1)
);
```

- To insert a row into the table `students` with the values: `1`, `Alice`, `20`, and `A`:

```sql
INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 20, 'A');
```

- To update the `grade` of the student with `id` = `1` to `B`:

```sql
UPDATE students SET grade = 'B' WHERE id = 1;
```

- To delete the row from the table `students` where `id` = `1`:

```sql
DELETE FROM students WHERE id = 1;
```

- To select all the columns and rows from the table `students`:

```sql
SELECT * FROM students;
```

- To select only the `name` and `grade` columns from the table `students` where `age` is greater than `18` and sort the result by `grade` in descending order:

```sql
SELECT name, grade FROM students WHERE age > 18 ORDER BY grade DESC;
```

- To select the average `age` of the students grouped by `grade`:

```sql
SELECT grade, AVG(age) FROM students GROUP BY grade;
```

- To create another table named `courses` with three columns: `code` (primary key), `title`, and `credits`:

```sql
CREATE TABLE courses (
  code VARCHAR(10) PRIMARY KEY,
  title VARCHAR(100),
  credits INT
);
```

- To create a third table named `enrollments` with three columns: `student_id` (foreign key), `course_code` (foreign key), and `semester`:

```sql
CREATE TABLE enrollments (
  student_id INT,
  course_code VARCHAR(10),
  semester VARCHAR(20),
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_code) REFERENCES courses(code)
);
```

- To join the tables `students`, `courses`, and `enrollments` and select the `name`, `