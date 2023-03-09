### Queries and Sub Queries

In the context of relational databases, queries are used to retrieve data from one or more tables based on specific criteria. Sub queries are queries that are embedded within another query to retrieve data that is used to filter the results of the outer query. In this section, we will cover the basics of queries and sub queries in the context of the relational data model and language.

#### Basic Query Structure

A basic query consists of the SELECT, FROM, and WHERE clauses. The SELECT clause specifies the columns to be retrieved, the FROM clause specifies the tables to be queried, and the WHERE clause specifies the conditions for selecting the data. Here is an example of a basic query:

```
SELECT column1, column2, ...
FROM table1, table2, ...
WHERE condition1 AND condition2 AND ...
```

#### Sub Queries

Sub queries can be used in place of a table or view in a query. They can be used in the SELECT, FROM, and WHERE clauses of a query. The result of a sub query is a single value or a table of values that can be used in the outer query. Here is an example of a sub query:

```
SELECT column1, column2, ...
FROM table1
WHERE column1 IN (SELECT column1 FROM table2 WHERE condition);
```

In this example, the sub query retrieves values from table2 based on a condition, and these values are used to filter the results of the outer query.

#### Advantages and Disadvantages of Sub Queries

Sub queries have several advantages, including:

- They can simplify complex queries by breaking them down into smaller, more manageable parts.
- They can be used to retrieve data that is not available in a single table.
- They can be used to perform calculations or aggregations on data before it is used in the outer query.

However, sub queries also have some disadvantages, including:

- They can be slower than other query techniques, especially if they are used in a large query.
- They can be difficult to read and understand, especially if they are nested several levels deep.
- They can be limited in their ability to handle large amounts of data.

#### Examples of Sub Queries

Here are some examples of sub queries:

```
SELECT column1, column2, ...
FROM table1
WHERE column1 IN (SELECT column1 FROM table2 WHERE condition);

SELECT column1, column2, ...
FROM table1
WHERE column1 = (SELECT MAX(column1) FROM table2);

SELECT column1, column2, ...
FROM table1
WHERE column1 NOT IN (SELECT column1 FROM table2 WHERE condition);
```

#### Applications of Sub Queries

Sub queries are commonly used in SQL to:

- Filter data based on complex conditions.
- Perform calculations or aggregations on data before it is used in the outer query.
- Retrieve data from multiple tables.

#### Conclusion

Queries and sub queries are essential tools for working with relational databases. They allow you to retrieve and manipulate data in a flexible and efficient way. By understanding the basics of queries and sub queries, you can take advantage of their power and flexibility to build complex and powerful database applications.