Hive shell is a command-line interface that allows users to interact with Hive and run Hive queries. It can be used in interactive or batch mode. Hive shell communicates with HiveServer2, which is a service that provides access to Hive via JDBC or ODBC drivers. HiveServer2 executes the queries on the Hadoop cluster using MapReduce, Tez, or Spark as the execution engine. Hive stores the metadata of the tables, partitions, columns, etc. in a relational database called Hive Metastore. Hive also uses HDFS or other compatible file systems to store the actual data.

The following diagram illustrates the basic architecture of Hive shell using ASCII characters:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Hive shell     |       |  HiveServer2    |       |  Hive Metastore |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +---------------------->+                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               +---------------------->+                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       +---------------------->+-----------------+
                                                                               |                 |
                                                                               |  HDFS          |
                                                                               |                 |
                                                                               +-----------------+
```