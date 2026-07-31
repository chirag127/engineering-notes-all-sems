### Hive Services

Hive services are the components that perform client interactions with Hive. They allow users to submit queries and commands to Hive and receive the results. Some of the main Hive services are:

- **HiveServer2**: This is the main service that provides a JDBC/ODBC interface for clients to connect to Hive and execute queries. It also supports authentication, authorization, and encryption. HiveServer2 can run in different modes, such as embedded, local, or remote .
- **Beeline**: This is a command-line shell that connects to HiveServer2 and allows users to submit queries and commands to Hive. It is based on the SQLLine tool and supports multiple sessions and output formats.
- **Hive Web Interface (HWI)**: This is a web-based graphical user interface that allows users to browse the Hive metadata, execute queries, and view the results. It is deprecated in Hive 0.14.0 and replaced by HiveServer2 web UI.
- **Hive Thrift Server**: This is an older service that provides a thrift interface for clients to connect to Hive and execute queries. It is deprecated in Hive 0.13.0 and replaced by HiveServer2.
- **Hive CLI**: This is a command-line interface that allows users to interact with Hive directly without connecting to any server. It is deprecated in Hive 2.0.0 and replaced by Beeline.

Hive services communicate with the Hive storage and computing components, such as the file system, the job client, and the metastore. The file system stores the data and the query results in HDFS or other compatible storage systems. The job client submits the queries to the execution engine, such as MapReduce, Tez, or Spark, and monitors the progress. The metastore stores the metadata of the tables, partitions, columns, and other schema information in a relational database, such as MySQL, PostgreSQL, or Oracle .