### Restricting and sorting data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Restricting data means limiting the rows that are retrieved by a SQL query based on some conditions.
- Sorting data means arranging the rows that are retrieved by a SQL query in a specific order.
- Restricting and sorting data are important tasks for data analysis and presentation.

#### Restricting data in ORACLE / MYSQL

- To restrict data in ORACLE / MYSQL, we can use the `WHERE` clause in a SQL query.
- The `WHERE` clause can contain single or multiple conditions to filter the data as per user needs.
- The conditions can use comparison operators, logical operators, arithmetic operators, and functions to specify the criteria for selecting rows.
- For example, to display the name and salary of employees who earn more than 5000, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 5000;
```

- To combine multiple conditions, we can use the `AND`, `OR`, and `NOT` operators.
- For example, to display the name and salary of employees who earn more than 5000 and work in department 10, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 5000 AND department_id = 10;
```

- To negate a condition, we can use the `NOT` operator.
- For example, to display the name and salary of employees who do not work in department 10, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE NOT department_id = 10;
```

- To check if a value is in a list of values, we can use the `IN` operator.
- For example, to display the name and salary of employees who work in department 10, 20, or 30, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE department_id IN (10, 20, 30);
```

- To check if a value matches a pattern, we can use the `LIKE` operator with wildcard characters (`%` and `_`).
- For example, to display the name and salary of employees whose first name starts with 'A', we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE first_name LIKE 'A%';
```

- To check if a value is null, we can use the `IS NULL` operator.
- For example, to display the name and salary of employees who do not have a manager, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE manager_id IS NULL;
```

#### Sorting data in ORACLE / MYSQL

- To sort data in ORACLE / MYSQL, we can use the `ORDER BY` clause in a SQL query.
- The `ORDER BY` clause can specify one or more columns to sort the data by, and the order can be ascending (`ASC`) or descending (`DESC`).
- The default order is ascending if not specified.
- For example, to display the name and salary of employees in ascending order of salary, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary ASC;
```

- To sort data by multiple columns, we can specify the columns in the order of precedence, separated by commas.
- For example, to display the name and salary of employees in ascending order of department id, and then in descending order of salary within each department, we can write:

```sql
SELECT first_name, last_name, salary, department_id
FROM employees
ORDER BY department_id ASC, salary DESC;
```

- To sort data by expressions or functions, we can use them in the `ORDER BY` clause.
- For example, to display the name and salary of employees in ascending order of their annual salary (assuming 12 months), we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary * 12 ASC;
```

- To sort data by custom criteria, we can use the `CASE` expression in the `ORDER BY` clause.
- For example, to display the name and salary of employees in ascending order of their first name, but with 'John' always at the top, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY CASE WHEN first

```
