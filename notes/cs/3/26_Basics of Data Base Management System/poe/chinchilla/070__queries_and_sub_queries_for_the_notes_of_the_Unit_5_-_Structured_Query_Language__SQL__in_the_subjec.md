### Queries and Sub Queries

SQL is a powerful language used to extract and manipulate data from relational databases. In this unit, we will learn about queries and sub queries, which are essential concepts in SQL.

#### Queries

A query is a request for information from a database. It is used to retrieve specific data based on certain conditions. The basic structure of a query is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- The `SELECT` statement specifies the columns to be retrieved from the table.
- The `FROM` statement specifies the table from which the data is to be retrieved.
- The `WHERE` statement specifies the conditions that must be met for the data to be retrieved.

Some common operators used in the `WHERE` statement are:

- `=` (equal to)
- `<>` or `!=` (not equal to)
- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal to)
- `>=` (greater than or equal to)

#### Sub Queries

A sub query is a query within another query. It is used to retrieve data based on the results of another query. The basic structure of a sub query is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE column_name IN (SELECT column_name FROM table_name WHERE condition);
```

- The `IN` operator is used to specify that the values returned by the sub query must match the values in the specified column of the main query.

Sub queries can also be used in the `FROM` clause to create a temporary table for use in the main query.

```
SELECT column1, column2, ...
FROM (SELECT column_name FROM table_name WHERE condition) AS temp_table
WHERE condition;
```

- The `AS` keyword is used to give a name to the temporary table created by the sub query.

Sub queries can be nested to any depth, but it is important to write them in a way that is easy to understand and maintain.

#### Conclusion

Queries and sub queries are essential concepts in SQL. They allow us to retrieve and manipulate data from relational databases in a powerful and flexible way. By understanding these concepts, we can write more efficient and effective SQL code.