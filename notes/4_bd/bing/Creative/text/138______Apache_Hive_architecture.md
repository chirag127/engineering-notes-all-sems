#### Apache Hive architecture

Apache Hive is a data warehouse system that enables analytics at a massive scale on top of Hadoop. It provides a SQL-like query language called HiveQL that can process structured and semi-structured data. Hive also supports user-defined functions and custom data formats.

The main components of Apache Hive architecture are:

- **Hive Clients**: These are the interfaces that allow users and applications to interact with Hive. They include the Hive Shell, the Hive Web Interface, the Hive JDBC and ODBC drivers, and the Hive Thrift API.
- **Hive Services**: These are the components that provide the core functionality of Hive, such as parsing, compiling, optimizing, and executing queries. They include the Hive Server 2, the Hive Metastore, and the Hive Compiler.
- **Processing Framework and Resource Management**: These are the components that handle the distributed processing and resource allocation of Hive queries. They include the MapReduce or Tez execution engine, and the YARN or Mesos resource manager.
- **Distributed Storage**: This is the component that stores the data and metadata of Hive tables and partitions. It includes the Hadoop Distributed File System (HDFS) or other compatible file systems.

The following diagram illustrates the Apache Hive architecture:

```
+-----------------+     +-----------------+
| Hive Clients    |     | Distributed     |
| - Hive Shell    |     | Storage         |
| - Hive Web UI   |     | - HDFS          |
| - Hive JDBC/ODBC|     | - S3            |
| - Hive Thrift   |     | - Azure Blob    |
+-----------------+     | - ...           |
        |               +-----------------+
        |                       ^
        v                       |
+-----------------+     +-----------------+
| Hive Services   |     | Processing      |
| - Hive Server 2 |     | Framework and   |
| - Hive Metastore|     | Resource        |
| - Hive Compiler |     | Management      |
+-----------------+     | - MapReduce/Tez |
        |               | - YARN/Mesos    |
        v               +-----------------+
+-----------------+             ^
| HiveQL          |             |
+-----------------+             |
        |                       |
        +-----------------------+
```