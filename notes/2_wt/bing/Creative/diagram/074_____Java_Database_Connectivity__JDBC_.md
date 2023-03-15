Java Database Connectivity (JDBC) is a standard Java API that allows Java programs to access various types of databases. JDBC supports both two-tier and three-tier models for database access. The basic JDBC architecture consists of two layers:

- JDBC API: This layer provides the application with methods to connect to the database, execute queries and commands, and handle the results. The JDBC API also defines the interfaces and classes that the application uses to interact with the JDBC driver.
- JDBC Driver: This layer implements the JDBC API for a specific database. The JDBC driver communicates with the database server and converts the JDBC calls into the database-specific protocol. The JDBC driver can be either a Type 1 driver that uses a bridge to connect to another data access API, a Type 2 driver that uses a native library to connect to the database, a Type 3 driver that uses a middleware server to connect to the database, or a Type 4 driver that uses a pure Java implementation to connect to the database.

The following diagram shows the JDBC architecture in a two-tier model, where a Java application or applet directly communicates with the database through the JDBC driver.

### Java Database Connectivity (JDBC)

```
+-----------------+        +-----------------+
| Java Application|        | Database Server |
| or Applet       |        |                 |
+-----------------+        +-----------------+
        |                          ^
        | JDBC API                 | Database-specific protocol
        v                          |
+-----------------+        +-----------------+
| JDBC Driver     |<------>| Database        |
|                 |        |                 |
+-----------------+        +-----------------+
```