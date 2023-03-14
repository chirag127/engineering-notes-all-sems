Joining in JDBC is the process of combining data from two or more tables based on a common column or condition. There are different types of joins available in JDBC, such as inner join, outer join, natural join, cross join, etc. Each join type has a different syntax and result set.

The following diagram illustrates the basic architecture of a joining operation in JDBC:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Application   |      |  JDBC Driver   |      |  Database      |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  SQL Query     |----->|  SQL Query     |----->|  SQL Query     |
|  with Join     |      |  with Join     |      |  with Join     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Result Set    |<-----|  Result Set    |<-----|  Result Set    |
|  with Join     |      |  with Join     |      |  with Join     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The steps involved in a joining operation in JDBC are:

1. Import the required package for the corresponding database.
2. Load and register the JDBC drivers.
3. Establish the connection with the database using a URL, username and password.
4. Create a statement object to execute the SQL query with join.
5. Execute the query and get the result set object that contains the joined data.
6. Process the result set by iterating over the rows and columns.
7. Close the connections and resources.