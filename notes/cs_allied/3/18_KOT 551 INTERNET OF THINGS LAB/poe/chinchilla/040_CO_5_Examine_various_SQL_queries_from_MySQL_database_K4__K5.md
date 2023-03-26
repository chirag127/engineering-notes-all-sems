# CO 5: Examine Various SQL Queries from MySQL Database K4, K5

In this section, we will discuss various SQL queries that can be used to manipulate data in a MySQL database. These queries are essential for anyone working with databases and are frequently used in software development, data analysis, and other related fields.

## Basic SQL Queries

1. **SELECT**: This query is used to retrieve data from one or more tables in a database. It is often the most commonly used query in SQL. The general syntax for the SELECT query is:

```sql
SELECT column1, column2, ... FROM table_name;
```

2. **INSERT**: This query is used to insert data into a table. The syntax for the INSERT query is:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

3. **UPDATE**: This query is used to modify existing data in a table. The syntax for the UPDATE query is:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

4. **DELETE**: This query is used to delete data from a table. The syntax for the DELETE query is:

```sql
DELETE FROM table_name WHERE condition;
```

## Advanced SQL Queries

1. **JOIN**: This query is used to combine data from two or more tables. There are several types of joins, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN. The syntax for the INNER JOIN query is:

```sql
SELECT column1, column2, ... FROM table1 INNER JOIN table2 ON table1.column = table2.column;
```

2. **GROUP BY**: This query is used to group data based on one or more columns in a table. The syntax for the GROUP BY query is:

```sql
SELECT column1, COUNT(column2) FROM table_name GROUP BY column1;
```

3. **ORDER BY**: This query is used to sort data based on one or more columns in a table. The syntax for the ORDER BY query is:

```sql
SELECT column1, column2, ... FROM table_name ORDER BY column1 ASC/DESC;
```

4. **DISTINCT**: This query is used to retrieve only unique values from a column in a table. The syntax for the DISTINCT query is:

```sql
SELECT DISTINCT column_name FROM table_name;
```

5. **LIMIT**: This query is used to limit the number of rows returned by a SELECT query. The syntax for the LIMIT query is:

```sql
SELECT column1, column2, ... FROM table_name LIMIT number_of_rows;
```

## Conclusion

In this section, we have covered various SQL queries that can be used in a MySQL database. These queries are essential for manipulating data in a database and are commonly used in software development and data analysis. By mastering these queries, you will have a solid foundation for working with databases and can easily retrieve, modify, and delete data as needed.