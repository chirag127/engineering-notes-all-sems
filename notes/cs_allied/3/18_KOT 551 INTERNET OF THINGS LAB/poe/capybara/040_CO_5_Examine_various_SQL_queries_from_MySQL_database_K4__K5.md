# CO 5: Examine Various SQL Queries from MySQL Database K4, K5

In this section, we will examine various SQL queries that can be used with the MySQL database. SQL stands for Structured Query Language, and it is used to communicate with databases. MySQL is a popular open-source relational database management system that uses SQL.

## SELECT Query

The SELECT query is used to retrieve data from a table. The basic syntax for a SELECT query is as follows:

```
SELECT column1, column2, ...
FROM table_name;
```

- The `column1, column2, ...` parameter specifies the columns that you want to retrieve data from.
- The `table_name` parameter specifies the name of the table from which you want to retrieve data.

## WHERE Clause

The WHERE clause is used to filter data based on a specific condition. The basic syntax for a SELECT query with a WHERE clause is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- The `condition` parameter specifies the condition that the data must meet in order to be returned.

## ORDER BY Clause

The ORDER BY clause is used to sort the data in ascending or descending order based on a specific column. The basic syntax for a SELECT query with an ORDER BY clause is as follows:

```
SELECT column1, column2, ...
FROM table_name
ORDER BY column_name ASC|DESC;
```

- The `column_name` parameter specifies the name of the column that you want to use for sorting.
- The `ASC` parameter specifies that the data should be sorted in ascending order (default).
- The `DESC` parameter specifies that the data should be sorted in descending order.

## JOIN Clause

The JOIN clause is used to combine data from two or more tables based on a related column. The basic syntax for a SELECT query with a JOIN clause is as follows:

```
SELECT column1, column2, ...
FROM table1
JOIN table2
ON table1.column_name = table2.column_name;
```

- The `table1` and `table2` parameters specify the names of the tables that you want to join.
- The `column_name` parameter specifies the name of the column that the tables have in common.

## GROUP BY Clause

The GROUP BY clause is used to group data based on a specific column. The basic syntax for a SELECT query with a GROUP BY clause is as follows:

```
SELECT column1, COUNT(column2)
FROM table_name
GROUP BY column1;
```

- The `COUNT(column2)` parameter specifies that you want to count the number of rows for each value in `column1`.
- The `GROUP BY` parameter specifies the name of the column that you want to group by.

## Conclusion

In this section, we have examined various SQL queries that can be used with the MySQL database. These queries can be used to retrieve, filter, sort, join, and group data from tables. Understanding these queries is essential for anyone who wants to work with databases.