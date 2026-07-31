# Design and implement a simple servlet book query with the help of JDBC & SQL

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- JDBC is a Java API that allows Java programs to interact with databases using SQL commands.
- SQL is a language for querying, manipulating, and analyzing data stored in relational databases.
- To design and implement a simple servlet book query with the help of JDBC & SQL, the following steps are required:

  1. Set up the database and the table that contains the book information, such as title, author, price, etc. You can use any relational database management system (RDBMS) that supports JDBC, such as MySQL, Oracle, PostgreSQL, etc. For example, you can create a database named `books` and a table named `book` with the following SQL commands:

  ```sql
  CREATE DATABASE books;
  USE books;
  CREATE TABLE book (
    id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL
  );
  ```

  2. Insert some sample data into the table using SQL `INSERT` statements. For example, you can insert three books with the following SQL commands:

  ```sql
  INSERT INTO book VALUES (1, 'Java: The Complete Reference', 'Herbert Schildt', 35.99);
  INSERT INTO book VALUES (2, 'Effective Java', 'Joshua Bloch', 29.99);
  INSERT INTO book VALUES (3, 'Head First Java', 'Kathy Sierra and Bert Bates', 39.99);
  ```

  3. Download the JDBC driver for your RDBMS and add it to the classpath of your web application. The JDBC driver is a Java library that enables the communication between the Java program and the database. You can find the JDBC driver for your RDBMS from the official website or a third-party source. For example, if you are using MySQL, you can download the MySQL Connector/J from https://dev.mysql.com/downloads/connector/j/. You can then copy the JAR file to the `WEB-INF/lib` folder of your web application.

  4. Create a Java servlet class that extends the `HttpServlet` class and overrides the `doGet` or `doPost` method. The servlet class should handle the HTTP request from the client, connect to the database using JDBC, execute the SQL query to retrieve the book information, and send the HTTP response to the client. For example, you can create a servlet class named `BookServlet` with the following code:

  ```java
  import java.io.IOException;
  import java.io.PrintWriter;
  import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.ResultSet;
  import java.sql.Statement;
  import javax.servlet.ServletException;
  import javax.servlet.annotation.WebServlet;
  import javax.servlet.http.HttpServlet;
  import javax.servlet.http.HttpServletRequest;
  import javax.servlet.http.HttpServletResponse;

  @WebServlet("/BookServlet")
  public class BookServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // Database URL, username and password
    private static final String DB_URL = "jdbc:mysql://localhost:3306/books";
    private static final String DB_USER = "root";
    private static final String DB_PASS = "root";

    // SQL query to select all books
    private static final String SQL_QUERY = "SELECT * FROM book";

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
      // Set the content type and character encoding of the response
      response.setContentType("text/html");
      response.setCharacterEncoding("UTF-8");

      // Get the output stream of the response
      PrintWriter out = response.getWriter();

      // Try to connect to the database and execute the query
      try {
        // Load the JDBC driver
        Class.forName("com.mysql.cj.jdbc.Driver");

        // Get a connection to the database
        Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

        // Create a statement object to execute the query
        Statement stmt = conn.createStatement();

        // Execute the query and get a result set object
        ResultSet rs = stmt.executeQuery(SQL_QUERY);

        // Print the HTML header
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Book Query</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h1>Book Query</h1>");

        // Check if the result set is not empty

```
