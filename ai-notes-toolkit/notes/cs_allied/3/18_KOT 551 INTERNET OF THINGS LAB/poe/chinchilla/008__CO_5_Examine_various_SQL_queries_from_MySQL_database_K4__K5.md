#### CO 5 Examine various SQL queries from MySQL database K4, K5

To effectively manage and manipulate data stored in a MySQL database, it is essential to have a good understanding of SQL queries. In this section, we will examine various SQL queries used to interact with a MySQL database.

1. Select Query: 

The SELECT query is one of the most commonly used SQL queries. It is used to retrieve data from one or more tables in a database. The syntax for a basic SELECT query is as follows:

```
SELECT column1, column2, …
FROM table_name;
```

2. Insert Query:

The INSERT query is used to add new records to a table in a database. The syntax for the basic INSERT query is as follows:

```
INSERT INTO table_name (column1, column2, …)
VALUES (value1, value2, …);
```

3. Update Query:

The UPDATE query is used to modify existing records in a table. The syntax for the basic UPDATE query is as follows:

```
UPDATE table_name
SET column1 = value1, column2 = value2, …
WHERE condition;
```

4. Delete Query:

The DELETE query is used to remove one or more records from a table. The syntax for the basic DELETE query is as follows:

```
DELETE FROM table_name
WHERE condition;
```

5. Join Query:

The JOIN query is used to combine data from two or more tables. There are several types of JOIN queries, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN. The syntax for a basic INNER JOIN query is as follows:

```
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

6. Group By Query:

The GROUP BY query is used to group records in a table based on one or more columns. The syntax for a basic GROUP BY query is as follows:

```
SELECT column_name(s)
FROM table_name
GROUP BY column_name(s);
```

7. Order By Query:

The ORDER BY query is used to sort the data in a table based on one or more columns. The syntax for a basic ORDER BY query is as follows:

```
SELECT column_name(s)
FROM table_name
ORDER BY column_name(s) ASC|DESC;
```

In conclusion, understanding SQL queries is essential for effectively managing and manipulating data in a MySQL database. Learning and practicing these queries will enable you to retrieve, add, modify, and delete data from your database.