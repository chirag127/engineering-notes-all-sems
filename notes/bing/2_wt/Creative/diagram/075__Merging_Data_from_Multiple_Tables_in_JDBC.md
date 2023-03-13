Merging data from multiple tables in JDBC is a process of combining the data from different sources into a single result set. There are different ways to achieve this, such as using SQL joins, subqueries, or custom code. One of the common methods is to use SQL joins, which allow you to specify the conditions for matching the rows from different tables based on common fields or expressions. There are different types of SQL joins, such as inner join, outer join, cross join, natural join, etc. Each type of join has a different effect on the result set and the performance of the query.

The following diagram illustrates the basic architecture of a SQL join operation in JDBC:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   JDBC Driver  |     |   SQL Server   |     |   JDBC Client  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |<---------------------|                      |
       |  SQL join query      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |---------------------->|
       |                      |  Result set          |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
```

The diagram shows the following steps:

- The JDBC client initiates a connection to the SQL server using the JDBC driver.
- The JDBC client sends a SQL join query to the SQL server using the JDBC driver.
- The SQL server executes the SQL join query and joins the data from multiple tables based on the join conditions.
- The SQL server returns the result set to the JDBC client using the JDBC driver.
- The JDBC client processes the result set and displays the merged data.