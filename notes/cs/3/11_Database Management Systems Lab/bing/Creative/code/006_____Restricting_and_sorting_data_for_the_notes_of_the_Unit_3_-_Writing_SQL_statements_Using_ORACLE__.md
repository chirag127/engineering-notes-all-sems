### Restricting and Sorting Data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Restricting data means limiting the rows that are retrieved by a query based on some conditions.
- Sorting data means arranging the rows that are retrieved by a query in a specific order.
- Both restricting and sorting data can be done by using clauses in the SQL statement, such as WHERE, ORDER BY, LIMIT, ROWNUM, etc.
- Some examples of restricting and sorting data in ORACLE and MYSQL are:

  - To display the name and salary of employees whose salary is between 10000 and 15000, we can use the WHERE clause with the BETWEEN operator:

    ```sql
    SELECT first_name, last_name, salary
    FROM employees
    WHERE salary BETWEEN 10000 AND 15000;
    ```

  - To display the name and department of employees whose department is either 10 or 20, we can use the WHERE clause with the IN operator:

    ```sql
    SELECT first_name, last_name, department_id
    FROM employees
    WHERE department_id IN (10, 20);
    ```

  - To display the name and job of employees whose job is not 'SALESMAN', we can use the WHERE clause with the NOT operator:

    ```sql
    SELECT first_name, last_name, job_id
    FROM employees
    WHERE job_id <> 'SALESMAN';
    ```

  - To display the name and salary of employees in descending order of salary, we can use the ORDER BY clause with the DESC keyword:

    ```sql
    SELECT first_name, last_name, salary
    FROM employees
    ORDER BY salary DESC;
    ```

  - To display the name and salary of employees in ascending order of name and descending order of salary, we can use the ORDER BY clause with multiple columns and keywords:

    ```sql
    SELECT first_name, last_name, salary
    FROM employees
    ORDER BY first_name ASC, salary DESC;
    ```

  - To display the first 5 rows of the employees table, we can use the LIMIT clause in MYSQL or the ROWNUM pseudocolumn in ORACLE:

    ```sql
    -- MYSQL
    SELECT *
    FROM employees
    LIMIT 5;

    -- ORACLE
    SELECT *
    FROM employees
    WHERE ROWNUM <= 5;
    ```

  - To display the rows from 6 to 10 of the employees table, we can use the LIMIT clause with an offset in MYSQL or a subquery with ROWNUM in ORACLE:

    ```sql
    -- MYSQL
    SELECT *
    FROM employees
    LIMIT 5, 5;

    -- ORACLE
    SELECT *
    FROM (
      SELECT *, ROWNUM AS rn
      FROM employees
      ORDER BY employee_id
    )
    WHERE rn BETWEEN 6 AND 10;
    ```