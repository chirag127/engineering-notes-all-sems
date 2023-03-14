Hive shell is a command-line interface that allows users to interact with Hive and execute HiveQL queries. It can run in either interactive or batch mode. Hive shell communicates with HiveServer2, which is a service that provides access to the Hive metastore and the execution engine. HiveServer2 supports multiple clients and concurrency, and can run queries using MapReduce, Tez, or Spark as the execution engine. Hive metastore is a relational database that stores the metadata of Hive tables, partitions, schemas, and functions. Hive shell can also connect to other data sources, such as HDFS, S3, or HBase, using different storage formats, such as Parquet, ORC, or plain text.

The following diagram illustrates the basic architecture of Hive shell:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Hive shell    |<----->|  HiveServer2    |<----->|  Hive metastore |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       v       v                       |
       |                 +-----------------+                  |
       |                 |                 |                  |
       |                 | Execution engine|                  |
       |                 |                 |                  |
       |                 +-----------------+                  |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       v       v                       |
       |                 +-----------------+                  |
       |                 |                 |                  |
       |                 |   Data sources  |                  |
       |                 |                 |                  |
       |                 +-----------------+                  |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       |       |                       |
       |                       v       v                       |
       |                 +-----------------+                  |
       |                 |                 |                  |
       |                 |   Data formats  |                  |
       |                 |                 |                  |
       |                 +-----------------+                  |
       |                                                       |
       +-------------------------------------------------------+
```