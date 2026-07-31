# Restricting and Sorting Data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Restricting data means limiting the rows that are retrieved by a query based on some conditions.
- Sorting data means arranging the rows that are retrieved by a query in a specific order.
- Both restricting and sorting data can be done by using clauses in the SQL statement, such as WHERE, ORDER BY, and LIMIT.

## Restricting Data

- The WHERE clause is used to filter the rows that match a given condition or expression.
- The WHERE clause can be used with any SQL statement that returns rows, such as SELECT, UPDATE, or DELETE.
- The WHERE clause can contain single or multiple conditions, which can be combined with logical operators such as AND, OR, and NOT.
- The WHERE clause can also use comparison operators such as =, <, >, <=, >=, <>, LIKE, IN, BETWEEN, and IS NULL to compare values.
- The WHERE clause can also use functions, subqueries, and variables to evaluate conditions.

### Examples of Restricting Data

- To display the name and salary of all employees whose salary is not in the range of $10,000 to $15,000, we can use the following query in MySQL:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000;
```

- To display the name and department of all employees who work in either department 10 or 20, we can use the following query in Oracle:

```sql
SELECT first_name, last_name, department_id
FROM employees
WHERE department_id IN (10, 20);
```

- To display the name and hire date of all employees who were hired in the year 2020, we can use the following query in Oracle:

```sql
SELECT first_name, last_name, hire_date
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 2020;
```

## Sorting Data

- The ORDER BY clause is used to sort the rows that are retrieved by a query in ascending or descending order.
- The ORDER BY clause can be used with any SQL statement that returns rows, such as SELECT or UNION.
- The ORDER BY clause can sort the rows by one or more columns or expressions, which can be specified by name, alias, or position.
- The ORDER BY clause can also use the ASC or DESC keywords to specify the sort order for each column or expression. The default order is ascending.
- The ORDER BY clause can also use the NULLS FIRST or NULLS LAST keywords to specify how null values are treated in the sort order.

### Examples of Sorting Data

- To display the name and salary of all employees in descending order of salary, we can use the following query in MySQL:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;
```

- To display the name and department of all employees in ascending order of department and then in descending order of name, we can use the following query in Oracle:

```sql
SELECT first_name, last_name, department_id
FROM employees
ORDER BY department_id ASC, last_name DESC;
```

- To display the name and hire date of all employees in ascending order of hire date and then in ascending order of name, with null values last, we can use the following query in Oracle:

```sql
SELECT first_name, last_name, hire_date
FROM employees
ORDER BY hire_date ASC NULLS LAST, first_name ASC;
```

## Limiting Rows

- The LIMIT clause is used to limit the number of rows that are retrieved by a query to a specified range.
- The LIMIT clause can be used with any SQL statement that returns rows, such as SELECT or UNION.
- The LIMIT clause can specify the offset and the count of the rows to be retrieved, or the percentage of the rows to be retrieved.
- The LIMIT clause can also use the WITH TIES option to include additional rows that have the same values as the last row in the result set.

### Examples of Limiting Rows

- To display the name and salary of the top 5 highest paid employees, we can use the following query in MySQL:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

- To display the name and department of the employees from the 11th to the 20th position in ascending order of department, we can use the following query in Oracle:

```sql
SELECT first

```
