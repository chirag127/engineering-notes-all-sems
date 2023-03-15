### Authenticate the user when he submits the login form using the user name and password from the database for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To authenticate the user when he submits the login form, we need to use JDBC (Java Database Connectivity) and ODBC (Open Database Connectivity) drivers to connect to the database and execute SQL queries to verify the user name and password.
- JDBC and ODBC are APIs (Application Programming Interfaces) that allow Java applications to interact with various types of databases using a standard interface.
- JDBC and ODBC drivers are software components that implement the API and provide the connection details and functionality for a specific database.
- To use JDBC and ODBC drivers, we need to import the relevant packages, such as `java.sql` and `javax.sql` for JDBC, and `sun.jdbc.odbc` for ODBC.
- We also need to set up a data source name (DSN) for the database we want to connect to, using the administrative tools of the operating system or the database management system. A DSN is a name that identifies the database and its connection parameters, such as the server name, the port number, the database name, the user name, and the password.
- To connect to the database using JDBC, we need to use the `DriverManager` class and its `getConnection` method, which takes a JDBC URL as a parameter. A JDBC URL is a string that specifies the type of driver, the DSN, and optionally some additional parameters, such as the authentication method. For example, a JDBC URL for Oracle database using ODBC driver and IAM authentication could look like this:

```java
jdbc:odbc:iam:dsnlogin;UID=system;PWD=pintu
```

- To connect to the database using ODBC, we need to use the `JdbcOdbcDriver` class and its `connect` method, which takes a DSN and a `Properties` object as parameters. The `Properties` object contains the user name and password for the database. For example, a connection using ODBC driver and IAM authentication could look like this:

```java
JdbcOdbcDriver driver = new JdbcOdbcDriver();
Properties props = new Properties();
props.put("UID", "system");
props.put("PWD", "pintu");
Connection conn = driver.connect("dsnlogin", props);
```

- Once we have a `Connection` object, we can use it to create a `Statement` object and execute SQL queries using its `executeQuery` method. The `executeQuery` method returns a `ResultSet` object, which contains the data returned by the query. For example, to verify the user name and password from the login table, we could use a query like this:

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM login WHERE uname = '" + username + "' AND pass = '" + password + "'");
```

- To check if the query returned any results, we can use the `next` method of the `ResultSet` object, which moves the cursor to the next row of data and returns true if there is one, or false if there is none. For example, to display a welcome message if the user name and password are valid, or an error message if they are not, we could use a code like this:

```java
if (rs.next()) {
  System.out.println("Welcome: " + username);
} else {
  System.out.println("Invalid user name and password");
}
```

- To use session tracking API, we need to import the `javax.servlet.http` package, which contains the classes and interfaces for managing HTTP sessions. A session is a way of maintaining the state of a user across multiple requests to a web application. A session is identified by a unique ID, which is usually stored in a cookie or a URL parameter.
- To create a session, we need to use the `getSession` method of the `HttpServletRequest` object, which takes a boolean parameter that indicates whether to create a new session if none exists, or to return null if none exists. For example, to create a session for a user who has logged in successfully, we could use a code like this:

```java
HttpSession session = request.getSession(true);
session.setAttribute("username", username);
```

- To access the session, we need to use the `getSession` method again, but with a false parameter, which returns the existing session or null if none exists. For example, to get the user