### Manipulating data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- SQL stands for Structured Query Language, which is a language for storing, manipulating, and retrieving data in relational database management systems.
- Oracle and MySQL are two popular relational database management systems that use SQL as their standard database language.
- Data manipulation language (DML) is a subset of SQL that allows users to add, change, and delete data in the database tables .
- DML statements include INSERT, UPDATE, DELETE, and MERGE .
- A transaction is a sequence of one or more DML statements that are treated as a unit by the database system. A transaction can either be committed (all changes are made permanent) or rolled back (all changes are undone) at the end.
- DML statements can be executed interactively using SQL commands, or embedded in a program using a host language such as Java, C#, or PHP .
- Some examples of DML statements using Oracle and MySQL syntax are:

  - INSERT: This statement adds one or more rows to a table. The syntax is:

    ```sql
    INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
    ```

    For example, to insert a new row into the EMPLOYEES table with the values 101, 'John', 'Smith', and 5000, the statement is:

    ```sql
    INSERT INTO EMPLOYEES (EMP_ID, FIRST_NAME, LAST_NAME, SALARY) VALUES (101, 'John', 'Smith', 5000);
    ```

  - UPDATE: This statement modifies one or more rows in a table. The syntax is:

    ```sql
    UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
    ```

    For example, to update the salary of the employee with the EMP_ID 101 to 6000, the statement is:

    ```sql
    UPDATE EMPLOYEES SET SALARY = 6000 WHERE EMP_ID = 101;
    ```

  - DELETE: This statement removes one or more rows from a table. The syntax is:

    ```sql
    DELETE FROM table_name WHERE condition;
    ```

    For example, to delete the employee with the EMP_ID 101 from the EMPLOYEES table, the statement is:

    ```sql
    DELETE FROM EMPLOYEES WHERE EMP_ID = 101;
    ```

  - MERGE: This statement combines the INSERT and UPDATE operations into one statement. It inserts new rows or updates existing rows based on a matching condition. The syntax is:

    ```sql
    MERGE INTO target_table USING source_table ON join_condition
    WHEN MATCHED THEN UPDATE SET column1 = value1, column2 = value2, ...
    WHEN NOT MATCHED THEN INSERT (column1, column2, ...) VALUES (value1, value2, ...);
    ```

    For example, to merge the data from the NEW_EMPLOYEES table into the EMPLOYEES table based on the EMP_ID column, the statement is:

    ```sql
    MERGE INTO EMPLOYEES USING NEW_EMPLOYEES ON (EMPLOYEES.EMP_ID = NEW_EMPLOYEES.EMP_ID)
    WHEN MATCHED THEN UPDATE SET EMPLOYEES.FIRST_NAME = NEW_EMPLOYEES.FIRST_NAME, EMPLOYEES.LAST_NAME = NEW_EMPLOYEES.LAST_NAME, EMPLOYEES.SALARY = NEW_EMPLOYEES.SALARY
    WHEN NOT MATCHED THEN INSERT (EMPLOYEES.EMP_ID, EMPLOYEES.FIRST_NAME, EMPLOYEES.LAST_NAME, EMPLOYEES.SALARY) VALUES (NEW_EMPLOYEES.EMP_ID, NEW_EMPLOYEES.FIRST_NAME, NEW_EMPLOYEES.LAST_NAME, NEW_EMPLOYEES.SALARY);
    ```

- DML statements can be combined with other SQL clauses such as WHERE, ORDER BY, GROUP BY, HAVING, and JOIN to filter, sort, aggregate, and join data from different tables .
- DML statements can also use operators such as arithmetic, comparison, logical, and string operators to perform calculations and comparisons on the data[^4