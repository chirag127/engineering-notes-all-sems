Hello, I am Sydney, your AI assistant. I can help you with writing SQL statements using Oracle or MySQL. Here are some notes on the topic of displaying data from multiple tables.

### Displaying data from multiple tables

- To display data from multiple tables, you need to use a **join** operation, which combines rows from two or more tables based on a common column or condition.
- There are different types of joins, such as **inner join**, **outer join**, **cross join**, and **self join**. Each type of join has a different syntax and result.
- An **inner join** returns only the rows that match the join condition in both tables. For example, to display the employee name and department name for each employee, you can use an inner join between the employees and departments tables:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;
```

- An **outer join** returns all the rows that match the join condition, as well as the rows that do not match from one or both tables. There are three types of outer joins: **left outer join**, **right outer join**, and **full outer join**. For example, to display the employee name and department name for each employee, as well as the employees who do not belong to any department, you can use a left outer join:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT OUTER JOIN departments d
ON e.department_id = d.department_id;
```

- A **cross join** returns the Cartesian product of the rows from both tables, which means every row from one table is paired with every row from the other table. For example, to display the employee name and job title for every possible combination of employees and jobs, you can use a cross join:

```sql
SELECT e.first_name, e.last_name, j.job_title
FROM employees e
CROSS JOIN jobs j;
```

- A **self join** is a special type of join that joins a table to itself, using an alias to distinguish the two instances of the same table. For example, to display the employee name and manager name for each employee, you can use a self join:

```sql
SELECT e.first_name, e.last_name, m.first_name AS manager_first_name, m.last_name AS manager_last_name
FROM employees e
INNER JOIN employees m
ON e.manager_id = m.employee_id;
```

- To display data from more than two tables, you can use multiple join operations in the same query, using parentheses to specify the order of execution. For example, to display the employee name, department name, and location name for each employee, you can use a nested join:

```sql
SELECT e.first_name, e.last_name, d.department_name, l.location_name
FROM employees e
INNER JOIN (departments d
INNER JOIN locations l
ON d.location_id = l.location_id)
ON e.department_id = d.department_id;
```

- To display data from multiple tables without using a join operation, you can use a **subquery**, which is a query nested inside another query. A subquery can return a single value, a list of values, or a table of values. For example, to display the employee name and salary for the employees who work in the IT department, you can use a subquery:

```sql
SELECT e.first_name, e.last_name, e.salary
FROM employees e
WHERE e.department_id = (SELECT d.department_id
FROM departments d
WHERE d.department_name = 'IT');
```

- To display data from multiple tables using a **set operator**, you can use one of the following operators: **UNION**, **UNION ALL**, **INTERSECT**, or **MINUS**. A set operator combines the results of two or more queries into a single result set. For example, to display the employee name and job title for the employees who work in either the IT or the Sales department, you can use a union operator:

```sql
SELECT e.first_name, e.last_name, j.job_title
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
WHERE e.department_id = (SELECT d.department_id
FROM departments d
WHERE d.department_name = 'IT')
UNION
SELECT e.first_name, e.last_name, j.job_title
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id
WHERE e.department_id = (SELECT d.department_id
FROM departments d
WHERE d.department_name = 'Sales');
```

- To display data from multiple tables using a **pivot** operation, you can use