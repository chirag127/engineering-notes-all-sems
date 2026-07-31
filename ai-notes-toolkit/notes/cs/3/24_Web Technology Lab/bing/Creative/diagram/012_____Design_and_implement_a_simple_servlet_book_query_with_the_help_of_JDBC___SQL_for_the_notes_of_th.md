### Design and implement a simple servlet book query with the help of JDBC & SQL

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. JDBC is a Java API that allows Java programs to interact with databases using SQL commands. SQL is a language for querying and manipulating data in relational databases.

To design and implement a simple servlet book query with the help of JDBC & SQL, we need to follow these steps:

1. Create a database and a table for storing book information, such as title, author, price, etc. For example, we can use MySQL as the database and create a table called books with the following SQL command:

```sql
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  author VARCHAR(50) NOT NULL,
  price DECIMAL(10,2) NOT NULL
);
```

2. Insert some sample data into the books table using SQL commands. For example, we can insert three books with the following SQL commands:

```sql
INSERT INTO books VALUES (1, 'Java: The Complete Reference', 'Herbert Schildt', 39.99);
INSERT INTO books VALUES (2, 'Head First Java', 'Kathy Sierra and Bert Bates', 29.99);
INSERT INTO books VALUES (3, 'Effective Java', 'Joshua Bloch', 49.99);
```

3. Download and install a web server that supports servlets, such as Apache Tomcat. Also, download and install a JDBC driver for the database, such as mysql-connector.jar for MySQL. Copy the JDBC driver jar file to the lib folder of the web server.

4. Create a Java project in an IDE, such as Eclipse, and add the web server and the JDBC driver to the build path. Create a dynamic web project and a servlet class in the project. For example, we can create a project called BookQuery and a servlet class called BookServlet.

5. Write the code for the servlet class to handle HTTP requests and responses. The servlet class should do the following tasks:

  - Load the JDBC driver and establish a connection to the database using the connection URL, username and password.
  - Create a SQL statement to query the books table and execute it using a JDBC ResultSet object.
  - Iterate over the ResultSet object and extract the book information from each row.
  - Create an HTML table to display the book information in the HTTP response.
  - Close the ResultSet, the statement and the connection objects.

For example, the code for the servlet class could look something like this:

```java
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class BookServlet extends HttpServlet {

  private static final long serialVersionUID = 1L;

  // Database connection parameters
  private static final String DB_URL = "jdbc:mysql://localhost:3306/bookdb";
  private static final String DB_USER = "root";
  private static final String DB_PASS = "root";

  // JDBC objects
  private Connection conn = null;
  private Statement stmt = null;
  private ResultSet rs = null;

  // SQL query
  private static final String SQL_QUERY = "SELECT * FROM books";

  // HTML table header
  private static final String HTML_TABLE_HEADER = "<table border='1'>"
      + "<tr><th>ID</th><th>Title</th><th>Author</th><th>Price</th></tr>";

  // HTML table footer
  private static final String HTML_TABLE_FOOTER = "</table>";

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {

    // Set the content type and the character encoding of the response
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the PrintWriter object to write the response
    PrintWriter out = response.getWriter();

    try {
      // Load the JDBC driver
      Class.forName("com.mysql.jdbc.Driver");

      // Get the connection to the database
      conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

      // Create the statement object
      stmt = conn.createStatement();

      // Execute the SQL query and get the result set
      rs = stmt.executeQuery(SQL_QUERY);

      // Write the HTML table header to the response
      out.println(HTML_TABLE_HEADER);

      // Loop through the result set and write each row to the response
      while (rs

```
