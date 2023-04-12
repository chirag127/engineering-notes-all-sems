### Design and implement a simple servlet book query with the help of JDBC & SQL

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. JDBC is a Java API that allows Java programs to interact with databases using SQL commands. SQL is a language for querying and manipulating data in relational databases.

To design and implement a simple servlet book query with the help of JDBC & SQL, we need to follow these steps:

1. Create a database and a table for storing book information, such as title, author, price, etc. For example, we can use MySQL as the database and create a table called books with the following SQL statement:

```sql
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(50),
  author VARCHAR(50),
  price DECIMAL(10,2)
);
```

2. Insert some sample data into the books table using SQL statements, such as:

```sql
INSERT INTO books VALUES (1, 'Java: The Complete Reference', 'Herbert Schildt', 35.99);
INSERT INTO books VALUES (2, 'Head First Java', 'Kathy Sierra and Bert Bates', 29.99);
INSERT INTO books VALUES (3, 'Effective Java', 'Joshua Bloch', 39.99);
```

3. Download and install a web server that supports servlets, such as Apache Tomcat, and configure it to run on a specific port, such as 8080. Also, download and copy the JDBC driver for MySQL, such as mysql-connector.jar, to the lib folder of Tomcat.

4. Create a Java project in an IDE, such as Eclipse, and add the servlet-api.jar and mysql-connector.jar to the build path. Also, create a web.xml file in the WEB-INF folder of the project and define the servlet name, class, and URL mapping. For example, we can create a servlet called BookServlet that handles requests to /books URL:

```xml
<web-app>
  <servlet>
    <servlet-name>BookServlet</servlet-name>
    <servlet-class>com.example.BookServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>BookServlet</servlet-name>
    <url-pattern>/books</url-pattern>
  </servlet-mapping>
</web-app>
```

5. Create a Java class that extends HttpServlet and overrides the doGet method to handle GET requests to /books URL. In the doGet method, we need to:

  - Get the request parameter for the book title, if any, and store it in a variable, such as title.
  - Load the JDBC driver and establish a connection to the MySQL database using the DriverManager class and the connection URL, username, and password. For example:

  ```java
  Class.forName("com.mysql.jdbc.Driver");
  Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/bookdb", "root", "password");
  ```

  - Create a SQL SELECT query to fetch the book information from the books table based on the title parameter, if any, or fetch all the books otherwise. For example:

  ```java
  String sql = "SELECT * FROM books";
  if (title != null && !title.isEmpty()) {
    sql += " WHERE title LIKE ?";
  }
  ```

  - Create a PreparedStatement object from the connection and set the title parameter, if any, using the setString method. For example:

  ```java
  PreparedStatement ps = con.prepareStatement(sql);
  if (title != null && !title.isEmpty()) {
    ps.setString(1, "%" + title + "%");
  }
  ```

  - Execute the query and get the ResultSet object that contains the book information. For example:

  ```java
  ResultSet rs = ps.executeQuery();
  ```

  - Get the response object and set the content type to text/html. For example:

  ```java
  HttpServletResponse response = (HttpServletResponse) resp;
  response.setContentType("text/html");
  ```

  - Get the PrintWriter object from the response and write the HTML code to display the book information in a table. For example:

  ```java
  PrintWriter out = response.getWriter();
  out.println("<html><head><title>Book Query</title></head><body>");
  out.println("<h1>Book Query</h1>");
  out.println("<form method='get' action='/books'>");
  out.println("Enter book title: <input type='text' name='title'>");
  out.println("<input type='submit'

```
