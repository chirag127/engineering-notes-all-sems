### Merging Data from Multiple Tables

- In relational databases, data is often stored in multiple tables that are related by foreign keys.
- To query data from multiple tables, we can use join operations that combine rows from two or more tables based on a common column value or condition.
- There are different types of joins, such as inner join, left join, right join, and full join, that produce different results depending on how they match the rows from the joined tables.
- Inner join returns only the rows that have matching values in both tables.
- Left join returns all the rows from the left table and the matching rows from the right table. If there is no match, the right table columns are filled with null values.
- Right join returns all the rows from the right table and the matching rows from the left table. If there is no match, the left table columns are filled with null values.
- Full join returns all the rows from both tables, regardless of whether they have matching values or not. If there is no match, the columns from the other table are filled with null values.
- To perform a join operation, we can use the JOIN keyword in the SQL statement, followed by the name of the table to join and the ON clause that specifies the join condition.
- For example, to join the table `employees` with the table `departments` based on the `department_id` column, we can write:

```sql
SELECT employees.name, employees.salary, departments.name AS department
FROM employees
JOIN departments
ON employees.department_id = departments.id;
```

- This query will return the name, salary, and department name of each employee who has a valid department id in the `employees` table.
- We can also use aliases for table names to make the query more concise and readable, such as:

```sql
SELECT e.name, e.salary, d.name AS department
FROM employees e
JOIN departments d
ON e.department_id = d.id;
```

- This query will produce the same result as the previous one, but using `e` and `d` as aliases for `employees` and `departments` respectively.
- We can also use different join types by specifying them after the JOIN keyword, such as:

```sql
SELECT e.name, e.salary, d.name AS department
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id;
```

- This query will return all the rows from the `employees` table, even if they do not have a matching department id in the `departments` table. In that case, the department column will be null.