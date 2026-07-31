
### Writing basic SQL SELECT statements 

1. The SQL SELECT statement is used to retrieve data from a database. 
2. The syntax of the SELECT statement is: 
    ```
    SELECT column1, column2, ... 
    FROM table_name;
    ```
3. The asterisk (\*) character can be used to select all columns in a table: 
    ```
    SELECT * 
    FROM table_name;
    ```
4. The WHERE clause is used to filter records: 
    ```
    SELECT column1, column2, ... 
    FROM table_name 
    WHERE condition;
    ```
5. The ORDER BY clause is used to sort the result set in ascending or descending order: 
    ```
    SELECT column1, column2, ... 
    FROM table_name 
    ORDER BY column1, column2, ... ASC|DESC;
    ```
6. The LIMIT clause is used to limit the number of records returned: 
    ```
    SELECT column1, column2, ... 
    FROM table_name 
    LIMIT number_of_records;
    ```
7. The ORACLE/MYSQL SELECT statement can be used to join multiple tables: 
    ```
    SELECT column1, column2, ... 
    FROM table1 
    INNER JOIN table2 
    ON table1.column_name = table2.column_name;
    ```