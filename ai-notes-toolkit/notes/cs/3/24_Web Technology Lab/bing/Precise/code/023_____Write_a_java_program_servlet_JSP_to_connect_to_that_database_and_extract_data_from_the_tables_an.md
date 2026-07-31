### Java Program to Connect to Database and Extract Data

Here is an example of a Java program that connects to a database and extracts data from tables to display:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class DatabaseConnection {
    public static void main(String[] args) {
        // Replace with your database URL, username, and password
        String url = "jdbc:mysql://localhost:3306/databaseName";
        String username = "username";
        String password = "password";

        try {
            // Load the JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            // Establish a connection to the database
            Connection conn = DriverManager.getConnection(url, username, password);

            // Create a statement object
            Statement stmt = conn.createStatement();

            // Execute a query and get a result set
            ResultSet rs = stmt.executeQuery("SELECT * FROM tableName");

            // Process the result set
            while (rs.next()) {
                // Get the data from the current row
                int id = rs.getInt("id");
                String name = rs.getString("name");
                // ...

                // Display the data
                System.out.println("ID: " + id + ", Name: " + name);
            }

            // Close the result set, statement, and connection
            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

This program uses the JDBC API to connect to a MySQL database, execute a query, and process the result set. You can modify the database URL, username, and password to match your database configuration.

In a servlet or JSP, you can use the same code to connect to the database and extract data. The only difference is that you would display the data in the response instead of printing it to the console.

For example, in a JSP, you could use the following code to display the data in an HTML table:

```jsp
<%@ page import="java.sql.*" %>
<%
    // Replace with your database URL, username, and password
    String url = "jdbc:mysql://localhost:3306/databaseName";
    String username = "username";
    String password = "password";

    try {
        // Load the JDBC driver
        Class.forName("com.mysql.jdbc.Driver");

        // Establish a connection to the database
        Connection conn = DriverManager.getConnection(url, username, password);

        // Create a statement object
        Statement stmt = conn.createStatement();

        // Execute a query and get a result set
        ResultSet rs = stmt.executeQuery("SELECT * FROM tableName");
%>
<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
    </tr>
<%
        // Process the result set
        while (rs.next()) {
            // Get the data from the current row
            int id = rs.getInt("id");
            String name = rs.getString("name");
            // ...
%>
    <tr>
        <td><%= id %></td>
        <td><%= name %></td>
    </tr>
<%
        }
%>
</table>
<%
        // Close the result set, statement, and connection
        rs.close();
        stmt.close();
        conn.close();
    } catch (Exception e) {
        e.printStackTrace();
    }
%>
```

This JSP uses scriptlets to connect to the database, execute a query, and process the result set. The data is then displayed in an HTML table using JSP expressions.

You can use similar code in a servlet by writing the HTML code to the response's output stream.

I hope this helps you understand how to connect to a database and extract data using Java, servlets, and JSPs. Let me know if you have any further questions.