#### Hive services

Hive services are the components that perform client interactions with Hive. They allow users to submit queries and commands to Hive and receive the results. Some of the main Hive services are:

- **HiveServer2**: This is the main service that provides a JDBC/ODBC interface for clients to connect to Hive and execute queries. It also supports authentication, authorization, and encryption. HiveServer2 can run in different modes, such as embedded, local, or remote.
- **Beeline**: This is a command-line shell that connects to HiveServer2 and allows users to submit queries and commands to Hive. It is based on the SQLLine tool and supports multiple sessions and output formats.
- **Hive Web Interface (HWI)**: This is a web-based graphical user interface that allows users to browse the Hive metadata, execute queries, and view the results. It is deprecated in Hive 0.14.0 and replaced by HiveServer2 web UI.
- **Hive Thrift Server**: This is an older service that provides a Thrift interface for clients to connect to Hive and execute queries. It is deprecated in Hive 0.13.0 and replaced by HiveServer2.
- **Hive CLI**: This is a command-line interface that allows users to interact with Hive directly without using HiveServer2. It is mainly used for debugging and testing purposes. It is deprecated in Hive 2.0.0 and replaced by Beeline.
- **Hive Metastore**: This is a service that stores the metadata of the tables, partitions, columns, and schemas in Hive. It can use different back-end databases, such as Derby, MySQL, PostgreSQL, or Oracle. It also provides a Thrift API for other Hive services and clients to access the metadata.