### Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union removes any duplicate rows from the combined result set.
- A union requires that the number, name, and data type of the columns in the SELECT queries are the same or compatible.
- A union can be used to combine data from different tables or views that have a similar structure or meaning.
- A union can be written as:

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION
SELECT column1, column2, ..., columnN FROM table2
UNION
...
UNION
SELECT column1, column2, ..., columnN FROM tableN;
```

- A union can also be modified with the ALL keyword to include duplicate rows in the result set. This can be written as:

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION ALL
SELECT column1, column2, ..., columnN FROM table2
UNION ALL
...
UNION ALL
SELECT column1, column2, ..., columnN FROM tableN;
```

- A union can be used to perform various tasks, such as:

  - Combining data from different sources or databases
  - Creating a summary report from multiple tables or views
  - Performing set operations such as intersection, difference, or union
  - Simplifying complex queries by breaking them into smaller parts
  - Enhancing query performance by reducing the number of joins or subqueries

- A union can be combined with other SQL clauses, such as ORDER BY, GROUP BY, HAVING, or WHERE, to further manipulate the result set. However, these clauses must be applied to the entire union, not to individual SELECT queries. For example:

```sql
SELECT name, salary FROM employees
UNION
SELECT name, income FROM freelancers
ORDER BY salary DESC;
```

- A union is different from a join, which compares columns from two tables to create result rows composed of columns from both tables. A union does not create individual rows from columns gathered from two tables, but concatenates result sets from two queries. For example:

```sql
-- This is a join
SELECT e.name, e.department, d.location FROM employees e
JOIN departments d ON e.department = d.name;

-- This is a union
SELECT name, department FROM employees
UNION
SELECT name, location FROM departments;
```

- A union is also different from a subquery, which is a query nested inside another query. A union is a set operator that combines multiple queries, while a subquery is a query component that can be used in various places, such as in the SELECT, FROM, or WHERE clauses. For example:

```sql
-- This is a subquery
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- This is a union
SELECT name, salary FROM employees
UNION
SELECT name, income FROM freelancers;
```

- A union is a powerful and versatile SQL operator that can be used to combine data from different sources, perform set operations, simplify complex queries, and enhance query performance. It is important to understand the syntax and rules of a union, as well as the differences between a union and other SQL concepts, such as joins and subqueries.