## Data Query Language(DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a component of SQL (Structured Query Language) that is used to retrieve and manipulate data in a relational database management system  .
- DQL statements are used to query the data contained in schema objects, such as tables, views, indexes, etc .
- The purpose of DQL is to get some schema relation based on the query passed to it, and to impose order upon it.
- The most common DQL statement is the SELECT statement, which allows you to select data from one or more tables or views, and apply various filters, joins, aggregations, and sorting options  .
- The syntax of the SELECT statement is as follows:

```sql
SELECT [DISTINCT] column_list
FROM table_list
[WHERE condition]
[GROUP BY column_list]
[HAVING condition]
[ORDER BY column_list [ASC | DESC]];
```

- The SELECT statement can also be used with subqueries, which are queries nested within another query, to perform complex operations on the data .
- Some examples of DQL statements are:

```sql
-- Select all the data from the employees table
SELECT * FROM employees;

-- Select the name and salary of the employees who work in the sales department
SELECT name, salary
FROM employees
WHERE department = 'sales';

-- Select the average salary of each department, and order the result by descending order of the average salary
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- Select the name and salary of the employees who earn more than the average salary of their department
SELECT name, salary
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = e.department);
```

- DQL is an essential part of SQL, as it allows you to access and manipulate the data stored in a database    .
- DQL is also the basis for other SQL commands, such as DML (Data Manipulation Language), which is used to insert, update, and delete data, and DCL (Data Control Language), which is used to grant and revoke permissions on the data  .
- DQL can be used with various database management systems, such as MySQL, Oracle, SQL Server, Postgres, etc .
- DQL can also be used with various tools and applications, such as virtual labs, which are online platforms that allow you to practice and learn SQL skills in a simulated environment.