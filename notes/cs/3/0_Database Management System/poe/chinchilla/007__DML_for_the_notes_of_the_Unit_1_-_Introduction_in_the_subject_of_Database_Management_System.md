### DML

DML stands for Data Manipulation Language, and it is a subset of SQL that is used to manipulate data stored in a database. DML is used to insert, update, delete, and retrieve data from a database. Here are some important points to know about DML:

- DML is used to insert data into a table. The INSERT statement is used to add new rows to a table. The syntax for the INSERT statement is as follows:

    ```sql
    INSERT INTO table_name (column1, column2, column3,...)
    VALUES (value1, value2, value3,...);
    ```

- DML is used to update data in a table. The UPDATE statement is used to modify existing data in a table. The syntax for the UPDATE statement is as follows:

    ```sql
    UPDATE table_name
    SET column1 = value1, column2 = value2,...
    WHERE condition;
    ```

- DML is used to delete data from a table. The DELETE statement is used to remove rows from a table. The syntax for the DELETE statement is as follows:

    ```sql
    DELETE FROM table_name WHERE condition;
    ```

- DML is used to retrieve data from a table. The SELECT statement is used to query a table and retrieve data. The syntax for the SELECT statement is as follows:

    ```sql
    SELECT column1, column2, column3,...
    FROM table_name
    WHERE condition;
    ```

- DML statements can be used in combination with other SQL statements to perform complex operations on a database.

- It is important to be careful when using DML statements, as they can affect multiple rows or even entire tables if not used correctly.

- DML statements are often used in conjunction with Data Definition Language (DDL) statements, which are used to create and modify the structure of a database.

In conclusion, DML is an important subset of SQL that is used to manipulate data stored in a database. It is used to insert, update, delete, and retrieve data from a table. It is important to be familiar with the syntax and usage of DML statements in order to effectively manage and manipulate data in a database.