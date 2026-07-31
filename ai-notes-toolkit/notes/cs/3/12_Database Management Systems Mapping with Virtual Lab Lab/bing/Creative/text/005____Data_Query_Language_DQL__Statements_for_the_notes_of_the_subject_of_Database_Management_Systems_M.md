## Data Query Language(DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a component of SQL (Structured Query Language) that is used to retrieve and manipulate data in a relational database management system   .
- DQL statements are used to query the data contained in schema objects, such as tables, views, indexes, etc .
- The purpose of DQL is to get some schema relation based on the query passed to it, and to impose order upon it.
- The most common DQL statement is the SELECT statement, which allows you to specify the columns, tables, conditions, and order of the data you want to retrieve    .
- The syntax of the SELECT statement is as follows:

```sql
SELECT column1, column2, ...
FROM table1, table2, ...
WHERE condition1, condition2, ...
ORDER BY column1, column2, ... ASC|DESC;
```

- The SELECT statement can be used with various clauses and operators to perform complex queries, such as joins, subqueries, aggregations, functions, etc    .
- Some examples of DQL statements are:

```sql
-- Select all the data from the employees table
SELECT * FROM employees;

-- Select the name and salary of the employees who work in the sales department
SELECT name, salary
FROM employees
WHERE department = 'sales';

-- Select the name and average salary of each department
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- Select the name and salary of the employees who earn more than the average salary of their department
SELECT e.name, e.salary
FROM employees e
WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department = e.department);

-- Select the name and phone number of the customers who have placed orders in the last month
SELECT c.name, c.phone
FROM customers c
JOIN orders o
ON c.id = o.customer_id
WHERE o.date > DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
ORDER BY c.name;
```

- DQL statements are used to perform various tasks in a database, such as data analysis, reporting, data mining, etc   .
- DQL statements are also used to test and verify the data integrity and consistency in a database   .
- DQL statements are executed by the database engine, which parses, optimizes, and executes the query, and returns the result set to the user or application   .
- DQL statements can be written and executed using various tools and interfaces, such as command-line, graphical user interface, web browser, application programming interface, etc   .