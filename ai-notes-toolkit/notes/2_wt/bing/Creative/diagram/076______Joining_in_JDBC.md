Joining in JDBC is the process of combining data from two or more tables based on a common column. To perform a join operation in JDBC, you need to follow these steps:

1. Import JDBC packages
2. Register and load the JDBC driver
3. Set a connection to the database
4. Create a statement object to execute the query
5. Works on the result set
6. Close the statement objects
7. Close the result set
8. Close the established connection

#### Joining in JDBC

The following diagram shows an example of joining two tables, Product and Supplier, based on the column ProductID.

```
+----------------+    +----------------+
| Product        |    | Supplier       |
+----------------+    +----------------+
| ProductID (PK) |----| ProductID (FK) |
| Name           |    | SupplierID (PK)|
| Price          |    | Name           |
| Category       |    | Address        |
+----------------+    +----------------+
```

The SQL query to perform this join is:

```sql
SELECT Product.Name, Product.Price, Supplier.Name, Supplier.Address
FROM Product
INNER JOIN Supplier
ON Product.ProductID = Supplier.ProductID;
```

The JDBC code to execute this query is:

```java
// Step 1: Import JDBC packages
import java.sql.*;

// Step 2: Register and load the JDBC driver
Class.forName("com.mysql.jdbc.Driver");

// Step 3: Set a connection to the database
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");

// Step 4: Create a statement object to execute the query
Statement stmt = conn.createStatement();

// Step 5: Works on the result set
ResultSet rs = stmt.executeQuery("SELECT Product.Name, Product.Price, Supplier.Name, Supplier.Address FROM Product INNER JOIN Supplier ON Product.ProductID = Supplier.ProductID");

// Loop through the result set and print the data
while (rs.next()) {
  System.out.println(rs.getString("Product.Name") + "\t" + rs.getDouble("Product.Price") + "\t" + rs.getString("Supplier.Name") + "\t" + rs.getString("Supplier.Address"));
}

// Step 6: Close the statement objects
stmt.close();

// Step 7: Close the result set
rs.close();

// Step 8: Close the established connection
conn.close();
```