#### CO 5 Examine various SQL queries from MySQL database K4, K5

In this section, we will discuss various SQL queries that can be used to extract or manipulate data from MySQL databases. SQL queries are essential for retrieving data from databases, and it is crucial to know how to write effective queries to extract the desired information. 

The following are some essential SQL queries:

1. **SELECT**: This is the most basic SQL query used to retrieve data from a database. It is used to select specific columns or all columns from a table. The syntax is as follows:

   ```
   SELECT column1, column2, ... FROM table_name;
   ```

2. **WHERE**: This clause is used to filter data based on specific conditions. It is used in conjunction with the `SELECT` statement. The syntax is as follows:

   ```
   SELECT column1, column2, ... FROM table_name WHERE condition;
   ```

3. **ORDER BY**: This clause is used to sort data in either ascending or descending order. It is used in conjunction with the `SELECT` statement. The syntax is as follows:

   ```
   SELECT column1, column2, ... FROM table_name ORDER BY column_name ASC|DESC;
   ```

4. **GROUP BY**: This clause is used to group data based on specific columns. It is used in conjunction with the `SELECT` statement. The syntax is as follows:

   ```
   SELECT column1, COUNT(column2) FROM table_name GROUP BY column1;
   ```

5. **JOIN**: This clause is used to combine data from two or more tables based on a related column. It is used in conjunction with the `SELECT` statement. The syntax is as follows:

   ```
   SELECT column1, column2, ... FROM table1 JOIN table2 ON table1.column = table2.column;
   ```

6. **INSERT INTO**: This query is used to insert data into a table. The syntax is as follows:

   ```
   INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
   ```

7. **UPDATE**: This query is used to update existing data in a table. The syntax is as follows:

   ```
   UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
   ```

8. **DELETE**: This query is used to delete data from a table. The syntax is as follows:

   ```
   DELETE FROM table_name WHERE condition;
   ```

In conclusion, SQL queries play a significant role in retrieving data from MySQL databases. It is essential to know how to write effective queries to extract the desired information. This knowledge is critical for any individual who works with databases or data analysis.