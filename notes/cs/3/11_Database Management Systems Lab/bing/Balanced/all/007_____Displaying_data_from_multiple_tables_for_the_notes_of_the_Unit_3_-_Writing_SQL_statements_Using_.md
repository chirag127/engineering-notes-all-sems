# Displaying data from multiple tables

- In a relational database, data is stored in tables that are related to each other through common columns or keys.
- To display data from more than one table, we can use SQL statements that combine or join the tables based on the common columns.
- There are different types of joins that can be used to display data from multiple tables, such as inner join, outer join, cross join, self join, etc.
- The syntax for joining two tables in SQL is:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition;
```

- The join condition specifies how the tables are related to each other, usually by comparing the values of the common columns.
- The join type determines which rows from the tables are included in the result set, depending on whether they match the join condition or not.
- For example, an inner join returns only the rows that match the join condition, while an outer join returns all the rows from one table and the matching rows from the other table.
- To display data from more than two tables, we can use multiple join clauses in the SQL statement, such as:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition1
JOIN table3
ON join_condition2;
```

- The join clauses are evaluated from left to right, so the order of the tables and the join conditions may affect the result set.
- Alternatively, we can use subqueries to display data from multiple tables. A subquery is a query that is nested inside another query, usually in the WHERE or HAVING clause.
- A subquery can return a single value, a row, a column, or a table, depending on the context of the main query.
- For example, we can use a subquery to display the names of the employees who work in the same department as a given employee, such as:

```sql
SELECT name
FROM employee
WHERE department_id = (
  SELECT department_id
  FROM employee
  WHERE name = 'John Smith'
);
```

- The subquery returns the department_id of John Smith, and the main query returns the names of the employees who have the same department_id.
- Subqueries can also be used in the SELECT or FROM clauses of the main query, but they must be given an alias to refer to them.
- For example, we can use a subquery to display the average salary of each department, such as:

```sql
SELECT d.name, s.avg_salary
FROM department d
JOIN (
  SELECT department_id, AVG(salary) AS avg_salary
  FROM employee
  GROUP BY department_id
) s
ON d.id = s.department_id;
```

- The subquery returns a table with two columns: department_id and avg_salary. The main query joins this table with the department table and displays the name and average salary of each department. The subquery is given an alias s to refer to it in the join clause.