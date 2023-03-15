#### Hive metastore

- Hive metastore is a central repository that stores metadata for Hive tables and partitions.
- Hive metastore provides a service that allows other applications to access the Hive metadata using a thrift API.
- Hive metastore can be configured to use different backends for storing the metadata, such as Derby, MySQL, PostgreSQL, Oracle, etc.
- Hive metastore consists of two components: a metastore server and a metastore database.
- The metastore server is a Java process that runs on a separate machine from the Hive server and communicates with the metastore database using JDBC.
- The metastore database is a relational database that stores the metadata in a set of tables defined by the Hive schema.
- The metastore server exposes a thrift interface that can be accessed by Hive clients, such as Hive CLI, HiveServer2, Hive Web Interface, etc.
- The metastore server also interacts with the Hadoop file system (HDFS) to perform operations such as creating, deleting, or renaming directories and files for Hive tables and partitions.
- The metastore server caches some of the metadata in memory to improve performance and reduce database load.
- The metastore server can be configured to use authentication, authorization, encryption, and auditing mechanisms to secure the access to the metadata.