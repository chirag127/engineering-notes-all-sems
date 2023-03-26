#### CO 5: Examine Various SQL Queries from MySQL Database K4, K5

In this section, we will examine various SQL queries that can be used in a MySQL database. These queries are essential in managing and retrieving data from a database. 

1. SELECT Query: The SELECT query is used to retrieve data from one or more tables in a database. It is the most commonly used SQL query. The syntax of the SELECT query is as follows:

   ```
   SELECT column1, column2, ..., columnN FROM table_name;
   ```

2. INSERT Query: The INSERT query is used to insert new data into a table in a database. The syntax of the INSERT query is as follows:

   ```
   INSERT INTO table_name (column1, column2, ..., columnN) VALUES (value1, value2, ..., valueN);
   ```

3. UPDATE Query: The UPDATE query is used to update existing data in a table in a database. The syntax of the UPDATE query is as follows:

   ```
   UPDATE table_name SET column1 = value1, column2 = value2, ..., columnN = valueN WHERE condition;
   ```

4. DELETE Query: The DELETE query is used to delete data from a table in a database. The syntax of the DELETE query is as follows:

   ```
   DELETE FROM table_name WHERE condition;
   ```

5. JOIN Query: The JOIN query is used to combine rows from two or more tables in a database based on a related column between them. The syntax of the JOIN query is as follows:

   ```
   SELECT column1, column2, ..., columnN FROM table1 JOIN table2 ON table1.column_name = table2.column_name;
   ```

6. GROUP BY Query: The GROUP BY query is used to group rows in a table in a database based on a specified column. The syntax of the GROUP BY query is as follows:

   ```
   SELECT column1, column2, ..., columnN FROM table_name GROUP BY column_name;
   ```

7. ORDER BY Query: The ORDER BY query is used to sort the result set in ascending or descending order based on a specified column. The syntax of the ORDER BY query is as follows:

   ```
   SELECT column1, column2, ..., columnN FROM table_name ORDER BY column_name ASC|DESC;
   ```

8. LIMIT Query: The LIMIT query is used to limit the number of rows returned in the result set. The syntax of the LIMIT query is as follows:

   ```
   SELECT column1, column2, ..., columnN FROM table_name LIMIT number_of_rows;
   ```

9. LIKE Query: The LIKE query is used to search for a specified pattern in a column of a table in a database. The syntax of the LIKE query is as follows:

   ```
   SELECT column1, column2, ..., columnN FROM table_name WHERE column_name LIKE pattern;
   ```

10. Subquery: A subquery is a query that is nested inside another query. It is used to retrieve data based on a condition from a single table or multiple tables. The syntax of the subquery is as follows:

    ```
    SELECT column1, column2, ..., columnN FROM table_name WHERE column_name = (SELECT column_name FROM table_name WHERE condition);
    ```

These are some of the most commonly used SQL queries in a MySQL database. Understanding and mastering these queries will allow you to effectively manage and retrieve data from a database.