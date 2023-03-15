### Design and implement a simple servlet book query with the help of JDBC & SQL

- A servlet is a Java class that runs on a web server and handles HTTP requests and responses.
- JDBC (Java Database Connectivity) is an API that allows Java programs to interact with various types of databases using SQL (Structured Query Language) commands.
- To design and implement a simple servlet book query with the help of JDBC & SQL, the following steps are required:

  1. Set up the JDBC environment and the database. Download the mysql-connector.jar file from the internet and move it to the apache-tomcat server folder. Create a database named `books` and a table named `book` with the following schema:

  | Column | Type | Description |
  | ------ | ---- | ----------- |
  | id | int | The primary key of the book |
  | title | varchar(50) | The title of the book |
  | author | varchar(50) | The author of the book |
  | price | double | The price of the book |

  2. Create a servlet class that extends the `HttpServlet` class and overrides the `doGet` method. The `doGet` method should perform the following tasks:

    - Get the book id from the request parameter using the `request.getParameter` method.
    - Load the JDBC driver using the `Class.forName` method with the driver class name as the argument.
    - Establish a connection to the database using the `DriverManager.getConnection` method with the database URL, username and password as the arguments.
    - Prepare a SQL select query to fetch the book details from the `book` table using the `Connection.prepareStatement` method with the query string as the argument. The query string should use a placeholder (`?`) for the book id and set it using the `PreparedStatement.setInt` method with the index and the book id as the arguments.
    - Execute the query using the `PreparedStatement.executeQuery` method and store the result in a `ResultSet` object.
    - Check if the result set is not empty using the `ResultSet.next` method and get the book details using the `ResultSet.getString` and `ResultSet.getDouble` methods with the column names as the arguments.
    - Set the content type of the response to `text/html` using the `response.setContentType` method.
    - Get the output stream of the response using the `response.getWriter` method and store it in a `PrintWriter` object.
    - Write the HTML code to display the book details in a table using the `PrintWriter.println` method. If the result set is empty, write a message to indicate that the book is not found.
    - Close the result set, the prepared statement and the connection using the `close` method.

  3. Compile the servlet class and place the class file in the `WEB-INF/classes` folder of the web application.
  4. Create a web.xml file in the `WEB-INF` folder of the web application and define the servlet and the servlet mapping using the `<servlet>` and `<servlet-mapping>` tags. The servlet name, the servlet class and the URL pattern should be specified as the child elements of the respective tags.