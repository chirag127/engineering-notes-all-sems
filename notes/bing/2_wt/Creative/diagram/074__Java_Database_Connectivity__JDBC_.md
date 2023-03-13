Java Database Connectivity (JDBC) is an API that allows Java programs to interact with various databases such as Oracle, MySQL, MS Access and SQL Server. JDBC supports both two-tier and three-tier processing models for database access.

### Java Database Connectivity (JDBC) Architecture

The JDBC architecture consists of four main components:

- The JDBC API: This defines the interfaces and classes that enable Java applications to execute SQL statements, process the results, and manage transactions.
- The JDBC Driver Manager: This is a class that manages the loading and registration of JDBC drivers, and provides a connection to a database through the appropriate driver.
- The JDBC Driver: This is a software component that implements the JDBC API for a specific database. It converts the JDBC calls into the database-specific protocol and communicates with the database server.
- The Database: This is the data source that stores the data and responds to the queries and updates from the JDBC driver.

The following diagram illustrates the basic architecture of a JDBC application:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  JDBC API       |      |  JDBC Driver    |      |  Database       |
|                 |      |  Manager        |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Java           |      |  JDBC-ODBC      |      |  ODBC Driver    |
|  Application    |----->|  Bridge         |----->|                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

In the two-tier model, the JDBC application communicates directly with the database through the JDBC driver. In the three-tier model, the JDBC application communicates with a middle-tier server that handles the database access and business logic, and the server communicates with the database through the JDBC driver. The following diagram illustrates the three-tier architecture of a JDBC application:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  JDBC API       |      |  JDBC Driver    |      |  Database       |
|                 |      |  Manager        |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Java           |      |  JDBC           |      |  JDBC Driver    |
|  Application    |----->|  Net Server     |----->|                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```