Hadoop is a framework for distributed processing of large-scale data sets using the MapReduce programming model. Hadoop consists of two main components: the Hadoop Distributed File System (HDFS) and the MapReduce engine. HDFS is a distributed file system that stores data across multiple nodes in a cluster, providing high availability, fault tolerance, and scalability. MapReduce is a programming model that allows parallel processing of large data sets by dividing them into smaller chunks and assigning them to different nodes for processing.

Hadoop also includes several additional modules that provide additional functionality, such as Hive, Pig, and HBase. Hive is a data warehouse infrastructure that provides data summarization and ad-hoc querying using a SQL-like query language called HiveQL. Pig is a high-level data-flow language and execution framework for parallel computation. Pig allows users to write complex data transformations using a simple scripting language called Pig Latin. HBase is a non-relational, distributed database that supports structured data storage for large tables. HBase provides fast random access and updates to data, as well as integration with MapReduce.

The following diagram illustrates the basic architecture of a Hadoop ecosystem, including the components mentioned above:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Client      |    |     Client      |    |     Client      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         +--------------------+--------------------+
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Master      |    |     Master      |    |     Master      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  NameNode       |    |  JobTracker     |    |  HMaster        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         |                    |                    |
         +--------------------+--------------------+
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Slave       |    |     Slave       |    |     Slave       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  DataNode       |    |  TaskTracker    |    |  HRegionServer  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  DataNode       |    |  TaskTracker    |    |  HRegionServer  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |