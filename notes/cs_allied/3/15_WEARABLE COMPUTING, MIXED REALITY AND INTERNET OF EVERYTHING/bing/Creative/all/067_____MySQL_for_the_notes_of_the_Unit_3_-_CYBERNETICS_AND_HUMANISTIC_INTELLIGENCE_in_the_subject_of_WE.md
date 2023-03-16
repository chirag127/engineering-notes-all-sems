# MySQL

MySQL is a relational database management system (RDBMS) that allows us to store, manipulate, and retrieve data in a structured way. MySQL is free, open-source, and widely used for various applications. In this section, we will learn some basic concepts and operations of MySQL.

## What is a database?

A database is a collection of related data that is organized in a logical way. A database can have one or more tables, which are the main units of data storage. A table consists of rows and columns, where each row represents a record and each column represents a field or an attribute of the record. For example, a table named `students` can store information about students, such as their names, IDs, majors, and grades.

## How to create a database?

To create a database in MySQL, we need to use the `CREATE DATABASE` statement, followed by the name of the database. For example, to create a database named `school`, we can use the following statement:

```sql
CREATE DATABASE school;
```

We can also specify some options for the database, such as the character set and the collation. For example, to create a database named `school` with the UTF-8 character set and the case-insensitive collation, we can use the following statement:

```sql
CREATE DATABASE school
CHARACTER SET utf8
COLLATE utf8_general_ci;
```

## How to use a database?

To use a database in MySQL, we need to select it with the `USE` statement, followed by the name of the database. For example, to use the `school` database, we can use the following statement:

```sql
USE school;
```

We can also check which database is currently in use with the `SELECT DATABASE()` function. For example, to display the name of the current database, we can use the following statement:

```sql
SELECT DATABASE();
```

## How to create a table?

To create a table in MySQL, we need to use the `CREATE TABLE` statement, followed by the name of the table and the definition of the columns. For example, to create a table named `students` with four columns: `id`, `name`, `major`, and `grade`, we can use the following statement:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  major VARCHAR(50),
  grade DECIMAL(3,2) CHECK (grade BETWEEN 0 AND 10)
);
```

We can also specify some constraints for the columns, such as the primary key, the not null, the check, the unique, and the foreign key. These constraints help to ensure the validity and integrity of the data. For example, in the above statement, we have specified that the `id` column is the primary key, which means that it must be unique and not null for each record. We have also specified that the `name` column is not null, which means that it must have a value for each record. We have also specified that the `grade` column must be between 0 and 10 with the check constraint.

## How to insert data into a table?

To insert data into a table in MySQL, we need to use the `INSERT INTO` statement, followed by the name of the table and the values of the columns. For example, to insert a record into the `students` table, we can use the following statement:

```sql
INSERT INTO students (id, name, major, grade)
VALUES (1, 'Alice', 'Computer Science', 9.5);
```

We can also insert multiple records at once by using a comma-separated list of values. For example, to insert three records into the `students` table, we can use the following statement:

```sql
INSERT INTO students (id, name, major, grade)
VALUES (2, 'Bob', 'Mathematics', 8.0),
       (3, 'Charlie', 'Physics', 7.5),
       (4, 'David', 'Biology', 6.0);
```

## How to query data from a table?

To query data from a table in MySQL, we need to use the `SELECT` statement, followed by the columns and the table name. For example, to query all the columns and records from the `students` table, we can use the following statement:

```sql
SELECT * FROM students;
```

We can also specify some conditions for the query with the `WHERE` clause. For example, to query the records from the `students` table