## Data Query Language(DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a component of SQL (Structured Query Language) that is used to retrieve and manipulate data in a relational database management system  .
- DQL statements are used to query the data contained in schema objects, such as tables, views, indexes, etc .
- The purpose of DQL is to get some schema relation based on the query passed to it, and to impose order upon it.
- The most common DQL statement is the SELECT statement, which allows you to specify the columns, tables, conditions, and order of the data you want to retrieve  .
- The syntax of the SELECT statement is as follows:

```sql
SELECT column1, column2, ...
FROM table1, table2, ...
WHERE condition1, condition2, ...
ORDER BY column1, column2, ...
```

- The SELECT statement can be used with various clauses and operators to perform complex queries, such as joining multiple tables, grouping and aggregating data, filtering and sorting data, etc  .
- Some examples of DQL statements are:

```sql
-- Select all the data from the employees table
SELECT * FROM employees;

-- Select the name and salary of the employees who work in the sales department
SELECT name, salary
FROM employees
WHERE department = 'sales';

-- Select the name and average salary of each department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- Select the name and salary of the employees who earn more than the average salary of their department
SELECT e.name, e.salary
FROM employees e
JOIN (
  SELECT department, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
) d
ON e.department = d.department
WHERE e.salary > d.avg_salary;

-- Select the name and salary of the top 10 highest paid employees
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 10;
```

- DQL statements can be executed using various tools and applications, such as command-line interfaces, graphical user interfaces, web browsers, etc .
- DQL statements can also be embedded in other programming languages, such as Java, Python, PHP, etc, to interact with the database from the application .