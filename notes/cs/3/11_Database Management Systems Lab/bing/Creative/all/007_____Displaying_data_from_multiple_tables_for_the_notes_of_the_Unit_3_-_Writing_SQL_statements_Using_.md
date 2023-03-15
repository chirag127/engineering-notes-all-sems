# Displaying data from multiple tables

- One of the main features of SQL is the ability to query data from multiple tables and combine the results into a single result set.
- This is useful for retrieving related information from different sources and presenting a comprehensive view of the data.
- There are different ways to display data from multiple tables using SQL statements, such as:
  - Joining columns in two or more tables
  - Merging data from multiple tables into a single column
  - Creating a subquery to retrieve data from more than one table
  - Using set operators to combine result sets from different queries

## Joining columns in two or more tables

- A join is a SQL operation that allows you to combine data from two or more tables based on a common column or condition.
- The common column is usually a primary key in one table and a foreign key in another table, which establishes a relationship between the tables.
- There are different types of joins, such as:
  - Inner join: returns only the rows that match the join condition in both tables.
  - Left join: returns all the rows from the left table and the matching rows from the right table, or NULL if there is no match.
  - Right join: returns all the rows from the right table and the matching rows from the left table, or NULL if there is no match.
  - Full join: returns all the rows from both tables, regardless of whether they match the join condition or not.
  - Cross join: returns the Cartesian product of the rows from both tables, which means every row from the left table is paired with every row from the right table.
- The syntax for joining tables in SQL is:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition;
```

- For example, if we have two tables, `employees` and `departments`, and we want to display the employee name, department name, and salary for each employee, we can use an inner join as follows:

```sql
SELECT e.name, d.name, e.salary
FROM employees e
JOIN departments d
ON e.department_id = d.id;
```

- The result would look something like this:

| name | name | salary |
| --- | --- | --- |
| Alice | Sales | 5000 |
| Bob | Marketing | 4000 |
| Charlie | IT | 6000 |
| David | HR | 3000 |

## Merging data from multiple tables into a single column

- Sometimes, we may want to display data from multiple tables into a single column, rather than multiple columns.
- This can be useful for concatenating values, aggregating data, or creating a list of values.
- To merge data from multiple tables into a single column, we can use the following techniques:
  - Concatenation operator: allows us to combine two or more values into a single string. The operator varies depending on the database system, but it is usually `||` or `+`.
  - Aggregate functions: allow us to perform calculations on a set of values and return a single value. Some common aggregate functions are `SUM`, `AVG`, `MIN`, `MAX`, `COUNT`, etc.
  - Subquery: allows us to nest a query inside another query and use the result as a value or a table. A subquery can be used in the `SELECT`, `FROM`, `WHERE`, `HAVING`, or `ORDER BY` clauses of the main query.
  - GROUP_CONCAT function: allows us to concatenate values from a group of rows into a single string, separated by a delimiter. This function is specific to MySQL and SQLite databases.
- For example, if we have two tables, `students` and `courses`, and we want to display the student name and the list of courses they are enrolled in, we can use a subquery and the `GROUP_CONCAT` function as follows:

```sql
SELECT s.name, 
(SELECT GROUP_CONCAT(c.name) FROM courses c WHERE c.student_id = s.id) AS courses
FROM students s;
```

- The result would look something like this:

| name | courses |
| --- | --- |
| Emma | Math, Physics, Chemistry |
| Noah | History, Geography, Literature |
| Olivia | Art, Music, Drama |
| Liam | Biology, Computer Science, Engineering |