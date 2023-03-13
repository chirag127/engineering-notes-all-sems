## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

The following is a detailed ascii diagram for Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala:

```
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|     Hadoop       |    |     Spark       |    |     Scala       |    |     MongoDB      |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|  HDFS            |    |  Spark Core     |    |  Scala Compiler |    |  BSON            |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|  MapReduce       |    |  Spark SQL      |    |  Scala Library  |    |  Indexing        |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|  YARN            |    |  Spark Streaming|    |  Scala REPL     |    |  Aggregation     |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|  Hive            |    |  Spark MLlib    |    |  Scala IDE      |    |  Replication     |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|  Pig             |    |  Spark GraphX   |    |  Scala Test     |    |  Sharding        |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|  Oozie           |    |                  |    |                  |    |  CRUD Operations |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|  Zookeeper       |    |                  |    |                  |    |  Capped          |
|                  |    |                  |    |                  |    |  Collections     |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|  Mahout          |    |                  |    |                  |    |                  |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
```

The diagram illustrates the basic architecture of a Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala. The Hadoop Eco System consists of HDFS, MapReduce, YARN, Hive, Pig, Oozie, Zookeeper and Mahout. HDFS is the distributed file system that stores the data. MapReduce is the programming model that processes the data in parallel. YARN is the resource manager that allocates the resources for the applications. Hive is the data warehouse that provides SQL-like queries. Pig is the scripting language that simplifies the data analysis. Oozie is the workflow scheduler that coordinates the jobs. Zookeeper is the service that maintains the configuration and coordination of the cluster. Mahout is the machine learning library that provides scalable algorithms.

Spark is a fast and general engine for large-scale data processing. It consists of Spark Core, Spark SQL, Spark Streaming, Spark MLlib and Spark GraphX. Spark Core is the foundation that provides the distributed memory abstraction and the basic operations. Spark SQL is the module that supports structured and semi-structured data processing. Spark Streaming is the module that enables real-time data processing. Spark MLlib is the module that provides