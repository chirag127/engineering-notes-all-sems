## Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDBC stands for Java Database Connectivity, which is a standard Java API for connecting and executing queries with databases .
- ODBC stands for Open Database Connectivity, which is a standard C API for connecting and executing queries with databases  .
- JDBC-ODBC Bridge is a type of driver that acts as an interface between Java applications and databases that support ODBC.
- Section tracking API is a way of tracking the state of a user session across multiple requests and responses in a web application.
- To design server site applications using JDDC,ODBC and section tracking API, one needs to:
  - Choose a suitable JDBC driver for the database to be used, such as JDBC-ODBC Bridge, JDBC-Net, Native-API, or Native-Protocol .
  - Load the JDBC driver using the Class.forName() method and register it with the DriverManager class .
  - Establish a connection with the database using the DriverManager.getConnection() method and passing the URL, username, and password of the database .
  - Create a Statement, PreparedStatement, or CallableStatement object using the Connection.createStatement(), Connection.prepareStatement(), or Connection.prepareCall() methods respectively .
  - Execute the SQL queries using the Statement.execute(), Statement.executeQuery(), or Statement.executeUpdate() methods and obtain the ResultSet object for retrieving the data .
  - Process the ResultSet object using the methods such as ResultSet.next(), ResultSet.getString(), ResultSet.getInt(), etc. and close the ResultSet, Statement, and Connection objects when done .
  - Use the section tracking API to store and retrieve the user session information, such as user ID, preferences, shopping cart, etc. using the methods such as HttpSession.setAttribute(), HttpSession.getAttribute(), HttpSession.invalidate(), etc. and configure the web.xml file to enable session tracking.
  - Handle any exceptions that may occur during the database operations or the session tracking using the try-catch-finally blocks and the SQLException, ClassNotFoundException, or IOException classes  .