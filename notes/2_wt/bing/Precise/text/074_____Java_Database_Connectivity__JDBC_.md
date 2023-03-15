### Java Database Connectivity (JDBC)

- JDBC (Java Database Connectivity) is the Java API that manages connecting to a database, issuing queries and commands, and handling result sets obtained from the database.
- Released as part of JDK 1.1 in 1997, JDBC was one of the earliest libraries developed for the Java language.
- It is a Java-based data access technology used for Java database connectivity and is part of the Java Standard Edition platform, from Oracle Corporation.
- JDBC allows multiple implementations to exist and be used by the same application. The API provides a mechanism for dynamically loading the correct Java packages and registering them with the JDBC Driver Manager. The Driver Manager is used as a connection factory for creating JDBC connections.
- Using the JDBC API, you can access virtually any data source, from relational databases to spreadsheets and flat files. JDBC technology also provides a common base on which tools and alternate interfaces can be built.
- JDBC API uses JDBC drivers to connect with the database. There are four types of JDBC drivers: JDBC-ODBC Bridge Driver, Native Driver, Network Protocol Driver, and Thin Driver.
- A database connection URL is a string that your DBMS JDBC driver uses to connect to a database. It can contain information such as where to search for the database, the name of the database to connect to, and configuration properties. The exact syntax of a database connection URL is specified by your DBMS.