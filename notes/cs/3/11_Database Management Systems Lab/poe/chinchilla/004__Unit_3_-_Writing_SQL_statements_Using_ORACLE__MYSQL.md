## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

In this unit, we will learn about writing SQL statements using ORACLE and MYSQL. SQL (Structured Query Language) is a widely used language for managing relational databases. It is used to create, modify, and query databases. 

Here are some key concepts that you should know about writing SQL statements using ORACLE/MYSQL:

1. SQL is used to communicate with databases, and it is used to perform various operations on data such as inserting, updating, and deleting data.

2. ORACLE and MYSQL are two popular relational database management systems that use SQL for database operations. 

3. SQL statements are used to interact with databases. There are several types of SQL statements, including SELECT, INSERT, UPDATE, and DELETE.

4. SELECT statements are used to retrieve data from one or more tables in a database. The syntax for a SELECT statement is as follows:

    ```
    SELECT column_name(s) FROM table_name WHERE condition;
    ```

5. INSERT statements are used to add new data to a table in a database. The syntax for an INSERT statement is as follows:

    ```
    INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
    ```

6. UPDATE statements are used to modify existing data in a table in a database. The syntax for an UPDATE statement is as follows:

    ```
    UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
    ```

7. DELETE statements are used to delete data from a table in a database. The syntax for a DELETE statement is as follows:

    ```
    DELETE FROM table_name WHERE condition;
    ```

8. In SQL, the WHERE clause is used to filter data based on a specific condition. The syntax for a WHERE clause is as follows:

    ```
    WHERE column_name operator value;
    ```

9. Operators that can be used in the WHERE clause include =, <, >, <=, >=, and <>.

10. SQL statements can be combined using logical operators such as AND, OR, and NOT.

11. In addition to basic SQL statements, advanced SQL statements can be used to perform more complex database operations. These include JOIN, GROUP BY, HAVING, and ORDER BY statements.

12. A JOIN statement is used to combine data from two or more tables based on a related column. The syntax for a JOIN statement is as follows:

    ```
    SELECT column_name(s) FROM table1 JOIN table2 ON table1.column_name = table2.column_name;
    ```

13. A GROUP BY statement is used to group data based on a specific column. The syntax for a GROUP BY statement is as follows:

    ```
    SELECT column_name(s) FROM table_name GROUP BY column_name;
    ```

14. A HAVING statement is used to filter data based on a specific condition after a GROUP BY statement has been executed. The syntax for a HAVING statement is as follows:

    ```
    SELECT column_name(s) FROM table_name GROUP BY column_name HAVING condition;
    ```

15. An ORDER BY statement is used to sort data in ascending or descending order based on a specific column. The syntax for an ORDER BY statement is as follows:

    ```
    SELECT column_name(s) FROM table_name ORDER BY column_name ASC|DESC;
    ```

By understanding these key concepts, you will be able to write SQL statements using ORACLE and MYSQL to perform various operations on databases.