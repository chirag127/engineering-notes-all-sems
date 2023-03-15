### Design and implement a simple servlet book query with the help of JDBC & SQL

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. JDBC is a Java API that allows Java programs to interact with databases using SQL commands. SQL is a language for querying and manipulating data in relational databases.

To design and implement a simple servlet book query with the help of JDBC & SQL, we need to follow these steps:

- Create a database and a table to store the book information, such as title, author, price, etc. For example, we can use MySQL as the database and create a table called books with the following SQL statement:

```sql
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(50),
  author VARCHAR(50),
  price DECIMAL(10,2)
);
```

- Insert some sample data into the books table using SQL statements, such as:

```sql
INSERT INTO books VALUES (1, 'Java: The Complete Reference', 'Herbert Schildt', 39.99);
INSERT INTO books VALUES (2, 'Head First Java', 'Kathy Sierra and Bert Bates', 29.99);
INSERT INTO books VALUES (3, 'Effective Java', 'Joshua Bloch', 49.99);
```

- Download and install a web server that supports servlets, such as Apache Tomcat, and configure it to run on a specific port, such as 8080.
- Download and copy the JDBC driver for the database, such as mysql-connector.jar, to the web server's lib folder, such as apache-tomcat/lib.
- Create a Java servlet class that extends HttpServlet and overrides the doGet method to handle the HTTP GET requests. In the doGet method, we need to:

  - Get the HTTP request parameters, such as the book id, from the request object.
  - Load the JDBC driver class and establish a connection to the database using the DriverManager class and the connection URL, username, and password.
  - Create a SQL SELECT query to fetch the book information from the books table based on the book id parameter.
  - Execute the query using a PreparedStatement object and store the result in a ResultSet object.
  - Set the content type of the HTTP response to text/html using the response object.
  - Get the PrintWriter object from the response object to write the HTML output to the browser.
  - Write the HTML code to display the book information in a table format, such as:

```html
<html>
<head>
  <title>Book Query</title>
</head>
<body>
  <h1>Book Query</h1>
  <table border="1">
    <tr>
      <th>ID</th>
      <th>Title</th>
      <th>Author</th>
      <th>Price</th>
    </tr>
    <tr>
      <td>1</td>
      <td>Java: The Complete Reference</td>
      <td>Herbert Schildt</td>
      <td>39.99</td>
    </tr>
  </table>
</body>
</html>
```

  - Close the ResultSet, PreparedStatement, and Connection objects to release the resources.

- Compile the servlet class and copy the class file to the web server's webapps folder, such as apache-tomcat/webapps/ROOT/WEB-INF/classes.
- Create a web.xml file in the web server's webapps folder, such as apache-tomcat/webapps/ROOT/WEB-INF, to map the servlet class to a URL pattern, such as /bookquery. For example, the web.xml file can look like this:

```xml
<web-app>
  <servlet>
    <servlet-name>BookQueryServlet</servlet-name>
    <servlet-class>BookQueryServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>BookQueryServlet</servlet-name>
    <url-pattern>/bookquery</url-pattern>
  </servlet-mapping>
</web-app>
```
