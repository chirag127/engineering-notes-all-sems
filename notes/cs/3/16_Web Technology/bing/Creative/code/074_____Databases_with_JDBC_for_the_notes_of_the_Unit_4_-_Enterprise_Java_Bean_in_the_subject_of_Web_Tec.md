### Databases with JDBC

- JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases from Java applications.
- JDBC provides a common interface for sending SQL statements to any database that supports JDBC, such as MySQL, Oracle, SQL Server, etc.
- JDBC consists of two components: a JDBC driver and a JDBC API.
  - A JDBC driver is a software module that implements the JDBC interface for a specific database vendor. It enables Java applications to communicate with the database using the vendor-specific protocol.
  - A JDBC API is a set of classes and interfaces that define the methods and constants for accessing and manipulating data in a database.
- The steps for connecting to a database with JDBC are as follows:
  1. Install or locate the database you want to access.
  2. Include the JDBC library in your Java project.
  3. Ensure the JDBC driver you need is on your classpath.
  4. Use the JDBC library to obtain a connection to the database.
  5. Create a statement object to execute SQL queries.
  6. Process the result set returned by the queries.
  7. Close the connection and release the resources.
- The JDBC service in Google Apps Script supports Google Cloud SQL for MySQL, MySQL, Microsoft SQL Server, and Oracle databases. It allows you to update an external database with JDBC from your script.
- The JDBC service in Azure Databricks supports connecting to external databases using JDBC. It provides optimized integrations for syncing data with many external data sources. It also allows you to control the parallelism for JDBC queries and write data to JDBC tables.