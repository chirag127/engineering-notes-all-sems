# Unit 5 - Structured Query Language (SQL)

- SQL is a standard language for creating, manipulating, and querying data in relational databases.
- SQL consists of several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- SQL commands can be classified into four categories: DDL, DML, DCL, and DQL.

## Data Definition Language (DDL)

- DDL is used to define the structure and schema of the database, such as tables, views, indexes, constraints, etc.
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
ALTER TABLE Student
ADD email VARCHAR(50) UNIQUE;

-- Delete the Student table and its data
DROP TABLE Student;

-- Rename the Student table to Students
RENAME TABLE Student TO Students;

-- Delete all the data from the Students table but keep the table structure
TRUNCATE TABLE Students;
```

## Data Manipulation Language (DML)

- DML is used to insert, update, delete, and merge data in the database tables.
- DML commands include INSERT, UPDATE, DELETE, and MERGE.
- Examples of DML commands are:

```sql
-- Insert a new record into the Students table
INSERT INTO Students (id, name, age, major, email)
VALUES (1, 'Alice', 19, 'Computer Science', 'alice@example.com');

-- Update the age and email of the student with id 1
UPDATE Students
SET age = 20, email = 'alice@new.com'
WHERE id = 1;

-- Delete the record of the student with id 1
DELETE FROM Students
WHERE id = 1;

-- Merge the data from the NewStudents table into the Students table
MERGE INTO Students AS S
USING NewStudents AS N
ON S.id = N.id
WHEN MATCHED THEN
  UPDATE SET S.name = N.name, S.age = N.age, S.major = N.major, S.email = N.email
WHEN NOT MATCHED THEN
  INSERT (id, name, age, major, email) VALUES (N.id, N.name, N.age, N.major, N.email);
```

## Data Control Language (DCL)

- DCL is used to control the access and permissions of the database users and roles.
- DCL commands include GRANT, REVOKE, and DENY.
- Examples of DCL commands are:

```sql
-- Grant the SELECT and UPDATE privileges on the Students table to the user Bob
GRANT SELECT, UPDATE ON Students TO Bob;

-- Revoke the UPDATE privilege on the Students table from the user Bob
REVOKE UPDATE ON Students FROM Bob;

-- Deny the DELETE privilege on the Students table to the user Bob
DENY DELETE ON Students TO Bob;
```

## Data Query Language (DQL)

- DQL is used to retrieve and manipulate data from the database tables and views.
- DQL commands include SELECT, JOIN, GROUP BY, HAVING, ORDER BY, and LIMIT.
- Examples of DQL commands are:

```sql
-- Select all the columns and records from the Students table
SELECT * FROM Students;

-- Select the name and email of the students who are majoring in Computer Science
SELECT name, email FROM Students
WHERE major = 'Computer Science';

-- Select the name and major of the students who are older than 18 and sort them by name in ascending order
SELECT name, major FROM Students
WHERE age > 18
ORDER BY name ASC;

-- Select the name and age of the students who are younger than 20 and group them by age
SELECT name, age FROM Students
WHERE age < 20
GROUP BY age;

-- Select the average age of the students who are majoring in Computer Science and having an email ending with '.com'
SELECT AVG(age) FROM Students
WHERE major = 'Computer Science' AND email LIKE '%.com';

-- Select the first 10 records from the Students table
SELECT * FROM Students
LIMIT 10;
```