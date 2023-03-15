#### Databases with JDBC in JDBC

- JDBC stands for Java Database Connectivity, which is an API for connecting and executing queries on databases from Java applications.
- JDBC provides a set of classes and interfaces that abstract the details of communication with different database systems, such as MySQL, Oracle, PostgreSQL, etc.
- To use JDBC, we need to have a JDBC driver for the specific database system we want to connect to. A JDBC driver is a software component that implements the JDBC API and enables Java applications to interact with the database.
- There are four types of JDBC drivers, each with different advantages and disadvantages:
  - Type 1: JDBC-ODBC bridge driver. This driver converts JDBC calls into ODBC calls and uses an ODBC driver to connect to the database. This driver is platform-dependent and requires an ODBC driver to be installed on the client machine.
  - Type 2: Native-API driver. This driver uses the native libraries of the database system to connect to the database. This driver is also platform-dependent and requires the native libraries to be available on the client machine.
  - Type 3: Network protocol driver. This driver uses a middleware server that converts JDBC calls into the database-specific protocol and forwards them to the database server. This driver is platform-independent but requires the middleware server to be installed and configured.
  - Type 4: Thin driver. This driver uses the database-specific protocol to communicate directly with the database server. This driver is platform-independent and does not require any additional software on the client machine.
- The JDBC URL is a string that specifies the location and properties of the database we want to connect to. The JDBC URL format can vary depending on the database system and the driver type, but it usually has the following structure:

  `jdbc:<subprotocol>:<subname>`

  where `<subprotocol>` is the name of the database system (such as mysql, oracle, postgresql, etc.) and `<subname>` is a database-specific string that can include the host, port, database name, user, password, and other parameters.

  For example, a JDBC URL for connecting to a MySQL database using a type 4 driver could look like this:

  `jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC`

- To connect to a database using JDBC, we need to perform the following steps:
  - Load the JDBC driver class using the `Class.forName()` method. This registers the driver with the `DriverManager` class, which manages the available drivers.
  - Obtain a connection object using the `DriverManager.getConnection()` method. This method takes the JDBC URL, the user name, and the password as arguments and returns a `Connection` object that represents the connection to the database.
  - Create a statement object using the `Connection.createStatement()` method. This method returns a `Statement` object that can be used to execute SQL queries on the database.
  - Execute the query using the `Statement.executeQuery()` method for queries that return a result set, such as `SELECT`, or the `Statement.executeUpdate()` method for queries that modify the database, such as `INSERT`, `UPDATE`, or `DELETE`. These methods take the SQL query as a string argument and return a `ResultSet` object or an integer value, respectively.
  - Process the result using the `ResultSet` object, which provides methods to access the data in each row and column of the result set.
  - Close the resources using the `close()` method of the `ResultSet`, `Statement`, and `Connection` objects. This releases the resources and closes the connection to the database.

- Here is an example of a Java program that connects to a MySQL database and executes a simple query using JDBC:

  ```java
  import java.sql.*;

  public class JDBCExample {

    public static void main(String[] args) {

      // JDBC driver name and database URL
      final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
      final String DB_URL = "jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC";

      // Database credentials
      final String USER = "root";
      final String PASS = "password";

      Connection conn = null;
      Statement stmt = null;
      ResultSet rs = null;

      try {
        // Step 1: Load the JDBC driver
        Class.forName(JDBC_DRIVER);

        // Step 2: Get the connection
        conn = DriverManager.getConnection(DB_URL, USER, PASS);

        // Step 3: Create the statement
        stmt = conn.createStatement();

        // Step 4: Execute the