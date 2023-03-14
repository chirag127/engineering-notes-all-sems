#### Joins and subqueries in Hive

- Joins are used to combine data from two or more tables based on a common column or condition.
- Subqueries are used to write a query within another query, usually to filter or aggregate data based on some criteria.
- Hive supports four types of joins: inner join, left outer join, right outer join, and full outer join.
- Hive also supports subqueries in the WHERE and HAVING clauses, but not in the SELECT or FROM clauses.
- The syntax for joins and subqueries in Hive is similar to SQL, with some differences and limitations.

##### Joins in Hive

- To perform a join in Hive, use the JOIN keyword followed by the table names and the join condition in the ON clause.
- For example, to join the table `employees` with the table `departments` based on the `dept_id` column, use:

```sql
SELECT e.name, d.name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;
```

- To specify the type of join, use the keywords INNER, LEFT OUTER, RIGHT OUTER, or FULL OUTER before the JOIN keyword.
- For example, to perform a left outer join, use:

```sql
SELECT e.name, d.name
FROM employees e
LEFT OUTER JOIN departments d
ON e.dept_id = d.dept_id;
```

- A left outer join returns all the rows from the left table, and the matching rows from the right table, or NULL if there is no match.
- A right outer join returns all the rows from the right table, and the matching rows from the left table, or NULL if there is no match.
- A full outer join returns all the rows from both tables, and NULL for the columns that do not match.
- An inner join returns only the rows that match in both tables.

##### Subqueries in Hive

- To perform a subquery in Hive, use the IN, NOT IN, EXISTS, NOT EXISTS, or ANY keywords in the WHERE or HAVING clause, followed by a nested query that returns a single column.
- For example, to filter the employees who work in the sales department, use:

```sql
SELECT name, salary
FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE name = 'Sales');
```

- The subquery returns the `dept_id` of the sales department, and the main query returns the name and salary of the employees who have that `dept_id`.
- To filter the employees who do not work in the sales department, use NOT IN instead of IN.
- To check if a subquery returns any rows, use EXISTS or NOT EXISTS.
- For example, to filter the departments that have no employees, use:

```sql
SELECT name
FROM departments
WHERE NOT EXISTS (SELECT * FROM employees WHERE employees.dept_id = departments.dept_id);
```

- The subquery returns all the rows from the employees table that match the `dept_id` of the departments table, and the main query returns the name of the departments that have no matching rows.
- To compare a value with the result of a subquery, use ANY or ALL keywords with a comparison operator.
- For example, to filter the employees who have a salary higher than any employee in the sales department, use:

```sql
SELECT name, salary
FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE dept_id IN (SELECT dept_id FROM departments WHERE name = 'Sales'));
```

- The subquery returns the salaries of the employees in the sales department, and the main query returns the name and salary of the employees who have a higher salary than any of those values.

##### Mnemonics and learning tricks for joins and subqueries in Hive

- To remember the types of joins, use the acronym FILR: Full, Inner, Left, Right.
- To remember the syntax for joins, use the mnemonic JOIN ON: Join the tables On the common column or condition.
- To remember the syntax for subqueries, use the mnemonic WHERE IN: Where the column is In the result of the subquery.