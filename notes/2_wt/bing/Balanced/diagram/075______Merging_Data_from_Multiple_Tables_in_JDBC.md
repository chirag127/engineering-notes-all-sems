Merging data from multiple tables in JDBC means combining the data from different sources into a single result set. There are different ways to do this, such as using SQL joins, subqueries, or a programmatic approach. Here is a simple example of how to merge data from two tables using a SQL join and JDBC:

#### Merging Data from Multiple Tables in JDBC

```
+--------+------+    +--------+------+
| Table1 |      |    | Table2 |      |
+--------+------+    +--------+------+
| id     | name |    | id     | age  |
+--------+------+    +--------+------+
| 1      | Bob  |    | 1      | 25   |
| 2      | Alice|    | 2      | 30   |
| 3      | John |    | 3      | 35   |
+--------+------+    +--------+------+

// SQL query to join the two tables on the id column
SELECT Table1.id, Table1.name, Table2.age FROM Table1 JOIN Table2 ON Table1.id = Table2.id;

// JDBC code to execute the query and display the result
// Assume conn is a valid Connection object
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT Table1.id, Table1.name, Table2.age FROM Table1 JOIN Table2 ON Table1.id = Table2.id");
while (rs.next()) {
  System.out.println(rs.getInt("id") + " " + rs.getString("name") + " " + rs.getInt("age"));
}
rs.close();
stmt.close();

// Output
1 Bob 25
2 Alice 30
3 John 35
```