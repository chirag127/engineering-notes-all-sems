## Data Query Language (DQL) Statements

Data Query Language (DQL) is a subset of SQL, which is used to retrieve information from a database. It is an essential part of Database Management Systems, and understanding DQL statements is crucial for efficiently querying databases. This section covers the basics of DQL statements and their syntax.

### SELECT Statement

The SELECT statement is the most commonly used DQL statement. It is used to retrieve data from one or more tables in a database. The basic syntax of the SELECT statement is as follows:

```
SELECT column1, column2, ... FROM table_name;
```

- `SELECT`: The keyword that indicates that we are retrieving data from the database.
- `column1, column2, ...`: The columns we want to retrieve data from. We can use the `*` operator to select all columns.
- `FROM`: The keyword that indicates the table from which we want to retrieve data.
- `table_name`: The name of the table from which we want to retrieve data.

### WHERE Clause

The WHERE clause is used to filter data based on certain conditions. The basic syntax of the WHERE clause is as follows:

```
SELECT column1, column2, ... FROM table_name WHERE condition;
```

- `condition`: The condition that we want to apply to the data. We can use comparison operators (`=`, `<>`, `>`, `<`, `>=`, `<=`) and logical operators (`AND`, `OR`, `NOT`) to create complex conditions.

### ORDER BY Clause

The ORDER BY clause is used to sort the retrieved data in ascending or descending order. The basic syntax of the ORDER BY clause is as follows:

```
SELECT column1, column2, ... FROM table_name ORDER BY column1 ASC/DESC;
```

- `ASC`: The keyword that indicates ascending order.
- `DESC`: The keyword that indicates descending order.

### GROUP BY Clause

The GROUP BY clause is used to group the retrieved data based on one or more columns. The basic syntax of the GROUP BY clause is as follows:

```
SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ...;
```

### HAVING Clause

The HAVING clause is used to filter the grouped data based on certain conditions. The basic syntax of the HAVING clause is as follows:

```
SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ... HAVING condition;
```

- `condition`: The condition that we want to apply to the grouped data.

### LIMIT Clause

The LIMIT clause is used to limit the number of retrieved rows. The basic syntax of the LIMIT clause is as follows:

```
SELECT column1, column2, ... FROM table_name LIMIT number_of_rows;
```

- `number_of_rows`: The maximum number of rows we want to retrieve.

### Conclusion

In summary, DQL statements are used to retrieve data from a database. The SELECT statement is the most commonly used DQL statement, and it can be combined with other clauses (WHERE, ORDER BY, GROUP BY, HAVING, and LIMIT) to create more complex queries. Understanding DQL statements is essential for efficiently querying databases, and this section provides a basic overview of their syntax.