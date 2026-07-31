## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- ORACLE and MYSQL are two popular relational database management systems (RDBMS) that use SQL as their query language.
- To write SQL statements using ORACLE or MYSQL, you need to follow some basic steps:
  - Connect to the database server using a client application, such as SQL Developer for ORACLE or MySQL Workbench for MYSQL.
  - Specify the database and schema (or user) that you want to work with, using the USE or ALTER SESSION commands.
  - Write SQL statements that follow the syntax and rules of the SQL language, such as SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, etc.
  - Execute the SQL statements using the RUN or EXECUTE commands, or by pressing a button in the client application.
  - View the results of the SQL statements in the output window or grid, or save them to a file or table.
  - Close the connection to the database server when you are done, using the EXIT or QUIT commands, or by closing the client application.

- Some examples of SQL statements using ORACLE or MYSQL are:

  - To select all the records from the EMPLOYEES table in the HR schema:

    ```sql
    -- ORACLE
    ALTER SESSION SET CURRENT_SCHEMA = HR;
    SELECT * FROM EMPLOYEES;

    -- MYSQL
    USE HR;
    SELECT * FROM EMPLOYEES;
    ```

  - To insert a new record into the DEPARTMENTS table in the HR schema:

    ```sql
    -- ORACLE
    ALTER SESSION SET CURRENT_SCHEMA = HR;
    INSERT INTO DEPARTMENTS (DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID, LOCATION_ID)
    VALUES (300, 'Research', 100, 1700);

    -- MYSQL
    USE HR;
    INSERT INTO DEPARTMENTS (DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID, LOCATION_ID)
    VALUES (300, 'Research', 100, 1700);
    ```

  - To update the salary of the employee with employee_id 200 in the EMPLOYEES table in the HR schema:

    ```sql
    -- ORACLE
    ALTER SESSION SET CURRENT_SCHEMA = HR;
    UPDATE EMPLOYEES
    SET SALARY = SALARY * 1.1
    WHERE EMPLOYEE_ID = 200;

    -- MYSQL
    USE HR;
    UPDATE EMPLOYEES
    SET SALARY = SALARY * 1.1
    WHERE EMPLOYEE_ID = 200;
    ```

  - To delete the record of the department with department_id 300 from the DEPARTMENTS table in the HR schema:

    ```sql
    -- ORACLE
    ALTER SESSION SET CURRENT_SCHEMA = HR;
    DELETE FROM DEPARTMENTS
    WHERE DEPARTMENT_ID = 300;

    -- MYSQL
    USE HR;
    DELETE FROM DEPARTMENTS
    WHERE DEPARTMENT_ID = 300;
    ```

  - To create a new table called PROJECTS in the HR schema:

    ```sql
    -- ORACLE
    ALTER SESSION SET CURRENT_SCHEMA = HR;
    CREATE TABLE PROJECTS (
      PROJECT_ID NUMBER(4) PRIMARY KEY,
      PROJECT_NAME VARCHAR2(50) NOT NULL,
      START_DATE DATE NOT NULL,
      END_DATE DATE,
      BUDGET NUMBER(10,2) NOT NULL
    );

    -- MYSQL
    USE HR;
    CREATE TABLE PROJECTS (
      PROJECT_ID INT(4) PRIMARY KEY,
      PROJECT_NAME VARCHAR(50) NOT NULL,
      START_DATE DATE NOT NULL,
      END_DATE DATE,
      BUDGET DECIMAL(10,2) NOT NULL
    );
    ```

  - To alter the table PROJECTS by adding a new column called STATUS in the HR schema:

    ```sql
    -- ORACLE
    ALTER SESSION SET CURRENT_SCHEMA = HR;
    ALTER TABLE PROJECTS
    ADD STATUS VARCHAR2(10) DEFAULT 'OPEN';

    -- MYSQL
    USE HR;
    ALTER TABLE PROJECTS
    ADD STATUS VARCHAR(10) DEFAULT 'OPEN';
    ```

  - To drop the table PROJECTS from the HR schema:

    ```sql
    -- ORACLE
    ALTER SESSION SET CURRENT_SCHEMA = HR;
    DROP TABLE PROJECTS;

    -- MYSQL
    USE HR;
    DROP TABLE PROJECTS;
    ```