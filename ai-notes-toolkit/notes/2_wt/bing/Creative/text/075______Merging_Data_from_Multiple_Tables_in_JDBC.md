#### Merging Data from Multiple Tables in JDBC

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases.
- One of the common tasks in JDBC is to merge data from multiple tables, which can be done using SQL queries that join the tables based on some common attributes or conditions.
- There are different types of joins in SQL, such as inner join, left join, right join, full join, cross join, etc. Each type of join has a different syntax and result set, depending on how the tables are related and what data is required.
- To merge data from multiple tables in JDBC, the following steps are needed:
  - Create a Connection object that represents the connection to the database.
  - Create a Statement object that can execute SQL queries on the database.
  - Write a SQL query that joins the tables using the appropriate join type and conditions.
  - Execute the query using the executeQuery() method of the Statement object, which returns a ResultSet object that contains the merged data.
  - Iterate over the ResultSet object using the next() method and the getXXX() methods to access the data in each row and column.
  - Close the ResultSet, Statement, and Connection objects to release the resources.
- Here is an example of merging data from two tables in JDBC using an inner join:

```java
// Assume that the tables are as follows:
// Employee (emp_id, name, dept_id, salary)
// Department (dept_id, dept_name, location)

// Import the required packages
import java.sql.*;

public class MergeExample {

  public static void main(String[] args) {
    // Declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      // Load the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      // Establish the connection to the database
      conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");

      // Create the statement object
      stmt = conn.createStatement();

      // Write the SQL query that joins the tables
      String sql = "SELECT e.name, e.salary, d.dept_name, d.location FROM Employee e INNER JOIN Department d ON e.dept_id = d.dept_id";

      // Execute the query and get the result set
      rs = stmt.executeQuery(sql);

      // Iterate over the result set and print the data
      while (rs.next()) {
        // Get the data from each column using the column name or index
        String name = rs.getString("name");
        double salary = rs.getDouble("salary");
        String dept_name = rs.getString("dept_name");
        String location = rs.getString("location");

        // Print the data
        System.out.println(name + "\t" + salary + "\t" + dept_name + "\t" + location);
      }
    } catch (Exception e) {
      // Handle any errors
      e.printStackTrace();
    } finally {
      // Close the JDBC objects
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
      } catch (SQLException se) {
        se.printStackTrace();
      }
    }
  }
}
```