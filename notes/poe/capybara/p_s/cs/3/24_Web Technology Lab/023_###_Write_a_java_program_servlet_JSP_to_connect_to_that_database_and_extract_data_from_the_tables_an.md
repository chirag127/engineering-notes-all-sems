### Write a Java Program/Servlet/JSP to Connect to That Database and Extract Data from the Tables and Display Them

When designing server site applications using JDDC, ODBC, and section tracking API, it's important to know how to connect to a database, extract data from tables, and display the information in a readable format. This is where Java programming comes in. In this section, we'll cover how to write a Java program, servlet, or JSP to connect to a database, extract data from tables, and display the information.

First, let's define what each of these terms mean:

- Java program: A program written in the Java programming language that can be executed on any platform with a Java Virtual Machine (JVM).
- Servlet: A server-side program that runs on a web server and handles client requests and responses.
- JSP: A server-side web page that can generate dynamic content.

Now, let's look at the steps involved in writing a Java program, servlet, or JSP to connect to a database, extract data from tables, and display the information.

1. Import the required packages: Before you start writing the code, you need to import the required packages. For example, to use JDBC (Java Database Connectivity), you need to import the java.sql package.

2. Load the database driver: Once you've imported the required packages, you need to load the database driver. The database driver is a software component that enables Java applications to interact with a database. To load the driver, you can use the Class.forName() method.

3. Establish a connection to the database: After loading the driver, you need to establish a connection to the database. To do this, you can use the DriverManager.getConnection() method.

4. Create a statement object: Once you've established a connection to the database, you need to create a statement object. The statement object is used to execute SQL statements.

5. Execute the SQL query: After creating the statement object, you need to execute the SQL query. This can be done using the statement.executeQuery() method.

6. Process the results: Once you've executed the SQL query, you need to process the results. This can be done using a while loop to iterate through the ResultSet object returned by the query.

7. Display the results: Finally, you need to display the results in a readable format. This can be done using HTML, JSP tags, or other web technologies.

Here's an example Java program that connects to a MySQL database, extracts data from a table, and displays the results:

```
import java.sql.*;

public class DBConnect {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/mydatabase", "username", "password");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM customers");
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " " + rs.getString("name"));
            }
            conn.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

In this example, we're using the com.mysql.jdbc.Driver driver to connect to a MySQL database. We're also using the Statement and ResultSet objects to execute a SELECT statement and retrieve the results.

Overall, writing a Java program, servlet, or JSP to connect to a database, extract data from tables, and display the information is an important skill for web developers. By following the steps outlined in this section and practicing with examples, you can become proficient in using JDBC, ODBC, and other database technologies to build robust server-side applications.