Hive services are the components that enable users to interact with Hive and perform various operations on data stored in Hadoop. The following ASCII diagram illustrates the basic architecture of Hive services:

```
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|   Hive Clients   |      |  Hive Services  |      |  Hive Storage   |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|  - Beeline       |      |  - HiveServer2  |      |  - HDFS         |
|  - JDBC/ODBC     |      |  - Hive CLI     |      |  - Amazon S3    |
|  - Web UI        |      |  - Hive WebHCat |      |  - Azure Blob   |
|  - Hive Thrift   |      |  - Hive Metastore|     |  - Other FS     |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
|                  |      |                 |      |                 |
+------------------+      +-----------------+      +-----------------+

```

Some of the main Hive services are:

- HiveServer2: A service that allows clients to execute queries against Hive using different interfaces such as JDBC, ODBC, and Thrift.
- Hive CLI: A command-line interface that allows users to interact with Hive directly.
- Hive WebHCat: A RESTful API that allows users to access and reuse Hive metadata and run Hive jobs.
- Hive Metastore: A service that stores the metadata of tables, partitions, columns, and schemas in a relational database. It also provides a catalog service for HCatalog, which enables data sharing between Hive, Pig, and MapReduce.