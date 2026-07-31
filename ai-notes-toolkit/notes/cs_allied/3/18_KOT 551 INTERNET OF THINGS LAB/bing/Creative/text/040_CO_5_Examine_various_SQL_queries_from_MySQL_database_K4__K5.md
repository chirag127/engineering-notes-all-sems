# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for manipulating and querying data in relational databases. MySQL is an open-source relational database management system that supports SQL. In this section, we will examine some of the basic and commonly used SQL queries from MySQL database.

## SQL Queries

A SQL query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. You can think of a SQL query as a question you sent to the database; after that, you expect the database will respond to the question by sending back the data. The best way to learn SQL is by practicing with interactive SQL courses or online SQL editors.

The basic syntax of a SQL query is:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

The `SELECT` clause specifies which columns of data you want to retrieve from the table. You can use `*` to select all columns. The `FROM` clause specifies which table you want to query from. The `WHERE` clause specifies a condition that filters the rows of data. You can use logical operators such as `AND`, `OR`, and `NOT` to combine multiple conditions. You can also use comparison operators such as `=`, `<>`, `<`, `>`, `<=`, `>=`, `LIKE`, and `IN` to compare values. You can end a SQL query with a semicolon `;`.

For example, the following SQL query selects the name and age columns from the table `students` where the age is greater than 18.

```sql
SELECT name, age
FROM students
WHERE age > 18;
```

## Types of SQL Queries

There are different types of SQL queries based on the purpose and functionality. Some of the common types of SQL queries are:

- DDL (Data Definition Language): These are the queries that define the structure and schema of the database, such as creating, altering, renaming, dropping, and truncating tables. Some of the DDL commands are `CREATE`, `ALTER`, `RENAME`, `DROP`, and `TRUNCATE`.
- DML (Data Manipulation Language): These are the queries that manipulate the data in the database, such as inserting, updating, deleting, and selecting records. Some of the DML commands are `INSERT`, `UPDATE`, `DELETE`, and `SELECT`.
- DCL (Data Control Language): These are the queries that control the access and permissions of the database, such as granting and revoking privileges and roles. Some of the DCL commands are `GRANT` and `REVOKE`.
- TCL (Transaction Control Language): These are the queries that manage the transactions in the database, such as committing, rolling back, and saving changes. Some of the TCL commands are `COMMIT`, `ROLLBACK`, and `SAVEPOINT`.
- DQL (Data Query Language): These are the queries that query the data from the database, such as selecting, joining, grouping, and ordering data. Some of the DQL commands are `SELECT`, `JOIN`, `GROUP BY`, and `ORDER BY`.

## Examples of SQL Queries from MySQL Database

Here are some examples of SQL queries from MySQL database that demonstrate the different types of SQL queries.

- DDL: Create a table called `employees` with four columns: `id` (integer, primary key, auto-increment), `name` (varchar, not null), `salary` (decimal, not null), and `department` (varchar, not null).

```sql
CREATE TABLE employees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  salary DECIMAL(10,2) NOT NULL,
  department VARCHAR(50) NOT NULL
);
```

- DML: Insert three records into the table `employees` with the following values: (1, 'Alice', 5000.00, 'Sales'), (2, 'Bob', 6000.00, 'Marketing'), and (3, 'Charlie', 7000.00, 'IT').

```sql
INSERT INTO employees (id, name, salary, department)
VALUES (1, 'Alice', 5000.00, 'Sales'),
       (2, 'Bob', 6000.00, 'Marketing'),
       (3, 'Charlie', 7000.00, 'IT');
```

- DCL: Grant the `SELECT` and `UPDATE` privileges on the table `employees` to the