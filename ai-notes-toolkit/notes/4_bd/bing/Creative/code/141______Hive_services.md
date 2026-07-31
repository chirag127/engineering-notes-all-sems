#### Hive services

Hive services are the components that perform client interactions with Hive. They allow users to submit queries and commands to Hive and receive the results. Some of the main Hive services are:

- **HiveServer2**: This is the main service that provides a JDBC/ODBC interface for clients to connect to Hive and execute queries. It also supports authentication, authorization, and encryption. HiveServer2 can run in different modes, such as embedded, local, or remote .
- **Beeline**: This is a command-line shell that connects to HiveServer2 and allows users to submit queries and commands interactively. Beeline supports multiple sessions and can run scripts from files.
- **Hive Web Interface (HWI)**: This is a web-based graphical user interface that allows users to browse the Hive metadata, execute queries, and view the results. HWI is deprecated and replaced by Hue, a more advanced web interface for Hadoop.
- **Hive Thrift Server**: This is an older service that provides a Thrift interface for clients to connect to Hive and execute queries. It is less secure and scalable than HiveServer2 and is not recommended for production use.
- **Hive Metastore**: This is a service that stores the metadata of the tables, partitions, columns, and schemas in Hive. It also provides a Thrift interface for other Hive services and clients to access the metadata. The Hive Metastore can use different back-end databases, such as Derby, MySQL, PostgreSQL, or Oracle .
- **Hive CLI**: This is a command-line shell that allows users to submit queries and commands directly to Hive without connecting to HiveServer2. It is mainly used for debugging and testing purposes and is not recommended for production use.

: https://www.guru99.com/introduction-hive.html
: https://www.interviewbit.com/blog/hive-architecture/
: https://www.simplilearn.com/what-is-hive-article