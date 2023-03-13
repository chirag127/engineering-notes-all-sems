#### Hive metastore

- Hive metastore is a service that stores metadata related to Apache Hive and other services, such as Impala, Spark, etc. in a backend relational database, such as MySQL .
- Metadata includes information about the tables, columns, partitions, schemas, databases, views, functions, etc. that are available in the data lake.
- Hive metastore provides a central repository of metadata that can easily be analyzed to make informed, data driven decisions, and therefore it is a critical component of many data lake architectures.
- Hive metastore supports storage on various file systems, such as S3, ADLS, GS, etc. through HDFS.
- Hive metastore can be configured in three modes: embedded, local, and remote.
  - Embedded mode: The metastore service and the Hive server run in the same JVM and use the same database connection. This is the default mode and is suitable for testing and development purposes.
  - Local mode: The metastore service runs in a separate JVM from the Hive server, but they use the same database connection. This mode allows multiple Hive servers to share the same metastore service.
  - Remote mode: The metastore service runs in a separate JVM and a separate host from the Hive server, and they use different database connections. This mode allows multiple Hive servers and other services to share the same metastore service across the network.
- Hive metastore can be accessed through various interfaces, such as Thrift, JDBC, ODBC, etc.
- Hive metastore can be integrated with other components, such as Ranger, Sentry, Atlas, etc. for security, governance, and lineage purposes.

A possible ascii diagram of Hive metastore in remote mode is:

```
+-----------------+        +-----------------+        +-----------------+
| Hive Server     |        | Metastore       |        | Database        |
|                 |        | Service         |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | Hive CLI    | |        | | Thrift      | |        | | MySQL       | |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | Hive JDBC   | |        | | JDBC        | |        | | PostgreSQL  | |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | Hive ODBC   | |        | | ODBC        | |        | | Oracle      | |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |-------------------------|-------------------------|
      |                         |                         |
      |                         |                         |
      |                         |                         |
+-----------------+        +-----------------+        +-----------------+
| Impala Server   |        | Spark Server    |        | HDFS            |
|                 |        |                 |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | Impala CLI  | |        | | Spark Shell | |        | | S3          | |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | Impala JDBC | |        | | Spark JDBC  | |        | | ADLS        | |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | Impala ODBC | |        | | Spark ODBC  | |        | | GS          | |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +