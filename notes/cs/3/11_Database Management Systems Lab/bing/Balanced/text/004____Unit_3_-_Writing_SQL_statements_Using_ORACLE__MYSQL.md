## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- ORACLE and MYSQL are two popular relational database management systems (RDBMS) that use SQL as their query language.
- To write SQL statements using ORACLE or MYSQL, you need to follow some basic steps:
  - Connect to the database server using a client application, such as SQL Developer for ORACLE or MySQL Workbench for MYSQL.
  - Specify the database and schema (or user) that you want to work with, using the USE or ALTER SESSION commands.
  - Write SQL statements that follow the syntax and rules of the SQL language, such as SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, etc.
  - Execute the SQL statements using the RUN or EXECUTE commands, or by pressing a keyboard shortcut, such as F5 or Ctrl+Enter.
  - View the results of the SQL statements in the output window or grid, and check for any errors or warnings.
  - Save the SQL statements in a script file, using the SAVE or SAVE AS commands, or by choosing a file name and location.
  - Close the connection to the database server, using the EXIT or DISCONNECT commands, or by closing the client application.

- Some examples of SQL statements using ORACLE or MYSQL are:

  - To select all the columns and rows from a table called EMPLOYEES:

    ```sql
    SELECT * FROM EMPLOYEES;
    ```

  - To insert a new row into a table called DEPARTMENTS, with values for the columns DEPT_ID, DEPT_NAME, and LOCATION:

    ```sql
    INSERT INTO DEPARTMENTS (DEPT_ID, DEPT_NAME, LOCATION) VALUES (10, 'Sales', 'New York');
    ```

  - To update the salary of an employee with the employee ID 1001, by adding 500 to the current salary:

    ```sql
    UPDATE EMPLOYEES SET SALARY = SALARY + 500 WHERE EMP_ID = 1001;
    ```

  - To delete a row from a table called PRODUCTS, where the product ID is 101:

    ```sql
    DELETE FROM PRODUCTS WHERE PROD_ID = 101;
    ```

  - To create a new table called CUSTOMERS, with columns CUST_ID, CUST_NAME, CUST_EMAIL, and CUST_PHONE:

    ```sql
    CREATE TABLE CUSTOMERS (
      CUST_ID INT PRIMARY KEY,
      CUST_NAME VARCHAR(50) NOT NULL,
      CUST_EMAIL VARCHAR(50) UNIQUE,
      CUST_PHONE VARCHAR(15)
    );
    ```

  - To alter the data type of a column called CUST_PHONE, from VARCHAR(15) to VARCHAR(20), in a table called CUSTOMERS:

    ```sql
    ALTER TABLE CUSTOMERS MODIFY CUST_PHONE VARCHAR(20);
    ```

  - To drop a table called ORDERS, along with its data and constraints:

    ```sql
    DROP TABLE ORDERS;
    ```