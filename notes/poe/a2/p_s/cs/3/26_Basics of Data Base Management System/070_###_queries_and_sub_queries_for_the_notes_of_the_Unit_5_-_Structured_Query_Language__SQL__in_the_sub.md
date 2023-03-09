 Here are the notes for Queries and Subqueries for Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

### Queries

- A query is a question asked to the database to retrieve data.
- The SELECT statement is used to query the database and retrieve data from a table.
- The basic syntax of a SELECT query is -

SELECT column1, column2, ...
FROM table_name;

- We can retrieve all the columns from a table using -

SELECT * FROM table_name;

- We can filter the results using a WHERE clause in the SELECT statement. The WHERE clause is used to extract only those records that fulfill a specified condition.
- The basic syntax is -

SELECT column1, column2, ...
FROM table_name
WHERE condition;

- We can sort the retrieved data in ascending or descending order using the ORDER BY clause. The default order is ascending.
- The basic syntax is -

SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;

- We can get only unique values by using the DISTINCT keyword.
- The basic syntax is -

SELECT DISTINCT column1, column2, ...
FROM table_name;

- We can limit the number of results returned using the LIMIT clause.
- The basic syntax is -

SELECT column1, column2, ...
FROM table_name
LIMIT number;

[Detailed explanations and examples for the above points along with diagrams and codes can be included here if required.]