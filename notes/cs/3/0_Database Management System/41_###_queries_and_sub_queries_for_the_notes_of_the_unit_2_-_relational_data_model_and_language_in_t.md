### Queries and Sub Queries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

Queries and sub-queries are two important concepts in database management systems that are used to retrieve data from a database. 

1. Queries: Queries are used to retrieve data from a database by specifying the conditions that the data must meet. Queries are written using a query language, such as SQL, and they are executed against a database to retrieve the data.

2. Sub-queries: Sub-queries are queries that are used within another query to retrieve data. Sub-queries are used to retrieve data that will be used as part of the main query, and they are executed before the main query.

The general structure of a sub-query in SQL is:

```
SELECT column_name
FROM table_name
WHERE column_name operator (SELECT column_name
                            FROM table_name
                            WHERE condition);
```

In this unit, you will learn about queries and sub-queries in database management systems, including the syntax, usage, and examples. You will also learn about the various types of queries that can be used to retrieve data from a database, including select queries, update queries, and delete queries. This will provide a foundation for understanding the principles and practices of database management systems, and for exploring the various concepts and techniques used in database design and implementation.
