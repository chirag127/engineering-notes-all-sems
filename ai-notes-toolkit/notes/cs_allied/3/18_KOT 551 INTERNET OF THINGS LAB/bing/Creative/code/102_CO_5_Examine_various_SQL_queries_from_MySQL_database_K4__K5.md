# CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that supports SQL.
- SQL queries are statements that specify what data to retrieve, insert, update, delete, or manipulate from a database.
- SQL queries can be classified into four categories: Data Definition Language (DDL), Data Manipulation Language (DML), Data Query Language (DQL), and Data Control Language (DCL).
- DDL is used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, or constraints.
- DML is used to manipulate the data in the database, such as inserting, updating, deleting, or merging records.
- DQL is used to query or retrieve data from the database, such as selecting, joining, filtering, sorting, grouping, or aggregating data.
- DCL is used to control the access and security of the database, such as granting, revoking, or denying permissions or roles to users or groups.
- Some examples of SQL queries from MySQL database are:

```sql
-- DDL: Create a table named students with four columns: id, name, age, and grade
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT,
  grade CHAR(1)
);

-- DML: Insert three records into the students table
INSERT INTO students (id, name, age, grade) VALUES
(1, 'Alice', 18, 'A'),
(2, 'Bob', 19, 'B'),
(3, 'Charlie', 20, 'C');

-- DQL: Select all the records from the students table
SELECT * FROM students;

-- DQL: Select the name and grade of the students who are older than 18
SELECT name, grade FROM students WHERE age > 18;

-- DQL: Select the average age of the students grouped by grade
SELECT grade, AVG(age) AS average_age FROM students GROUP BY grade;

-- DCL: Grant select and update privileges on the students table to a user named user1
GRANT SELECT, UPDATE ON students TO user1;
```