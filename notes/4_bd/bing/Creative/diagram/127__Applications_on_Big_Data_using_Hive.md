Applications on Big Data using Hive are mainly related to data analytics, reporting, dashboarding, auditing, and machine learning. Hive allows users to perform SQL-like queries on large datasets stored in Hadoop or other compatible systems, using batch processing with Apache Tez or MapReduce. Hive also provides a metastore that stores the metadata of the tables and partitions, and enables data abstraction and discovery. Hive can integrate with other tools like Apache Pig and MapReduce through HCatalog, which is a table and storage management layer that reads data from the Hive metastore.

The following diagram illustrates the basic architecture of a Hive application on Big Data using ASCII art:

```
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  User Interface  |      |  HiveQL Compiler |      |  Execution Engine|
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       V                        V                        V
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  HiveQL Processor|      |  Optimizer       |      |  MapReduce or Tez|
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       V                        V                        V
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  Metastore       |      |  Driver          |      |  HDFS or S3      |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
```