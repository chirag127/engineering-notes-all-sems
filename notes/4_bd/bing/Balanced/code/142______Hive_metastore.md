#### Hive metastore

- The Hive metastore is a central repository of metadata for Hive tables and partitions.
- The Hive metastore stores information such as the schema, location, format, partitioning, and statistics of the Hive tables and partitions.
- The Hive metastore also stores the configuration parameters and security policies for accessing the Hive tables and partitions.
- The Hive metastore can be configured to use different back-end databases, such as Derby, MySQL, PostgreSQL, Oracle, or SQL Server.
- The Hive metastore can be deployed in two modes: embedded or remote.
  - In embedded mode, the Hive metastore runs in the same JVM as the Hive server and uses a local database.
  - In remote mode, the Hive metastore runs as a separate service and uses a remote database.
- The Hive metastore provides a thrift interface for clients to interact with the metadata.
- The Hive metastore can be accessed by different components of the Hive ecosystem, such as Hive CLI, HiveServer2, Hive Web Interface, and other applications that use the Hive JDBC or ODBC drivers.
- The Hive metastore can also be integrated with other frameworks that use the Hive storage handler, such as Spark SQL, Presto, and Impala.