#### Joining in JDBC

Joining in JDBC can be done by executing a SQL statement that includes a JOIN clause. Here is an example of how to perform a JOIN operation between two tables in JDBC:

```java
// Assume conn is an active Connection
Statement stmt = conn.createStatement();
String query = "SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id";
ResultSet rs = stmt.executeQuery(query);

while (rs.next()) {
    // Process the row
}
```

This code creates a `Statement` object and executes a SQL query that performs an `INNER JOIN` between `table1` and `table2` on the `id` column. The results of the query are stored in a `ResultSet` object, which can be iterated to process each row of the result.