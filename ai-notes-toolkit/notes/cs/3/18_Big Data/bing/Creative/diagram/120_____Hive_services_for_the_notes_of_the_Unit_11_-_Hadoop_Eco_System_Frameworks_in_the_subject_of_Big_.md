### Hive Services

Hive services are the components that perform client interactions with Hive. They allow users to submit queries and commands to Hive and receive the results. Some of the main Hive services are:

- **HiveServer2**: This is the main service that provides a JDBC/ODBC interface for clients to connect to Hive and execute queries. It also supports authentication, authorization, and encryption. HiveServer2 can run in different modes, such as embedded, local, or remote .
- **Beeline**: This is a command-line shell that connects to HiveServer2 and allows users to submit queries and commands to Hive. It is based on the SQLLine tool and supports multiple sessions and output formats.
- **Hive Web Interface**: This is a web-based graphical user interface that allows users to browse the Hive metadata, execute queries, and view the query history and logs.
- **Hive Thrift Server**: This is a legacy service that provides a Thrift interface for clients to connect to Hive and execute queries. It is deprecated and replaced by HiveServer2.
- **Hive Metastore**: This is a service that stores the metadata of the tables, partitions, columns, and schemas in Hive. It can use different back-end databases, such as MySQL, PostgreSQL, or Oracle. The Hive Metastore can run in embedded mode (within the same JVM as HiveServer2) or remote mode (as a separate process) .
- **Hive CLI**: This is a legacy command-line shell that allows users to submit queries and commands to Hive. It is deprecated and replaced by Beeline.