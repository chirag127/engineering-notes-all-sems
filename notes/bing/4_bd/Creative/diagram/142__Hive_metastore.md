Hive metastore is a central repository of metadata that can easily be analyzed to make informed, data driven decisions, and therefore it is a critical component of many data lake architectures. It stores information about the tables, partitions, columns, data types, locations, and other properties of the data stored in Hive. It also supports storage on various file systems such as S3, ADLS, GS, etc. through HDFS. Hive metastore can be configured to use different backends such as Derby, MySQL, PostgreSQL, etc. to store the metadata.

#### Hive metastore

The following diagram illustrates the basic architecture of a Hive metastore:

```
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|   Hive Client    |      |   Hive Server    |      |   Metastore DB   |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  - Hive CLI      |      |  - Thrift Server |      |  - Derby         |
|  - Hive JDBC     |      |  - Hive Service  |      |  - MySQL         |
|  - Hive ODBC     |      |  - Metastore     |      |  - PostgreSQL    |
|  - Hive Web UI   |      |    Service       |      |  - etc.          |
|  - etc.          |      |                  |      |                  |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
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
       +---------------------->|                       |
       |                       |                       |
       |                       +---------------------->|
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
       |                       <----------------------+
       |                       |                       |
       <----------------------+                       |
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
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|   HDFS Client    |      |   HDFS Server    |      |   HDFS Storage   |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  - HDFS CLI      |      |  - NameNode      |      |  - S3            |
|  - HDFS API      |      |  - DataNode      |      |  - ADLS          |
|  - etc.          |      |  - etc.          |      |  - GS            |
|                  |      |                  |      |  - etc.          |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
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
       +---------------------->|                       |
       |                       |                       |