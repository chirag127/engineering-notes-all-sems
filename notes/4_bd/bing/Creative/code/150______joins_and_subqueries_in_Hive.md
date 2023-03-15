#### Joins and Subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Hive supports four types of joins: inner join, left outer join, right outer join, and full outer join.
- The syntax for joins in Hive is similar to SQL, except that Hive requires the join condition to be specified in the ON clause, not in the WHERE clause.
- For example, to join the table `employees` with the table `departments` on the column `dept_id`, the query would be:

```sql
SELECT e.name, e.salary, d.name AS department
FROM employees e
JOIN departments d
ON e.dept_id = d.id;
```

- Subqueries are used to nest one query inside another query, usually in the WHERE or HAVING clause.
- Hive supports subqueries only in the following contexts: IN, NOT IN, EXISTS, NOT EXISTS, and scalar subqueries in the SELECT clause.
- The syntax for subqueries in Hive is similar to SQL, except that Hive does not allow subqueries in the FROM clause.
- For example, to find the employees who have a higher salary than the average salary of their department, the query would be:

```sql
SELECT e.name, e.salary, d.name AS department
FROM employees e
JOIN departments d
ON e.dept_id = d.id
WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);
```