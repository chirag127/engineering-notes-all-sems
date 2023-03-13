#### Analyzing data with Hadoop

Hadoop is a framework for distributed processing of large-scale data sets using a cluster of computers. Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce.

HDFS is a distributed file system that stores data across multiple nodes in a cluster. HDFS provides high availability, fault tolerance, scalability and parallelism.

MapReduce is a programming model that allows users to write applications that process large amounts of data in parallel on a cluster. MapReduce consists of two phases: map and reduce. The map phase takes an input data set and transforms it into a set of key-value pairs. The reduce phase takes the output of the map phase and combines the values associated with the same key.

The following diagram illustrates the basic architecture of a Hadoop cluster:

```
+-----------------+    +-----------------+    +-----------------+
| NameNode        |    | DataNode        |    | DataNode        |
| (Master node)   |    | (Worker node)   |    | (Worker node)   |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | HDFS Master | |    | | HDFS Slave  | |    | | HDFS Slave  | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | JobTracker  | |    | | TaskTracker | |    | | TaskTracker | |
| | (MapReduce  | |    | | (MapReduce  | |    | | (MapReduce  | |
| | Master)     | |    | | Slave)      | |    | | Slave)      | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                              |
                              |
                              v
                      +-----------------+
                      | Client          |
                      |                 |
                      | +-------------+ |
                      | | HDFS Client | |
                      | +-------------+ |
                      |                 |
                      | +-------------+ |
                      | | MapReduce   | |
                      | | Client      | |
                      | +-------------+ |
                      +-----------------+
```