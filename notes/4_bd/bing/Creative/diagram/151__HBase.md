### HBase

HBase is a distributed, scalable, column-oriented database that runs on top of Hadoop Distributed File System (HDFS). It is modeled after Google's Bigtable and provides random, real-time read/write access to large datasets.

The following ASCII diagram illustrates the basic architecture of HBase:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Client       |    |    Client       |    |    Client       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
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
                           |
                           |
                           |
                           |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Master       |    |    ZooKeeper    |    |    HDFS         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
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
|    RegionServer |    |    RegionServer |    |    RegionServer |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Region       |    |    Region       |    |    Region       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

Some key components of HBase architecture are:

- Client: The client is the interface that allows users to interact with HBase. It provides APIs for creating, updating, deleting, and querying tables. The client communicates with the master and the region servers to perform operations on the data.
- Master: The master is the central coordinator that manages the cluster metadata, such as the assignment of regions to region servers, the load balancing of regions, the splitting of regions, and the handling of failures. The master also communicates with ZooKeeper and HDFS to maintain the consistency and availability of the data.
- ZooKeeper: ZooKeeper is a distributed coordination service that provides reliable and consistent service discovery, configuration management, and leader election for HBase. ZooKeeper maintains the information about the current master, the region servers, and the regions. ZooKeeper also handles the failover of the master and the region servers in case of failures.
- HDFS: HDFS is the underlying distributed file system that stores the data of HBase. HBase uses HDFS to store the data files, the write-ahead logs, and the snapshots. HDFS provides fault tolerance, replication, and scalability for HBase