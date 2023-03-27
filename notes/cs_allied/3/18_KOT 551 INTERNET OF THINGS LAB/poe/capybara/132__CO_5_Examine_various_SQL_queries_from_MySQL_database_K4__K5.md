#### CO 5 Examine various SQL queries from MySQL database K4, K5

In this section, we will cover the different SQL queries that can be used in MySQL database. These queries are essential for database management and are commonly used in various applications. Below are some of the SQL queries used in MySQL:

- SELECT statement: This statement is used to retrieve data from a table. It can be used to select all columns or specific columns in a table. It is important to note that the SELECT statement is case-insensitive.

- INSERT INTO statement: This statement is used to insert new data into a table. The syntax for the INSERT INTO statement is as follows:

    ```
    INSERT INTO table_name (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);
    ```

- UPDATE statement: This statement is used to update existing data in a table. The syntax for the UPDATE statement is as follows:

    ```
    UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
    ```

- DELETE statement: This statement is used to delete existing data from a table. The syntax for the DELETE statement is as follows:

    ```
    DELETE FROM table_name
    WHERE condition;
    ```

- CREATE TABLE statement: This statement is used to create a new table in the database. The syntax for the CREATE TABLE statement is as follows:

    ```
    CREATE TABLE table_name (
        column1 datatype,
        column2 datatype,
        column3 datatype,
        ....
    );
    ```

- ALTER TABLE statement: This statement is used to modify an existing table in the database. The syntax for the ALTER TABLE statement is as follows:

    ```
    ALTER TABLE table_name
    ADD column_name datatype;
    ```

- DROP TABLE statement: This statement is used to remove an existing table from the database. The syntax for the DROP TABLE statement is as follows:

    ```
    DROP TABLE table_name;
    ```

In conclusion, understanding and mastering these SQL queries is essential for effective database management. These queries are used in a wide range of applications and can help to streamline data retrieval and manipulation.