### Restricting and sorting data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

In this section, we will learn about how to restrict and sort data in SQL statements using ORACLE /MYSQL. Restricting data helps in retrieving the data that we require, and sorting data helps in organizing the data in a particular order.

Below are some points that will help you understand how to use these techniques:

1. **Restricting Data:**
   - The `WHERE` clause is used to restrict data in SQL statements.
   - We can use various operators like `=`, `<`, `>`, `<=`, `>=`, `<>`, `LIKE`, `BETWEEN`, `IN`, `NOT IN`, etc. in the `WHERE` clause to filter the data.
   - We can also use logical operators like `AND`, `OR`, `NOT` to combine multiple conditions in the `WHERE` clause.
   - Example: `SELECT * FROM employees WHERE salary > 50000 AND department = 'IT';`

2. **Sorting Data:**
   - The `ORDER BY` clause is used to sort data in SQL statements.
   - We can use `ASC` for ascending order and `DESC` for descending order to sort the data.
   - We can sort the data on one or more columns.
   - Example: `SELECT * FROM employees ORDER BY salary DESC, last_name ASC;`

3. **Combining Restricting and Sorting Data:**
   - We can combine the `WHERE` and `ORDER BY` clauses to filter and sort data.
   - Example: `SELECT * FROM employees WHERE department = 'IT' ORDER BY salary DESC;`

4. **Limiting Data:**
   - We can use the `LIMIT` clause to limit the number of rows returned by a SQL statement.
   - This is useful when we want to see only a few rows from a large table.
   - Example: `SELECT * FROM employees LIMIT 10;`

By using these techniques, we can retrieve and organize the data in a way that is useful for us. It is essential to understand these concepts as they are used extensively in database management systems. Practice these techniques on sample data to improve your skills.