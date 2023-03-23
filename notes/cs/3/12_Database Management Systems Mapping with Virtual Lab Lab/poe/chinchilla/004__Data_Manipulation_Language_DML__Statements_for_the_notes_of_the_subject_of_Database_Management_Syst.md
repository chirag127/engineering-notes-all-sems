## Data Manipulation Language(DML) Statements

DML statements are used to modify the data in a database. These statements allow users to insert, update, delete, and retrieve data from a database. In this section, we will discuss the most commonly used DML statements.

### INSERT Statement

The INSERT statement is used to insert new data into a table. The syntax of the INSERT statement is as follows:

```sql
INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
```

Example:

```sql
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id, salary)
VALUES (1, 'John', 'Doe', 'johndoe@example.com', '2022-01-01', 'IT_PROG', 5000);
```

### UPDATE Statement

The UPDATE statement is used to modify existing data in a table. The syntax of the UPDATE statement is as follows:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

Example:

```sql
UPDATE employees SET salary = 6000 WHERE employee_id = 1;
```

### DELETE Statement

The DELETE statement is used to delete data from a table. The syntax of the DELETE statement is as follows:

```sql
DELETE FROM table_name WHERE condition;
```

Example:

```sql
DELETE FROM employees WHERE employee_id = 1;
```

### SELECT Statement

The SELECT statement is used to retrieve data from a table. The syntax of the SELECT statement is as follows:

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```

Example:

```sql
SELECT * FROM employees WHERE job_id = 'IT_PROG';
```

These are the most commonly used DML statements. In addition to these statements, there are other DML statements such as MERGE, UPSERT, and CALL, which are used in specific scenarios. Understanding these statements is essential for managing and manipulating data in a database.