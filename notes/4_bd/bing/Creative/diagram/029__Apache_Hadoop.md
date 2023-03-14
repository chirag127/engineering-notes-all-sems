Apache Hadoop is a software framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models . Hadoop follows the master-slave architecture for effectively storing and processing vast amounts of data. The master nodes assign tasks to the slave nodes.

The following is a detailed ASCII diagram for Apache Hadoop:

```
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    NameNode     |  | Secondary       |  |    Resource     |
|                 |  | NameNode        |  |    Manager      |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    HDFS         |  |    HDFS         |  |    YARN         |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    Master       |  |    Master       |  |    Master       |
|    Node         |  |    Node         |  |    Node         |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    Cluster      |  |    Cluster      |  |    Cluster      |
|    Metadata     |  |    Metadata     |  |    Metadata     |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    ZooKeeper    |  |    ZooKeeper    |  |    ZooKeeper    |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    HBase        |  |    HBase        |  |    HBase        |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    Hive         |  |    Hive         |  |    Hive         |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    Pig          |  |    Pig          |  |    Pig          |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    Spark        |  |    Spark        |  |    Spark        |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    MapReduce    |  |    MapReduce    |  |    MapReduce    |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    DataNode     |  |    DataNode     |  |    NodeManager  |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    HDFS         |  |    HDFS         |  |    YARN         |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    Slave        |  |    Slave        |  |    Slave        |
|    Node         |  |    Node         |  |    Node         |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|    Data         |  |    Data         |  |    Data         |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
```

The diagram shows the basic architecture of a Hadoop cluster, which consists of one or more master nodes and many slave nodes. The