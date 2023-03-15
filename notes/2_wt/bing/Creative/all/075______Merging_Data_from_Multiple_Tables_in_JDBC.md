#### Merging Data from Multiple Tables in JDBC

- JDBC stands for Java Database Connectivity, which is an API for connecting and executing queries on databases.
- JDBC allows you to perform various operations on data, such as inserting, updating, deleting, and retrieving data from one or more tables.
- Sometimes, you may need to merge data from multiple tables into a single result set, which can be done using SQL joins or subqueries.
- SQL joins are used to combine rows from two or more tables based on a common column or condition. There are different types of joins, such as inner join, outer join, cross join, and natural join.
- SQL subqueries are used to nest one query inside another query, which can be used to filter, aggregate, or compare data from multiple tables.
- To merge data from multiple tables in JDBC, you need to follow these steps:

  1. Create a connection object that represents a connection to the database using the DriverManager class.
  2. Create a statement object that can execute SQL queries using the connection object.
  3. Write a SQL query that uses joins or subqueries to merge data from multiple tables. You can use aliases to refer to different tables or columns in the query.
  4. Execute the query using the statement object and store the result in a result set object, which is a collection of rows that match the query.
  5. Iterate over the result set object and access the data from each row using the get methods of the result set object. You can use the column name or index to specify which column to get.
  6. Close the result set, statement, and connection objects to release the resources.

- Here is an example of merging data from multiple tables in JDBC using an inner join:

```java
//import the required packages
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class MergeExample {

  public static void main(String[] args) {
    //declare the connection, statement, and result set objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      //register the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      //create a connection to the database
      conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");

      //create a statement object
      stmt = conn.createStatement();

      //write a SQL query that uses an inner join to merge data from two tables
      String sql = "SELECT e.name, e.salary, d.name AS department FROM employee e INNER JOIN department d ON e.dept_id = d.id";

      //execute the query and store the result in a result set object
      rs = stmt.executeQuery(sql);

      //iterate over the result set and print the data
      while (rs.next()) {
        //get the data from each column using the column name or index
        String name = rs.getString("name");
        double salary = rs.getDouble("salary");
        String department = rs.getString("department");

        //print the data
        System.out.println(name + "\t" + salary + "\t" + department);
      }
    } catch (ClassNotFoundException e) {
      //handle the exception for the JDBC driver
      e.printStackTrace();
    } catch (SQLException e) {
      //handle the exception for the SQL operations
      e.printStackTrace();
    } finally {
      //close the result set, statement, and connection objects
      try {
        if (rs != null) {
          rs.close();
        }
        if (stmt != null) {
          stmt.close();
        }
        if (conn != null) {
          conn.close();
        }
      } catch (SQLException e) {
        //handle the exception for closing the objects
        e.printStackTrace();
      }
    }
  }
}
```

- Here is an example of merging data from multiple tables in JDBC using a subquery:

```java
//import the required packages
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class MergeExample {

  public static void main(String[] args) {
    //declare the connection, statement, and result set objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      //register the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      //create a connection to the database
      conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb",