## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

The following diagram illustrates the basic architecture of a Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala:

```
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|     MongoDB      |    |    Cassandra     |    |    Cloudant      |    |    Other NoSQL   |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|    NoSQL Data    |    |    NoSQL Data    |    |    NoSQL Data    |    |    NoSQL Data    |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|     Hadoop       |    |     Hadoop       |    |     Hadoop       |    |     Hadoop       |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|     HDFS         |    |     HDFS         |    |     HDFS         |    |     HDFS         |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|     YARN         |    |     YARN         |    |     YARN         |    |     YARN         |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|     Spark        |    |     Spark        |    |     Spark        |    |     Spark        |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |    |                  |
|     Scala        |    |     Scala        |    |     Scala        |    |     Scala        |
|                  |    |                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+    +------------------+
```

The diagram shows how different NoSQL databases, such as MongoDB, Cassandra, Cloudant, and others, can store and process data using Hadoop, HDFS, YARN, Spark, and Scala. Hadoop is a framework for distributed processing of large data sets across clusters of computers. HDFS is the distributed file system that stores data on the Hadoop cluster. YARN is the resource manager that allocates and manages resources for the Hadoop applications. Spark is an analytics engine that can perform batch, streaming, SQL, and machine learning tasks on the Hadoop data. Scala is a programming language that can be used to write Spark applications.