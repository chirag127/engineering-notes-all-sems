#### Joining in JDBC

- Joining in JDBC is the process of combining data from two or more tables based on a common column or condition.
- Joining in JDBC can be performed using the SQL JOIN clause in the query string, which specifies the tables to join and the join condition.
- Joining in JDBC can also be performed using the JoinRowSet interface, which allows adding RowSet objects to a JoinRowSet object and specifying the match column for each RowSet object.
- Joining in JDBC can be useful for retrieving related data from multiple tables in a single query, which can improve the performance and efficiency of the application.
- Joining in JDBC can be of different types, such as inner join, outer join, cross join, natural join, etc., depending on the join condition and the result set required.

Some examples of joining in JDBC are:

- Using SQL JOIN clause:

```java
// Create a query string with a join clause
String query = "SELECT p.name, p.price, s.name FROM Product p INNER JOIN Supplier s ON p.supplier_id = s.id";

// Execute the query using a Statement object
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(query);

// Process the result set
while (rs.next()) {
  String productName = rs.getString(1);
  double productPrice = rs.getDouble(2);
  String supplierName = rs.getString(3);
  System.out.println(productName + " - " + productPrice + " - " + supplierName);
}

// Close the resources
rs.close();
stmt.close();
```

- Using JoinRowSet interface:

```java
// Create a JoinRowSet object
JoinRowSet jrs = new JoinRowSetImpl();

// Create two RowSet objects with data from two tables
CachedRowSet productRS = new CachedRowSetImpl();
productRS.setCommand("SELECT id, name, price, supplier_id FROM Product");
productRS.execute(conn);

CachedRowSet supplierRS = new CachedRowSetImpl();
supplierRS.setCommand("SELECT id, name FROM Supplier");
supplierRS.execute(conn);

// Add the RowSet objects to the JoinRowSet object and specify the match column
jrs.addRowSet(productRS, "supplier_id");
jrs.addRowSet(supplierRS, "id");

// Process the JoinRowSet object
while (jrs.next()) {
  String productName = jrs.getString("name");
  double productPrice = jrs.getDouble("price");
  String supplierName = jrs.getString(5); // the fifth column is the name from the supplier table
  System.out.println(productName + " - " + productPrice + " - " + supplierName);
}

// Close the resources
jrs.close();
productRS.close();
supplierRS.close();
```