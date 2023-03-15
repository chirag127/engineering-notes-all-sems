#### Hive services

Hive services are the components that enable users to interact with Hive and perform various operations on data stored in Hive tables. Hive services include:

- **HiveServer2**: This is the main service that provides a JDBC/ODBC interface for clients to execute queries and access the metadata. HiveServer2 supports multiple concurrent users and sessions, and provides security features such as authentication and authorization.
- **Hive Metastore**: This is the service that stores the metadata of Hive tables, partitions, columns, and other objects. The metadata is stored in a relational database such as MySQL or PostgreSQL, and can be accessed by HiveServer2 and other Hive components. The Hive Metastore also provides a thrift interface for external tools and applications to interact with the metadata.
- **Hive Web Interface (HWI)**: This is a web-based graphical user interface that allows users to browse the Hive metadata, submit queries, and view the results. HWI is deprecated and replaced by Hive View in Ambari.
- **Hive CLI**: This is a command-line interface that allows users to execute Hive commands and queries. Hive CLI is mainly used for debugging and testing purposes, and is not recommended for production use. Hive CLI does not support concurrent users or sessions, and does not provide any security features.