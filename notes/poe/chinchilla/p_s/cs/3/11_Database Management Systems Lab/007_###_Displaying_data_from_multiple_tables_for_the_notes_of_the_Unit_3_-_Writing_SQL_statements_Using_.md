### Displaying data from multiple tables

In a database, data is often distributed across multiple tables. To get a complete view of the data, it is necessary to combine the data from these tables. This can be done using SQL JOIN statements.

#### Types of JOIN statements

There are four types of JOIN statements: 

1. INNER JOIN
2. LEFT JOIN
3. RIGHT JOIN
4. FULL OUTER JOIN

#### INNER JOIN

INNER JOIN returns only the rows that have matching values in both tables. This means that if there is no matching value in the other table, that row will not be included in the result set.

For example:

```sql
SELECT *
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

#### LEFT JOIN

LEFT JOIN returns all the rows from the left table and the matching rows from the right table. If there is no matching row in the right table, the result will contain NULL values.

For example:

```sql
SELECT *
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

#### RIGHT JOIN

RIGHT JOIN returns all the rows from the right table and the matching rows from the left table. If there is no matching row in the left table, the result will contain NULL values.

For example:

```sql
SELECT *
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

#### FULL OUTER JOIN

FULL OUTER JOIN returns all the rows from both tables. If there is no matching row in one of the tables, the result will contain NULL values.

For example:

```sql
SELECT *
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;
```

#### UNION

UNION is another way to combine data from multiple tables. However, unlike JOIN, UNION does not combine the data horizontally. Instead, it combines the data vertically.

For example:

```sql
SELECT column1
FROM table1
UNION
SELECT column1
FROM table2;
```

#### Conclusion

Displaying data from multiple tables is a fundamental concept in database management. Understanding how to use JOIN statements and UNION can help you build more complex queries and retrieve more meaningful data from your databases.