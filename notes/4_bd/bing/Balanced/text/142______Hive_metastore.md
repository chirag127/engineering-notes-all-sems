#### Hive metastore

- Hive metastore is a central repository that stores metadata for Hive tables and partitions.
- Hive metastore provides a service that allows other applications to access the Hive metadata using a Thrift API or a JDBC connection.
- Hive metastore can be configured to use different back-end databases, such as Derby, MySQL, PostgreSQL, Oracle, etc.
- Hive metastore consists of two components: a metastore server and a metastore database.
- The metastore server is a Java process that runs on a separate machine from the Hive server and communicates with the metastore database using JDBC.
- The metastore database is a relational database that stores the schema and location of Hive tables and partitions, as well as other information such as statistics, privileges, etc.
- Hive metastore supports two modes of operation: embedded and remote.
- In embedded mode, the metastore server and the metastore database run on the same machine as the Hive server, and the metastore database uses Derby as the back-end.
- In remote mode, the metastore server and the metastore database run on different machines from the Hive server, and the metastore database can use any supported back-end.
- Remote mode is recommended for production environments, as it provides better scalability, reliability, and security than embedded mode.