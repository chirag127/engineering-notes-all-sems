#### Hive services

Hive services are the components that enable users to interact with Hive and perform various operations on data stored in Hive tables. Some of the main Hive services are:

- **HiveServer2**: This is the main service that provides a JDBC/ODBC interface for clients to connect to Hive and execute queries. HiveServer2 also supports authentication, authorization, and encryption for secure communication. HiveServer2 can run in embedded mode or remote mode. In embedded mode, HiveServer2 and the metastore run in the same JVM, which is suitable for testing and debugging. In remote mode, HiveServer2 and the metastore run in separate JVMs, which is suitable for production and scalability  .

- **Beeline**: This is a command-line shell that allows users to submit commands and queries to HiveServer2. Beeline uses JDBC to connect to HiveServer2 and supports multiple simultaneous connections. Beeline can also run scripts and save query results to files.

- **Metastore**: This is a service that stores the metadata of Hive tables, such as table names, column names, data types, partition information, etc. The metastore can use different backends, such as Derby, MySQL, PostgreSQL, etc. The metastore can run in embedded mode or remote mode. In embedded mode, the metastore runs in the same JVM as HiveServer2 or Hive CLI, which is suitable for testing and debugging. In remote mode, the metastore runs in a separate JVM and can be accessed by multiple Hive clients, which is suitable for production and scalability  .

- **HCatalog**: This is a service that provides a table and storage management layer for Hive. HCatalog allows other data processing tools, such as Pig and MapReduce, to access Hive tables without knowing the details of the underlying storage format or location. HCatalog also provides a REST API, called WebHCat, for accessing the Hive metadata and executing Hive jobs .

- **Hive CLI**: This is a deprecated service that provides a command-line interface for users to interact with Hive. Hive CLI is not recommended for production use, as it does not support authentication, authorization, or encryption. Hive CLI also runs Hive queries in the same JVM as the CLI, which can cause memory issues. Users should use Beeline instead of Hive CLI.