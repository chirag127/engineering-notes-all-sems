### Queries and Sub Queries

Queries and sub queries are essential tools when it comes to retrieving data from a database management system. In this unit, we will explore the different types of queries and sub queries that can be used in a relational data model.

#### Queries

A query is a request for data from a database. It is used to retrieve specific information from one or more tables in a database. There are different types of queries, such as:

- **Select Query**: This query is used to retrieve data from one or more tables in a database. It can be used to retrieve all the data from a table or only specific columns. The syntax for a select query is as follows:

```sql
SELECT column1, column2, ... FROM table_name;
```

- **Insert Query**: This query is used to insert new data into a table in a database. The syntax for an insert query is as follows:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

- **Update Query**: This query is used to update existing data in a table in a database. The syntax for an update query is as follows:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

- **Delete Query**: This query is used to delete data from a table in a database. The syntax for a delete query is as follows:

```sql
DELETE FROM table_name WHERE condition;
```

#### Sub Queries

A sub query is a query that is nested inside another query. It is used to retrieve data that will be used in the main query. There are different types of sub queries, such as:

- **Single-row sub query**: This sub query returns only one row of data to the main query. The syntax for a single-row sub query is as follows:

```sql
SELECT column1, column2, ... FROM table_name WHERE column_name = (SELECT column_name FROM table_name WHERE condition);
```

- **Multiple-row sub query**: This sub query returns multiple rows of data to the main query. The syntax for a multiple-row sub query is as follows:

```sql
SELECT column1, column2, ... FROM table_name WHERE column_name operator (SELECT column_name FROM table_name WHERE condition);
```

- **Correlated sub query**: This sub query is related to the main query and depends on the values returned from the main query. The syntax for a correlated sub query is as follows:

```sql
SELECT column1, column2, ... FROM table_name t1 WHERE condition operator (SELECT column_name FROM table_name t2 WHERE t1.column_name = t2.column_name);
```

In conclusion, queries and sub queries are essential tools for retrieving and manipulating data in a relational data model. Understanding their syntax and usage is crucial for effective database management system operations.