Hadoop Eco System Frameworks are a set of tools, libraries, and frameworks that help you build applications on top of Apache Hadoop. Hadoop is a framework that enables processing of large data sets which reside in the form of clusters. The core component of the Hadoop ecosystem is a Hadoop distributed file system (HDFS). HDFS is a distributed file system that has the capability to store a large stack of data sets. There are four major elements of Hadoop i.e. HDFS, MapReduce, YARN, and Hadoop Common    .

The following is a detailed ASCII diagram for Hadoop Eco System Frameworks:

```
+-----------------------------------------------------------------+
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                          Hadoop Ecosystem                       |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
+-----------------------------------------------------------------+
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|+-----------------+ +-----------------+ +-----------------+ +-----------------+|
||                 | |                 | |                 | |                 ||
||    Hadoop       | |    Hadoop       | |    Hadoop       | |    Hadoop       ||
||    Common       | |    HDFS         | |    MapReduce    | |    YARN         ||
||                 | |                 | |                 | |                 ||
|+-----------------+ +-----------------+ +-----------------+ +-----------------+|
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|+-----------------+ +-----------------+ +-----------------+ +-----------------+|
||                 | |                 | |                 | |                 ||
||    Pig          | |    Hive         | |    HBase        | |    Spark        ||
||                 | |                 | |                 | |                 ||
|+-----------------+ +-----------------+ +-----------------+ +-----------------+|
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|+-----------------+ +-----------------+ +-----------------+ +-----------------+|
||                 | |                 | |                 | |                 ||
||    Sqoop        | |    Flume        | |    Oozie        | |    Zookeeper    ||
||                 | |                 | |                 | |                 ||
|+-----------------+ +-----------------+ +-----------------+ +-----------------+|
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|+-----------------+ +-----------------+ +-----------------+ +-----------------+|
||                 | |                 | |                 | |                 ||
||    Mahout       | |    Storm        | |    Kafka        | |    Cassandra    ||
||                 | |                 | |                 | |                 ||
|+-----------------+ +-----------------+ +-----------------+ +-----------------+|
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
|                                                                 |
+-----------------------------------------------------------------+
```

The diagram shows the four core components of Hadoop and some of the most popular tools and frameworks that are built on top of them or work with them. Each of these components and tools has a specific function and role in the Hadoop ecosystem. For example:

- Hadoop Common: It provides the common utilities and libraries that are used by other Hadoop modules.
- Hadoop HDFS: It is the distributed file system that stores the data in a fault-tolerant and scalable manner across the cluster nodes.
- Hadoop MapReduce: It is the programming model that allows for parallel processing of large data sets using key-value pairs.
- Hadoop YARN: It is the resource management layer that allocates and manages the compute resources for the applications running