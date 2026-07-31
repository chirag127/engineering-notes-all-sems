# CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to query, manipulate, and analyze data.
- SQL queries are commands that are used to retrieve, insert, update, delete, or modify data in a database .
- SQL queries can be classified into five types based on their purpose and functionality:
  - DDL (Data Definition Language): These are queries that define the structure and schema of the database, such as creating, altering, renaming, dropping, or truncating tables or databases. Examples of DDL commands are `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, etc.
  - DML (Data Manipulation Language): These are queries that manipulate the data in the database, such as inserting, updating, deleting, or selecting data from tables. Examples of DML commands are `INSERT INTO`, `UPDATE`, `DELETE`, `SELECT`, etc.
  - DCL (Data Control Language): These are queries that control the access and permissions of the data in the database, such as granting, revoking, or denying privileges to users or roles. Examples of DCL commands are `GRANT`, `REVOKE`, `DENY`, etc.
  - TCL (Transaction Control Language): These are queries that manage the transactions in the database, such as committing, rolling back, or saving the changes made by the queries. Examples of TCL commands are `COMMIT`, `ROLLBACK`, `SAVEPOINT`, etc.
  - DQL (Data Query Language): These are queries that query the data in the database, such as retrieving, filtering, sorting, grouping, or aggregating data from tables. Examples of DQL commands are `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, etc.
- To write SQL queries in MySQL, one needs to have a database management application (such as MySQL Workbench, Sequel Pro, etc.) that can connect to the MySQL server and execute the queries .
- The basic syntax of a SQL query in MySQL is as follows:

  ```sql
  SELECT column1, column2, ...
  FROM table_name
  WHERE condition
  GROUP BY column1, column2, ...
  HAVING condition
  ORDER BY column1, column2, ...
  LIMIT number;
  ```
- The `SELECT` clause specifies the columns or expressions to be retrieved from the table.
- The `FROM` clause specifies the table or tables from which to retrieve the data.
- The `WHERE` clause specifies the condition or criteria to filter the rows of the table.
- The `GROUP BY` clause specifies the columns or expressions to group the rows of the table by a common value.
- The `HAVING` clause specifies the condition or criteria to filter the groups of the table.
- The `ORDER BY` clause specifies the columns or expressions to sort the rows of the table in ascending or descending order.
- The `LIMIT` clause specifies the maximum number of rows to be returned by the query.
- The `;` symbol marks the end of the query.

- Here are some examples of SQL queries in MySQL :

  - To create a database named `students`:

    ```sql
    CREATE DATABASE students;
    ```

  - To create a table named `student_info` with four columns: `id`, `name`, `age`, and `grade`:

    ```sql
    CREATE TABLE student_info (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT,
      grade CHAR(1)
    );
    ```

  - To insert a new row into the `student_info` table with the values `1`, `Alice`, `18`, and `A`:

    ```sql
    INSERT INTO student_info (id, name, age, grade)
    VALUES (1, 'Alice', 18, 'A');
    ```

  - To update the `grade` column of the `student_info` table to `B` where the `id` is `1`:

    ```sql
    UPDATE student_info
    SET grade = 'B'
    WHERE id = 1;
    ```

  - To delete the row from the `student_info` table where the `id` is