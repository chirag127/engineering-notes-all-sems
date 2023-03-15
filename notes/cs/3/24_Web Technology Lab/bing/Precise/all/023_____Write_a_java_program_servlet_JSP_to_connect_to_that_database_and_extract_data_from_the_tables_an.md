# Unit 5 - Design server site applications using JDDC, ODBC and section tracking API

In this unit, we will learn how to connect to a database and extract data from tables using Java, Servlets, and JSP. Here are the steps to follow:

1. **Set up the database connection:** To connect to a database, you need to set up a connection using the JDBC (Java Database Connectivity) or ODBC (Open Database Connectivity) API. You will need to provide the database URL, username, and password to establish the connection.

2. **Create a Statement object:** Once the connection is established, you need to create a Statement object to execute SQL queries.

3. **Execute the query:** Use the executeQuery() method of the Statement object to execute the SQL query and retrieve the data from the database.

4. **Process the ResultSet:** The executeQuery() method returns a ResultSet object that contains the data retrieved from the database. You can iterate through the ResultSet and extract the data from each row.

5. **Display the data:** Once you have extracted the data from the ResultSet, you can display it using JSP or Servlets.

Here is an example of a Java program that connects to a database and extracts data from a table:

```java
import java.sql.*;

public class DatabaseConnection {
    public static void main(String[] args) {
        // Replace with your database URL, username, and password
        String url = "jdbc:mysql://localhost:3306/database_name";
        String username = "username";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, username, password)) {
            String query = "SELECT * FROM table_name";
            try (Statement stmt = conn.createStatement();
                 ResultSet rs = stmt.executeQuery(query)) {
                while (rs.next()) {
                    // Extract data from each row
                    int id = rs.getInt("id");
                    String name = rs.getString("name");
                    // ...
                    System.out.println(id + ", " + name);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

This is a basic example of how to connect to a database and extract data from a table using Java. You can use similar steps to connect to a database and extract data using Servlets and JSP. Remember to close the database connection and any resources such as Statement and ResultSet objects when you are done to avoid resource leaks.