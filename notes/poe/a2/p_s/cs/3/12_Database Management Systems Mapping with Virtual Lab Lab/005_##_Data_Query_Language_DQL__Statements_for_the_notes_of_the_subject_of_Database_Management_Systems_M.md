 Here is the content in markdown format for the topic -

## Data Query Language(DQL) Statements

Data Query Language(DQL) statements are used to retrieve data from the database. The primary DQL statements are -

1. SELECT - retrieves data from the database that matches criteria specified in the statement. It is the most commonly used DQL statement. The basic syntax is -

SELECT column1, column2, ...
FROM table_name;

We can specify additional criteria using WHERE clause, specify columns to group using GROUP BY clause, order the results using ORDER BY clause, etc.

Examples -

SELECT * FROM customers; // Retrieves all columns from customers table

SELECT name, age FROM students WHERE age > 20; // Retrieves name and age columns from students where age is more than 20

2. DESCRIBE - provides metadata about the table such as column names, data types, constraints, etc. The basic syntax is -

DESCRIBE table_name;

Example -

DESCRIBE products;

3. EXPLAIN - provides the execution plan for a given DQL statement. It shows the order of table access and types of access (full table scan, index scan, etc.). The basic syntax is -

EXPLAIN SELECT statement;

Example -

EXPLAIN SELECT * FROM customers WHERE age > 30;

Advantages of DQL -
- Retrieves required data from the database.
- Can filter and sort the data using WHERE and ORDER BY clauses.
- Can retrieve partial data using SELECT on specific columns.

Disadvantages -
- Data modifications are not possible. We cannot insert, update or delete data using DQL. We need to use DML for that.
- Aggregate functions can only be used on numeric data and some string data.