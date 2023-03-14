Merging data from multiple tables in JDBC is a process of joining two or more tables based on a common field or condition. There are different types of joins available in SQL, such as inner join, outer join, natural join, cross join, etc. Depending on the join type, the result set will contain different combinations of rows from the tables.

The following diagram illustrates the basic architecture of a JDBC application that merges data from multiple tables:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  JDBC Driver    |      |  JDBC API       |      |  Application    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Driver Manager |<---->|  Connection     |<---->|  SQL Statement  |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Database       |<---->|  Statement      |<---->|  Result Set     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Table 1        |      |  ResultSet      |<---->|  Data           |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Table 2        |      |  ResultSet      |<---->|  Data           |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Table 3        |      |  ResultSet      |<---->|  Data           |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The steps involved in merging data from multiple tables in JDBC are:

- Create a JDBC connection object using the DriverManager class and the database URL, username, and password.
- Create a JDBC statement object using the connection object and the SQL query that joins the tables.
- Execute the statement object using the executeQuery() method and store the result in a JDBC result set object.
- Iterate over the result set object using the next() method and retrieve the data from each row using the getXXX() methods, where XXX is the data type of the column.
- Close the result set, statement, and connection objects using the close() method.