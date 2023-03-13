Manipulating in JDBC means using the JDBC API to create, insert into, update, and query tables in a database. JDBC is a Java-based interface that allows Java applications to connect to and interact with various types of databases. JDBC drivers are the software components that implement the JDBC API for different database vendors.

#### Manipulating in JDBC

The following diagram illustrates the basic architecture of manipulating in JDBC using ASCII characters:

```
+----------------+     +----------------+     +----------------+
| Java Program   |     | JDBC Driver   |     | Database       |
|                |     |               |     |                |
| +------------+ |     | +------------+ |     | +------------+ |
| | JDBC API   | |     | | JDBC API   | |     | | SQL Engine | |
| +------------+ |     | +------------+ |     | +------------+ |
| | Connection | |---->| | Connection | |---->| | Connection | |
| +------------+ |     | +------------+ |     | +------------+ |
| | Statement  | |---->| | Statement  | |---->| | Statement  | |
| +------------+ |     | +------------+ |     | +------------+ |
| | ResultSet  | |<----| | ResultSet  | |<----| | ResultSet  | |
| +------------+ |     | +------------+ |     | +------------+ |
+----------------+     +----------------+     +----------------+
```

The diagram shows the following steps:

- The Java program uses the JDBC API to create a Connection object that represents a connection to the database.
- The Java program uses the Connection object to create a Statement object that represents a SQL statement to be executed on the database.
- The Java program uses the Statement object to execute the SQL statement and obtain a ResultSet object that represents the result of the query.
- The Java program uses the ResultSet object to access and manipulate the data returned by the query.