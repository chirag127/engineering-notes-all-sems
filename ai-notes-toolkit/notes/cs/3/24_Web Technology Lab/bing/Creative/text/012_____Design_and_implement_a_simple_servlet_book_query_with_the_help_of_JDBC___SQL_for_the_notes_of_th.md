### Design and implement a simple servlet book query with the help of JDBC & SQL

A servlet is a Java class that runs on a web server and handles HTTP requests and responses. JDBC is a Java API that allows Java programs to interact with databases using SQL commands. SQL is a language for querying and manipulating data in relational databases.

To design and implement a simple servlet book query with the help of JDBC & SQL, we need to follow these steps:

1. Create a database and a table to store the book information. For example, we can use MySQL as the database and create a table called books with columns id, title, author, price and genre.
2. Download and install a web server that supports servlets, such as Apache Tomcat. Also, download and add the JDBC driver for MySQL to the web server's classpath. For example, we can download the mysql-connector.jar file from the internet and copy it to the lib folder of Tomcat.
3. Create a servlet class that extends the HttpServlet class and overrides the doGet or doPost method. In this method, we need to do the following:
  - Get the parameters from the HTTP request, such as the book id or the book genre.
  - Load the JDBC driver and establish a connection to the database using the DriverManager class.
  - Create a SQL query to select the books that match the parameters using the PreparedStatement class.
  - Execute the query and get the result set using the executeQuery and getResultSet methods.
  - Iterate over the result set and extract the book information using the getString, getInt and getDouble methods.
  - Create an HTML table to display the book information using the PrintWriter class.
  - Close the result set, the statement and the connection using the close method.
4. Create a web.xml file that maps the servlet class to a URL pattern. For example, we can map the servlet class to /bookquery.
5. Create a HTML file that contains a form to submit the parameters to the servlet. For example, we can create a form that has input fields for the book id and the book genre, and a submit button that sends the request to /bookquery.
6. Deploy the servlet class, the web.xml file and the HTML file to the web server's webapps folder. For example, we can create a folder called bookquery and copy the files to it.
7. Run the web server and access the HTML file from a web browser. For example, we can access http://localhost:8080/bookquery/index.html and enter some parameters to see the book query results.