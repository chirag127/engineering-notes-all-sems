## Data Query Language (DQL) Statements

Data Query Language (DQL) is a subset of the Structured Query Language (SQL) used to retrieve data from a database. DQL statements are used to perform queries on the data stored in the database and retrieve the desired information.

Here are some common DQL statements used in Database Management Systems:

1. **SELECT**: The SELECT statement is used to retrieve data from one or more tables in a database. The basic syntax of the SELECT statement is as follows:
```
SELECT column1, column2, ...
FROM table_name;
```
2. **WHERE**: The WHERE clause is used to filter the records returned by the SELECT statement. The basic syntax of the WHERE clause is as follows:
```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```
3. **ORDER BY**: The ORDER BY clause is used to sort the records returned by the SELECT statement in ascending or descending order. The basic syntax of the ORDER BY clause is as follows:
```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```
4. **GROUP BY**: The GROUP BY clause is used to group the records returned by the SELECT statement based on one or more columns. The basic syntax of the GROUP BY clause is as follows:
```
SELECT column1, column2, ...
FROM table_name
GROUP BY column1, column2, ...;
```
5. **HAVING**: The HAVING clause is used to filter the groups returned by the GROUP BY clause. The basic syntax of the HAVING clause is as follows:
```
SELECT column1, column2, ...
FROM table_name
GROUP BY column1, column2, ...
HAVING condition;
```

These are some of the basic DQL statements used in Database Management Systems. They can be used in combination to perform complex queries on the data stored in the database. It is important to have a good understanding of these statements to effectively retrieve data from a database.