### Program to illustrate JDBC connectivity for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab.

JDBC or Java Database Connectivity is a standard API that enables Java applications to interact with various databases. In this program, we will illustrate how to establish JDBC connectivity to a database using Java.

Here are the steps to illustrate JDBC connectivity:

1. Import the required packages: 
To use JDBC, we need to import the required packages. These packages can be found in the java.sql package. 

2. Load the driver class: 
To establish a JDBC connection, we need to load the driver class using the Class.forName() method. 

3. Create a connection object: 
To connect to a database, we need to create a Connection object. We can create a Connection object using the DriverManager.getConnection() method. 

4. Create a statement object: 
To execute SQL queries, we need to create a Statement object. We can create a Statement object using the Connection.createStatement() method. 

5. Execute the query: 
Once we have a Statement object, we can execute SQL queries using the executeQuery() method. 

6. Process the results: 
Once we have executed the query, we can process the results using the ResultSet object. 

Here is a sample code to illustrate JDBC connectivity:

```
import java.sql.*;

public class JdbcExample {
   public static void main(String[] args) {
      try {
         // Load the driver class
         Class.forName("com.mysql.jdbc.Driver");

         // Create a connection object
         Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "root", "password");

         // Create a statement object
         Statement stmt = con.createStatement();

         // Execute the query
         ResultSet rs = stmt.executeQuery("SELECT * FROM mytable");

         // Process the results
         while (rs.next()) {
            System.out.println(rs.getInt(1) + "  " + rs.getString(2));
         }

         // Close the connection
         con.close();
      } catch (Exception e) {
         System.out.println(e);
      }
   }
}
```

In this program, we have loaded the MySQL JDBC driver, created a connection object to a database named "mydatabase", created a statement object to execute SQL queries, executed a select query to fetch data from a table named "mytable", and processed the results using a ResultSet object.

This program can be used as a reference for establishing JDBC connectivity in ASP, JSP, or PHP based dynamic web pages.