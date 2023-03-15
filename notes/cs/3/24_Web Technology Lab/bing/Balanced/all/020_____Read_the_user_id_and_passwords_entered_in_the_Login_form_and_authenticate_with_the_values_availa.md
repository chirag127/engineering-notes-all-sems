# Read the user id and passwords entered in the Login form and authenticate with the values available in the cookies for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To read the user id and password from the login form in Java, you can use the `request.getParameter()` method to get the values entered by the user in the HTML input fields. For example, if your login form has `<input type="text" name="userid">` and `<input type="password" name="password">`, you can get the user id and password as follows:

```java
String userid = request.getParameter("userid");
String password = request.getParameter("password");
```

- To authenticate the user id and password with the values available in the cookies, you can use the `request.getCookies()` method to get an array of `Cookie` objects that represent the cookies sent by the browser. You can then iterate over the array and compare the cookie names and values with the user id and password. For example, if your cookies have the names "userid" and "password", you can do something like this:

```java
Cookie[] cookies = request.getCookies();
boolean authenticated = false;
if (cookies != null) {
  for (Cookie cookie : cookies) {
    if (cookie.getName().equals("userid") && cookie.getValue().equals(userid)) {
      authenticated = true;
    }
    if (cookie.getName().equals("password") && cookie.getValue().equals(password)) {
      authenticated = true;
    }
  }
}
if (authenticated) {
  // proceed to the next page
} else {
  // redirect to the login page with an error message
}
```

- To design server-side applications using JDBC, ODBC and session tracking API, you can follow these steps:

  - JDBC (Java Database Connectivity) is an API that allows Java programs to interact with various types of databases. You can use JDBC to establish a connection to a database, execute SQL queries and statements, and process the results. To use JDBC, you need to have a JDBC driver that matches your database type and version. You can then use the `DriverManager` class to get a `Connection` object that represents the database connection. For example, to connect to a MySQL database, you can do something like this:

  ```java
  // load the MySQL JDBC driver
  Class.forName("com.mysql.jdbc.Driver");
  // get the database connection using the driver, the URL, the user name and the password
  Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "password");
  ```

  - ODBC (Open Database Connectivity) is a standard that allows applications to access data from various types of databases. You can use ODBC to connect to a database that has an ODBC driver installed on your system. You can then use the `DriverManager` class to get a `Connection` object that represents the database connection. For example, to connect to a Microsoft Access database, you can do something like this:

  ```java
  // load the ODBC driver
  Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
  // get the database connection using the driver and the data source name (DSN)
  Connection con = DriverManager.getConnection("jdbc:odbc:mydsn");
  ```

  - Session tracking API is a set of classes and interfaces that allow you to maintain the state of a user across multiple requests. You can use session tracking API to store and retrieve information about a user, such as their preferences, shopping cart items, etc. You can use the `HttpSession` interface to represent a session object that is associated with a user. You can get the session object from the `request` object using the `getSession()` method. You can then use the `setAttribute()` and `getAttribute()` methods to store and retrieve data in the session object. For example, to store the user name in the session object, you can do something like this:

  ```java
  // get the session object, creating a new one if it does not exist
  HttpSession session = request.getSession(true);
  // store the user name in the session object
  session.setAttribute("username", userid);
  ```

  - To retrieve the user name from the session object, you can do something like this:

  ```java
  // get the session object, returning null if it does not exist
  HttpSession session = request.getSession(false);
  if (session != null) {
    // get the user name from