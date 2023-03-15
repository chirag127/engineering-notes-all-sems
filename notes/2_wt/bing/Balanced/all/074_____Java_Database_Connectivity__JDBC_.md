# Java Database Connectivity (JDBC)

- JDBC is an API (Application Programming Interface) that allows Java programs to interact with databases .
- JDBC provides a set of classes and interfaces that define how a client can access a database, issue queries and commands, and handle the results .
- JDBC supports various types of data sources, such as relational databases, spreadsheets, and flat files.
- JDBC uses drivers to connect to different databases. A driver is a software component that implements the JDBC API for a specific database vendor .
- There are four types of JDBC drivers: JDBC-ODBC Bridge Driver, Native Driver, Network Protocol Driver, and Thin Driver.
- To establish a connection to a database, a Java program needs to use a database connection URL, which is a string that specifies the location, name, and configuration of the database.
- A typical JDBC program consists of the following steps: loading the driver, creating a connection, creating a statement, executing a query, processing the result set, and closing the resources .