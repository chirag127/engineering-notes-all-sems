#### Hive services

Hive services are the components that perform client interactions with Hive. They allow users to submit queries and commands to Hive and receive the results. Some of the main Hive services are:

- **HiveServer2**: This is the main service that provides a JDBC/ODBC interface for clients to connect to Hive and execute queries. It also supports authentication, authorization, and encryption. HiveServer2 can run in different modes, such as embedded, local, or remote .
- **Beeline**: This is a command-line shell that connects to HiveServer2 and allows users to submit queries and commands to Hive. It is based on the SQLLine tool and supports multiple sessions and output formats.
- **Metastore**: This is a service that stores the metadata of the tables, partitions, columns, and schemas in Hive. It also provides APIs for other services and applications to access and manipulate the metadata. The metastore can use different back-end databases, such as MySQL, PostgreSQL, or Oracle .
- **WebHCat**: This is a REST API service that provides a web interface for users to run Hive queries and other Hadoop jobs. It also allows users to create and manage Hive tables and partitions. WebHCat uses the Templeton server to communicate with the Hadoop cluster and the metastore.
- **Hive CLI**: This is a deprecated service that provides a command-line interface for users to interact with Hive. It is not recommended to use this service as it has several limitations and issues. Users should use Beeline or HiveServer2 instead.