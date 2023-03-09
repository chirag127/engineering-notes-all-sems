 Here are the notes for Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

### Structured Query Language (SQL)

- SQL is a standard language for accessing and manipulating databases.
- It is used to query, insert, update and modify data from a relational database.
- The basic syntax of SQL consists of:

SELECT - extracts data from the database
UPDATE - updates data in the database
DELETE - deletes data from the database
INSERT INTO - inserts new data into the database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table

- Some commonly used clauses in SQL queries are:

FROM - specifies the table to query
WHERE - specifies a condition for filtering records
AND, OR, NOT - used to combine conditions
ORDER BY - sorts the result-set in ascending or descending order
GROUP BY - groups rows by one or more columns
HAVING - used with GROUP BY to filter groups

- Examples of SQL queries:

SELECT * FROM customers; - retrieves all columns from customers table
SELECT name, age FROM customers; - retrieves specific columns from customers table
SELECT * FROM customers WHERE age > 30; - retrieves records where age is greater than 30
SELECT * FROM customers ORDER BY age; - retrieves records from customers table ordered by age

- Advantages of SQL:

Standard language - can be used with different databases
Simple and easy to learn
Performs tasks efficiently on large data
Powerful enough to handle complex queries

- Disadvantages of SQL:

Inefficient with recursive and hierarchical data
Not suitable for data mining tasks
May have compatibility issues between different database vendors

- Applications of SQL:

All major database systems use SQL
Widely used for data science, data analytics and business intelligence tasks
Used by developers and data analysts to interact with data
Run by DBA's for data administration tasks
Forms the basis for other database languages and modelling techniques