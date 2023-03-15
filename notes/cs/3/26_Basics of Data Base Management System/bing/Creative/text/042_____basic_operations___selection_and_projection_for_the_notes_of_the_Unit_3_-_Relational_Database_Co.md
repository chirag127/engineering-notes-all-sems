### Basic operations – selection and projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database  .
- Selection operation targets records (rows) or specific entities in a relational database. It filters the rows that satisfy a given condition or predicate .
- Projection operation targets attributes (columns) or specific properties in a relational database. It selects the columns that are specified in the query  .
- In SQL, the SELECT statement combines both selection and projection operations in a single statement.
- The syntax of the SELECT statement is as follows:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- The SELECT clause specifies the projection operation, i.e., the columns to be retrieved from the table.
- The FROM clause specifies the table name from which the data is to be retrieved.
- The WHERE clause specifies the selection operation, i.e., the condition or predicate to filter the rows.
- The SELECT * statement is a special case of the projection operation that returns all the columns in the table. It can also be used as a selection operation if no condition is specified.
- Examples of selection and projection operations in SQL are:

```sql
-- Selection operation: returns the rows where the salary is greater than 50000
SELECT * FROM employee WHERE salary > 50000;

-- Projection operation: returns the name and department columns of the employee table
SELECT name, department FROM employee;

-- Selection and projection operation: returns the name and department columns of the employee table where the salary is greater than 50000
SELECT name, department FROM employee WHERE salary > 50000;
```