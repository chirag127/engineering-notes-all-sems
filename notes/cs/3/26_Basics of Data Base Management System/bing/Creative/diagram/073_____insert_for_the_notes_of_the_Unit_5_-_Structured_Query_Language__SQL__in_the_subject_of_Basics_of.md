Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes for the topic of Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System.

# Unit 5 - Structured Query Language (SQL)

## Introduction

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational database management systems (RDBMS).
- SQL was developed in the 1970s by IBM and has been adopted by many vendors such as Oracle, Microsoft, MySQL, PostgreSQL, etc.
- SQL can perform various tasks such as creating, querying, updating, deleting, and managing data and database objects.
- SQL is divided into several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).

## Data Definition Language (DDL)

- DDL is used to define the structure and schema of the database, such as tables, columns, constraints, indexes, views, etc.
- DDL commands include CREATE, ALTER, DROP, RENAME, and TRUNCATE.
- Examples of DDL commands are:

```sql
-- Create a table named Student with four columns: id, name, age, and major
CREATE TABLE Student (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age > 0),
  major VARCHAR(20)
);

-- Add a column named email to the Student table
ALTER TABLE Student ADD email VARCHAR(50) UNIQUE;

-- Delete the Student table
DROP TABLE Student;

-- Rename the Student table to Students
RENAME TABLE Student TO Students;

-- Delete all the data from the Students table
TRUNCATE TABLE Students;
```

## Data Manipulation Language (DML)

- DML is used to insert, update, delete, and retrieve data from the database tables.
- DML commands include INSERT, UPDATE, DELETE, and SELECT.
- Examples of DML commands are:

```sql
-- Insert a new record into the Students table
INSERT INTO Students (id, name, age, major, email) VALUES (1, 'Alice', 19, 'Computer Science', 'alice@example.com');

-- Update the age and major of the student with id 1
UPDATE Students SET age = 20, major = 'Data Science' WHERE id = 1;

-- Delete the student with id 1
DELETE FROM Students WHERE id = 1;

-- Retrieve all the records from the Students table
SELECT * FROM Students;

-- Retrieve the name and email of the students who are majoring in Data Science
SELECT name, email FROM Students WHERE major = 'Data Science';
```

## Data Control Language (DCL)

- DCL is used to control the access and permissions of the database users and roles.
- DCL commands include GRANT, REVOKE, and DENY.
- Examples of DCL commands are:

```sql
-- Create a user named Bob with password '1234'
CREATE USER Bob IDENTIFIED BY '1234';

-- Grant Bob the SELECT and UPDATE privileges on the Students table
GRANT SELECT, UPDATE ON Students TO Bob;

-- Revoke the UPDATE privilege from Bob on the Students table
REVOKE UPDATE ON Students FROM Bob;

-- Deny Bob the DELETE privilege on the Students table
DENY DELETE ON Students TO Bob;
```

## Data Query Language (DQL)

- DQL is used to query and analyze data from the database tables using various clauses, operators, functions, and keywords.
- DQL commands include SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT, JOIN, etc.
- Examples of DQL commands are:

```sql
-- Retrieve the name and age of the students who are older than 18 and sort them by age in descending order
SELECT name, age FROM Students WHERE age > 18 ORDER BY age DESC;

-- Retrieve the average age of the students for each major
SELECT major, AVG(age) FROM Students GROUP BY major;

-- Retrieve the name and email of the students who have the same major as Alice
SELECT s1.name, s1.email FROM Students s1 JOIN Students s2 ON s1.major = s2.major WHERE s2.name = 'Alice';

-- Retrieve the name and major of the first 10 students
SELECT name, major FROM Students LIMIT 10;
```