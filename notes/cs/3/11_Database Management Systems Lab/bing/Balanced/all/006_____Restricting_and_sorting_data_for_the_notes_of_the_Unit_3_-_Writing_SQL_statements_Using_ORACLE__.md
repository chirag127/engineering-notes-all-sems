# Restricting and Sorting Data for the Notes of the Unit 3 - Writing SQL Statements Using ORACLE /MYSQL in the Subject of Database Management Systems Lab

- Restricting data means limiting the rows that are retrieved by a query based on some conditions.
- Sorting data means arranging the rows that are retrieved by a query in a specific order.
- Both restricting and sorting data can be done by using clauses in the SQL statements.

## Restricting Data

- The WHERE clause is used to restrict data by specifying one or more conditions that the rows must satisfy to be selected.
- The WHERE clause can be used with SELECT, UPDATE, and DELETE statements.
- The WHERE clause can contain single or multiple conditions, which can be combined with logical operators such as AND, OR, and NOT.
- The WHERE clause can use various comparison operators, such as =, <, >, <=, >=, <>, !=, LIKE, BETWEEN, IN, and IS NULL.
- The WHERE clause can also use expressions, functions, subqueries, and pattern matching to filter data.

### Examples of Restricting Data

- To display the name and salary of all employees whose salary is not in the range of 10,000 to 15,000, use the following query:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000;
```

- To display the name and department of all employees who work in either department 10 or 20, use the following query:

```sql
SELECT first_name, last_name, department_id
FROM employees
WHERE department_id IN (10, 20);
```

- To display the name and job of all employees whose job starts with the letter 'S', use the following query:

```sql
SELECT first_name, last_name, job_id
FROM employees
WHERE job_id LIKE 'S%';
```

## Sorting Data

- The ORDER BY clause is used to sort data by specifying one or more columns or expressions to order the rows by.
- The ORDER BY clause can be used only with SELECT statements.
- The ORDER BY clause can use ASC (ascending) or DESC (descending) keywords to specify the sort order. The default order is ASC.
- The ORDER BY clause can use column aliases, column positions, or expressions to sort data.
- The ORDER BY clause can also use the NULLS FIRST or NULLS LAST keywords to specify how null values are treated in the sort order.

### Examples of Sorting Data

- To display the name and salary of all employees in descending order of salary, use the following query:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;
```

- To display the name and department of all employees in ascending order of department and then in descending order of name, use the following query:

```sql
SELECT first_name, last_name, department_id
FROM employees
ORDER BY department_id ASC, last_name DESC;
```

- To display the name and job of all employees in ascending order of the length of their job, use the following query:

```sql
SELECT first_name, last_name, job_id
FROM employees
ORDER BY LENGTH(job_id) ASC;
```

## SQL Row Limiting Clause

- The SQL row limiting clause is used to limit the number of rows that are retrieved by a query.
- The SQL row limiting clause can be used only with SELECT statements.
- The SQL row limiting clause can use the OFFSET and FETCH keywords to specify the starting row and the number of rows to fetch.
- The SQL row limiting clause can also use the PERCENT keyword to specify the percentage of rows to fetch.
- The SQL row limiting clause can also use the WITH TIES keyword to include additional rows that have the same sort key as the last row fetched.

### Examples of SQL Row Limiting Clause

- To display the name and salary of the top 5 highest paid employees, use the following query:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
FETCH FIRST 5 ROWS ONLY;
```

- To display the name and salary of the next 5 highest paid employees after skipping the first 10, use the following query:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
OFFSET 10 ROWS
FETCH NEXT 5 ROWS ONLY;
```

- To display the name and salary of the top 10 percent of employees, use the following query:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY