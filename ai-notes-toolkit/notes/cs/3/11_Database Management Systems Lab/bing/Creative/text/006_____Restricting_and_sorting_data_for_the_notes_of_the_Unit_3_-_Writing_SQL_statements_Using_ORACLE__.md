### Restricting and sorting data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Restricting data means limiting the rows that are retrieved by a SQL query based on some conditions.
- Sorting data means arranging the rows that are retrieved by a SQL query in a specific order.
- Restricting and sorting data are important tasks for data analysis and presentation.

#### Restricting data in ORACLE / MYSQL

- To restrict data in ORACLE / MYSQL, we can use the **WHERE** clause in a SQL query.
- The WHERE clause can contain single or multiple conditions to filter the data as per user needs.
- The conditions can be based on arithmetic, logical, comparison, or string operators.
- The conditions can be combined using **AND**, **OR**, or **NOT** keywords.
- The conditions can also use **IN**, **BETWEEN**, **LIKE**, or **NULL** keywords to check for membership, range, pattern, or absence of values.
- The syntax of the WHERE clause is:

```sql
SELECT column_list
FROM table_name
WHERE condition;
```

- For example, to display the name and salary of all employees whose salary is not in the range $10,000 through $15,000, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000;
```

#### Sorting data in ORACLE / MYSQL

- To sort data in ORACLE / MYSQL, we can use the **ORDER BY** clause in a SQL query.
- The ORDER BY clause can specify one or more columns to sort the data by.
- The ORDER BY clause can also specify the sort order as **ASC** (ascending) or **DESC** (descending) for each column.
- The default sort order is ascending if not specified.
- The syntax of the ORDER BY clause is:

```sql
SELECT column_list
FROM table_name
WHERE condition
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

- For example, to display the name and salary of all employees in descending order of salary, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;
```

#### Limiting rows in ORACLE / MYSQL

- To limit the number of rows that are retrieved by a SQL query, we can use different methods in ORACLE and MYSQL.
- In ORACLE, we can use the **ROWNUM** pseudocolumn to filter the rows based on their position in the result set.
- The ROWNUM pseudocolumn assigns a sequential number to each row starting from 1.
- The ROWNUM pseudocolumn can be used in the WHERE clause or the ORDER BY clause, but not in the SELECT list or the GROUP BY clause.
- The syntax of using ROWNUM is:

```sql
SELECT column_list
FROM table_name
WHERE ROWNUM <= n;
```

- For example, to display the name and salary of the top 5 highest paid employees, we can write:

```sql
SELECT first_name, last_name, salary
FROM (
  SELECT first_name, last_name, salary
  FROM employees
  ORDER BY salary DESC
)
WHERE ROWNUM <= 5;
```

- In MYSQL, we can use the **LIMIT** clause to specify the maximum number of rows to return from a SQL query.
- The LIMIT clause can also specify the offset to start from, which is 0 by default.
- The syntax of using LIMIT is:

```sql
SELECT column_list
FROM table_name
WHERE condition
ORDER BY column
LIMIT offset, count;
```

- For example, to display the name and salary of the top 5 highest paid employees, we can write:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;
```