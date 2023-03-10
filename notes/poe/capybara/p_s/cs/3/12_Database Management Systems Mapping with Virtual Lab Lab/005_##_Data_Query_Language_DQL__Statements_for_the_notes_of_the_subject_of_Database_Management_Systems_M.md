## Data Query Language(DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

Data Query Language (DQL) is a subset of SQL (Structured Query Language) used to retrieve data from a database. It is used to perform data manipulation operations such as retrieval, selection, and projection of data. In this section, we will discuss the various DQL statements and their use in database management systems.

### SELECT Statement

The SELECT statement is used to retrieve data from a database. It is the most commonly used statement in DQL. The basic syntax of the SELECT statement is as follows:

```
SELECT column1, column2, ... FROM table_name;
```

Where `column1`, `column2`, ... are the names of the columns to be retrieved and `table_name` is the name of the table from which the data is to be retrieved.

### WHERE Clause

The WHERE clause is used to filter data based on a specified condition. It is used in conjunction with the SELECT statement. The basic syntax of the WHERE clause is as follows:

```
SELECT column1, column2, ... FROM table_name WHERE condition;
```

Where `condition` is the condition that needs to be satisfied. For example:

```
SELECT * FROM employees WHERE salary > 50000;
```

This statement will retrieve all the employees whose salary is greater than 50000.

### ORDER BY Clause

The ORDER BY clause is used to sort the data in ascending or descending order based on one or more columns. The basic syntax of the ORDER BY clause is as follows:

```
SELECT column1, column2, ... FROM table_name ORDER BY column1 ASC/DESC, column2 ASC/DESC, ...;
```

Where `column1`, `column2`, ... are the names of the columns to be sorted and `ASC` or `DESC` is used to specify the order in which the data is to be sorted.

### GROUP BY Clause

The GROUP BY clause is used to group the data based on one or more columns. The basic syntax of the GROUP BY clause is as follows:

```
SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ...;
```

Where `column1`, `column2`, ... are the names of the columns to be grouped.

### HAVING Clause

The HAVING clause is used to filter the data based on a specified condition for a group of rows. It is used in conjunction with the GROUP BY clause. The basic syntax of the HAVING clause is as follows:

```
SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ... HAVING condition;
```

Where `condition` is the condition that needs to be satisfied.

### Joins

Joins are used to combine data from two or more tables based on a related column. There are four types of joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN.

```
SELECT column1, column2, ... FROM table1 JOIN table2 ON condition;
```

Where `table1` and `table2` are the names of the tables to be joined and `condition` is the condition that needs to be satisfied.

### Subqueries

A subquery is a query that is nested inside another query. It is used to retrieve data based on a condition that is not directly available in the table. The basic syntax of a subquery is as follows:

```
SELECT column1, column2, ... FROM table_name WHERE column_name IN (SELECT column_name FROM another_table WHERE condition);
```

Where `another_table` is the table from which the data is to be retrieved and `condition` is the condition that needs to be satisfied.

In conclusion, DQL statements are an essential part of database management systems. They are used to retrieve, filter, sort, group, and join data from tables. By understanding the various DQL statements, one can perform complex data manipulation operations on a database.