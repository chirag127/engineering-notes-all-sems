Hadoop Eco System and YARN are two related concepts in the field of big data processing. Hadoop Eco System refers to the various components of the Apache Hadoop software library, which includes open source projects as well as a complete range of complementary tools. Some of the most well-known tools of the Hadoop ecosystem include HDFS, Hive, Pig, YARN, MapReduce, Spark, HBase, Oozie, Sqoop, Zookeeper, etc.

YARN stands for Yet Another Resource Negotiator, and it is one of the core components in open source Apache Hadoop suitable for resource management. It is responsible for managing workloads, monitoring, and security controls implementation. It also allocates system resources to the various applications running in a Hadoop cluster while assigning which tasks should be executed by each cluster nodes. YARN has two main components: Resource Manager and Node Manager

The following diagram illustrates the basic architecture of a Hadoop Eco System and YARN:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     HDFS        |    |     Hive        |    |     Pig         |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     HBase       |    |     Spark       |    |     Oozie       |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     Sqoop       |    |     Zookeeper   |    |     Flume       |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     MapReduce   |    |     YARN        |    |     Tez         |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     Hadoop      |    |     Hadoop      |    |     Hadoop      |
|     Common      |    |     Common      |    |     Common      |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     Linux       |    |     Linux       |    |     Linux       |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     Node 1      |    |     Node 2      |    |     Node 3      |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     Cluster     |    |     Cluster     |    |     Cluster     |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     Resource    |    |     Node        |    |     Node        |
|     Manager     |    |     Manager     |    |     Manager     |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|     YARN        |    |     YARN        |    |     YARN        |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
```