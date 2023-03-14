Hive metastore is a central repository of metadata for Hive tables and partitions in a relational database, and provides clients (including Hive, Impala and Spark) access to this information using the metastore service API. It is a critical component of many data lake architectures, as it allows users to query data in various formats and locations using SQL.

#### Hive metastore

The following is a simplified ASCII diagram of the Hive metastore architecture:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Hive Client   |<---->|  Thrift Server  |<---->|  Metastore DB   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
      ^  ^  ^                   ^  ^  ^                   ^  ^  ^
      |  |  |                   |  |  |                   |  |  |
      |  |  +-------------------+  |  +-------------------+  |  |
      |  |                         |                         |  |
      |  +-------------------------+-------------------------+  |
      |                                                          |
      +----------------------------------------------------------+
```

The Hive client is any application that interacts with Hive metastore, such as Hive, Spark, Impala, or Pig. The client communicates with the Thrift server, which is a service that exposes the metastore API using the Thrift protocol. The Thrift server connects to the metastore database, which is usually MySQL, Postgres, or Derby, and stores the metadata for tables, partitions, columns, data types, locations, etc. The metadata is projected to SQL, so it can be easily queried using HSQL. The Thrift server also handles authentication and authorization for the clients.