# Design and implement a simple servlet book query with the help of JDBC & SQL

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- JDBC (Java Database Connectivity) is an API that allows Java programs to interact with various types of databases using SQL (Structured Query Language) commands.
- To design and implement a simple servlet book query with the help of JDBC & SQL, the following steps are required:

  - Create a database and a table to store the book information, such as title, author, price, etc. For example, using MySQL, the following SQL commands can be used:

    ```sql
    CREATE DATABASE books;
    USE books;
    CREATE TABLE book (
      id INT PRIMARY KEY,
      title VARCHAR(50),
      author VARCHAR(50),
      price DECIMAL(10,2)
    );
    INSERT INTO book VALUES
    (1, 'Java: The Complete Reference', 'Herbert Schildt', 35.99),
    (2, 'Head First Java', 'Kathy Sierra and Bert Bates', 29.99),
    (3, 'Effective Java', 'Joshua Bloch', 39.99);
    ```

  - Download and install a web server that supports servlets, such as Apache Tomcat, and configure it to run on a specific port, such as 8080.
  - Download and add the JDBC driver for the database to the web server's classpath, such as mysql-connector.jar for MySQL.
  - Create a Java servlet class that extends HttpServlet and overrides the doGet or doPost method to handle the HTTP requests and responses. For example, the following servlet class can be used to query the book table and display the results in a HTML table:

    ```java
    import java.io.*;
    import java.sql.*;
    import javax.servlet.*;
    import javax.servlet.http.*;

    public class BookServlet extends HttpServlet {

      // JDBC driver name and database URL
      static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
      static final String DB_URL = "jdbc:mysql://localhost:3306/books";

      // Database credentials
      static final String USER = "root";
      static final String PASS = "password";

      // Method to handle GET requests
      public void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {

        // Set response content type
        response.setContentType("text/html");

        // Get the printwriter object from response to write the required html in the response
        PrintWriter out = response.getWriter();

        // Write the HTML header
        out.println("<html><head><title>Book Query</title></head><body>");

        // Write the HTML form to get the user input
        out.println("<form method='post' action='BookServlet'>");
        out.println("<p>Enter the book title or author name to search:</p>");
        out.println("<input type='text' name='query' required>");
        out.println("<input type='submit' value='Search'>");
        out.println("</form>");

        // Write the HTML footer
        out.println("</body></html>");
      }

      // Method to handle POST requests
      public void doPost(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {

        // Set response content type
        response.setContentType("text/html");

        // Get the printwriter object from response to write the required html in the response
        PrintWriter out = response.getWriter();

        // Write the HTML header
        out.println("<html><head><title>Book Query</title></head><body>");

        // Get the user input from the request
        String query = request.getParameter("query");

        // Declare JDBC objects
        Connection conn = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;

        try {
          // Register JDBC driver
          Class.forName(JDBC_DRIVER);

          // Open a connection
          conn = DriverManager.getConnection(DB_URL, USER, PASS);

          // Prepare a SQL statement to search the book table by title or author
          String sql = "SELECT * FROM book WHERE title LIKE ? OR author LIKE ?";
          stmt = conn.prepareStatement(sql);
          stmt.setString(1, "%" + query + "%");
          stmt.setString(2, "%" + query + "%");

          // Execute the query and get the result set
          rs = stmt.executeQuery();

          // Write the HTML table to display the query results
          out.println("<table border='1'>");
          out.println("<tr><th>ID</th><th>Title</th><th>Author</th><th>Price</th></tr>");

          // Loop through the result