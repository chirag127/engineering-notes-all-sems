# Join Operations

Join operations are used to combine data from two or more tables in a relational database based on some common attribute or condition. Join operations are essential for querying data across multiple tables and for implementing relationships between entities.

## Types of Join Operations

There are different types of join operations that can be performed in SQL, depending on the desired result. Some of the most common types are:

- **Inner join**: This type of join returns only the rows that match the join condition in both tables. For example, if we want to join the tables `Customers` and `Orders` based on the `CustomerID` column, an inner join will return only the rows where the same `CustomerID` exists in both tables.
- **Left outer join**: This type of join returns all the rows from the left table, and the matching rows from the right table. If there is no match for a row in the left table, the columns from the right table will be null. For example, if we want to join the tables `Customers` and `Orders` based on the `CustomerID` column, a left outer join will return all the rows from the `Customers` table, and the corresponding rows from the `Orders` table if they exist, or null values otherwise.
- **Right outer join**: This type of join returns all the rows from the right table, and the matching rows from the left table. If there is no match for a row in the right table, the columns from the left table will be null. For example, if we want to join the tables `Customers` and `Orders` based on the `CustomerID` column, a right outer join will return all the rows from the `Orders` table, and the corresponding rows from the `Customers` table if they exist, or null values otherwise.
- **Full outer join**: This type of join returns all the rows from both tables, and the matching rows from the other table. If there is no match for a row in either table, the columns from the other table will be null. For example, if we want to join the tables `Customers` and `Orders` based on the `CustomerID` column, a full outer join will return all the rows from both tables, and the corresponding rows from the other table if they exist, or null values otherwise.
- **Cross join**: This type of join returns the Cartesian product of the two tables, which means every possible combination of rows from both tables. For example, if we want to join the tables `Customers` and `Orders` without any condition, a cross join will return every row from the `Customers` table paired with every row from the `Orders` table.

## Syntax of Join Operations

The general syntax of join operations in SQL is:

```sql
SELECT column_list
FROM table1
JOIN table2
ON join_condition;
```

The `JOIN` keyword can be replaced by the specific type of join, such as `INNER JOIN`, `LEFT OUTER JOIN`, `RIGHT OUTER JOIN`, `FULL OUTER JOIN`, or `CROSS JOIN`. The `ON` clause specifies the join condition, which is usually a comparison of columns from both tables using a logical operator, such as `=` or `<>`. The `SELECT` clause specifies the columns to be retrieved from the joined tables.

For example, the following query performs an inner join between the tables `Customers` and `Orders` based on the `CustomerID` column, and returns the `CustomerName`, `OrderID`, and `OrderDate` columns:

```sql
SELECT Customers.CustomerName, Orders.OrderID, Orders.OrderDate
FROM Customers
INNER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;
```

## References

: Joins (SQL Server) - SQL Server | Microsoft Learn. https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver16
: SQL JOIN | How to link Relational Databases - IONOS. https://www.ionos.com/digitalguide/hosting/technical-matters/sql-join/
: JOIN OPERATOR - University of Delaware. https://www1.udel.edu/evelyn/SQL-Class2/SQLclass2_Join.html
: How To Use Joins in SQL | DigitalOcean. https://www.digitalocean.com/community/tutorials/how-to-use-joins-in-sql