## Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

- JDBC (Java Database Connectivity) is an API that allows Java applications to interact with various types of databases using a standard interface.
- ODBC (Open Database Connectivity) is an older API that enables applications written in different languages and platforms to access databases using a common driver.
- JDBC-ODBC Bridge is a type of driver that acts as an interface between JDBC and ODBC, converting the JDBC calls to ODBC calls and vice versa.
- Section tracking API is an API that enables web applications to maintain state information across multiple requests from the same client, such as user preferences, shopping cart items, etc.
- To design server site applications using these APIs, one needs to follow these steps:

  - Choose a suitable database and install the corresponding JDBC or ODBC driver on the server.
  - Establish a connection to the database using the DriverManager class or the DataSource interface in JDBC, or the SQLConnect function in ODBC.
  - Create and execute SQL statements using the Statement, PreparedStatement, or CallableStatement classes in JDBC, or the SQLExecDirect or SQLPrepare functions in ODBC.
  - Process the results using the ResultSet class in JDBC, or the SQLFetch or SQLGetData functions in ODBC.
  - Close the connection and release the resources using the close method in JDBC, or the SQLDisconnect function in ODBC.
  - Implement section tracking using the HttpSession interface or the Cookie class in Java, or the Session or Application objects in ASP.NET.