### Hive services

Hive services are the components that perform client interactions with Hive. They allow users to submit queries and commands to Hive and receive the results. Some of the main Hive services are:

- **HiveServer2**: This is the main service that provides a JDBC/ODBC interface for clients to connect to Hive and execute queries. It also supports multiple concurrent users and sessions, security features, and a web UI for monitoring and debugging .
- **Beeline**: This is a command-line shell that connects to HiveServer2 and allows users to submit queries and commands to Hive. It is based on the SQLLine tool and supports multiple output formats, scripting, and variables.
- **Hive Web Interface (HWI)**: This is a web-based graphical user interface that allows users to browse the Hive metadata, create and drop tables, and run queries. It is deprecated in Hive 0.14.0 and replaced by HiveServer2 web UI.
- **Hive Metastore**: This is a service that stores the metadata of the tables, partitions, columns, and schemas in Hive. It can use different back-end databases such as MySQL, PostgreSQL, Oracle, etc. It also provides a Thrift API for other components to access the metadata .
- **Hive CLI**: This is a legacy command-line interface that allows users to interact with Hive directly. It is deprecated in Hive 2.0.0 and replaced by Beeline.