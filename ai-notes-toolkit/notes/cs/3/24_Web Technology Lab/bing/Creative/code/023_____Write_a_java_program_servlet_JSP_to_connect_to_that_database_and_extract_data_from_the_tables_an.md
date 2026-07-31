# Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To connect to a database using Java, you need to use the JDBC (Java Database Connectivity) API, which provides a set of classes and interfaces to interact with various databases  .
- To use JDBC, you need to have a JDBC driver for the specific database you want to connect to, such as MySQL, Oracle, SQL Server, etc. The driver is a JAR file that implements the JDBC interfaces and communicates with the database server .
- To download the MySQL JDBC driver, you can go to the MySQL community downloads page and select the Connector/J option. Then, you can download the latest version of the JAR file and add it to your classpath when compiling and running your Java code.
- To connect to a MySQL database using JDBC, you need to follow these steps :
  - Load the MySQL JDBC driver class using the Class.forName() method, passing the fully qualified name of the driver class as a parameter. This will register the driver with the DriverManager class, which manages the available drivers and connections.
  - Create a Connection object using the DriverManager.getConnection() method, passing the URL of the database, the username and the password as parameters. The URL should have the format "jdbc:mysql://hostname:port/databaseName". The Connection object represents a physical connection to the database server.
  - Create a Statement object using the Connection.createStatement() method. The Statement object is used to execute SQL queries on the database.
  - Execute the SQL query using the Statement.executeQuery() method, passing the query string as a parameter. This will return a ResultSet object, which contains the data returned by the query. The ResultSet object has a cursor that points to the current row of data. You can use the ResultSet.next() method to move the cursor to the next row, and the ResultSet.getXXX() methods to get the values of the columns in the current row, where XXX is the data type of the column, such as getInt(), getString(), getDouble(), etc.
  - Close the ResultSet, Statement and Connection objects using the close() method. This will release the resources and terminate the connection to the database.

- To display the data from the ResultSet object, you can use a loop to iterate over the rows and print the values of the columns using the System.out.println() method. Alternatively, you can use a utility class such as DBTablePrinter to print the data in a table format.
- To write a servlet or a JSP to connect to a database and display data, you need to follow the same steps as above, but instead of printing the data to the standard output, you need to write the data to the response object, which represents the output stream to the client. You can use the response.setContentType() method to set the content type of the response, such as "text/html", and the response.getWriter() method to get a PrintWriter object, which can write text to the response. You can use HTML tags to format the data in a table or a list. You can also use JSP tags such as <sql:query>, <sql:result>, <sql:column>, etc. to simplify the database access and display.

- Here is an example of a Java program that connects to a MySQL database and displays the data from a table called employees:

```java
// Import the required packages
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DatabaseConnection {

  public static void main(String[] args) {
    // Declare the variables for the database connection
    String url = "jdbc:mysql://localhost:3306/mydb"; // The URL of the database
    String username = "root"; // The username of the database
    String password = "root"; // The password of the database
    Connection conn = null; // The connection object
    Statement stmt = null; // The statement object
    ResultSet rs = null; // The result set object

    try {
      // Load the MySQL JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");
      // Create a connection to the database
      conn = DriverManager.getConnection(url, username, password);
      // Create a statement to execute SQL queries
      stmt

```
