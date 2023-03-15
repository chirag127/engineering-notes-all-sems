# Basic Operations – Selection and Projection

- Selection and projection are two unary operations in relational algebra that are used to manipulate data in a relational database.
- Selection operation targets records (rows) or specific entities in a relational database. It filters the rows that satisfy a given condition or predicate.
- Projection operation targets attributes (columns) or specific properties in a relational database. It selects the columns that are specified in the query.
- In SQL, the SELECT statement combines both selection and projection operations in a single statement. The WHERE clause is used for selection and the column names are used for projection.
- Examples of selection and projection operations in SQL:

  - Select all the rows and columns from a table named Employees:

    ```sql
    SELECT * FROM Employees;
    ```

  - Select only the rows where the salary is greater than 5000 from a table named Employees:

    ```sql
    SELECT * FROM Employees WHERE salary > 5000;
    ```

  - Select only the columns name and department from a table named Employees:

    ```sql
    SELECT name, department FROM Employees;
    ```

  - Select only the rows where the department is 'Sales' and only the columns name and salary from a table named Employees:

    ```sql
    SELECT name, salary FROM Employees WHERE department = 'Sales';
    ```