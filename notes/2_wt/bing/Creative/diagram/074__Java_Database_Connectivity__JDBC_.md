Java Database Connectivity (JDBC) is a standard Java API for database-independent connectivity between the Java programming language and a wide range of databases. JDBC supports both two-tier and three-tier processing models for database access.

### Java Database Connectivity (JDBC)

```
+---------------------+    +---------------------+    +---------------------+
|                     |    |                     |    |                     |
|   Java Application  |    |   JDBC Driver       |    |   Database Server   |
|                     |    |                     |    |                     |
+---------------------+    +---------------------+    +---------------------+
|                     |    |                     |    |                     |
|   JDBC API          |<-->|   JDBC Driver       |<-->|   Database          |
|                     |    |   Manager           |    |                     |
+---------------------+    +---------------------+    +---------------------+
|                     |    |                     |    |                     |
|   JDBC Driver       |<-->|   JDBC-Net          |<-->|   JDBC Driver       |
|   Interface         |    |   Pure Java         |    |   Native-Protocol   |
|                     |    |                     |    |                     |
+---------------------+    +---------------------+    +---------------------+
|                     |    |                     |    |                     |
|   JDBC Driver       |<-->|   JDBC-Net          |<-->|   Middleware        |
|   Interface         |    |   Pure Java         |    |   (RMI, CORBA, etc) |
|                     |    |                     |    |                     |
+---------------------+    +---------------------+    +---------------------+
|                     |    |                     |    |                     |
|   JDBC Driver       |<-->|   Native-API        |<-->|   Database API      |
|   Interface         |    |   Partly Java       |    |                     |
|                     |    |                     |    |                     |
+---------------------+    +---------------------+    +---------------------+
|                     |    |                     |    |                     |
|   JDBC Driver       |<-->|   Native-API        |<-->|   ODBC Driver       |
|   Interface         |    |   Partly Java       |    |                     |
|                     |    |                     |    |                     |
+---------------------+    +---------------------+    +---------------------+
```

The JDBC API provides a set of interfaces and classes to connect to different databases and execute SQL statements. The JDBC Driver Manager is responsible for loading the appropriate driver for each database and establishing the connection. The JDBC Driver is a software component that enables the communication between the Java application and the database server. There are four types of JDBC drivers:

- JDBC-ODBC Bridge Driver: This driver uses the ODBC driver to connect to the database. It is not recommended for production use as it is slow and platform-dependent.
- Native-API Driver: This driver uses the native database API to connect to the database. It is faster than the JDBC-ODBC Bridge Driver, but still platform-dependent and requires native libraries to be installed on the client machine.
- Network Protocol Driver: This driver uses a network protocol to communicate with a middleware server that then connects to the database. It is platform-independent and can access multiple databases, but adds an extra layer of complexity and overhead.
- Thin Driver: This driver is a pure Java driver that directly connects to the database using the database-specific protocol. It is the most portable and efficient driver, but requires the database server to support the network protocol.