#### How does HDFS store

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data processing.
- HDFS stores data in a distributed manner, by dividing the files into fixed-size blocks (default 128 MB) and storing them across multiple DataNodes in the cluster.
- DataNodes are the slave nodes that store the actual data blocks and serve read and write requests from the clients.
- NameNode is the master node that maintains the file system namespace and the metadata of all the files and blocks in the cluster. It also manages the replication and placement of blocks on DataNodes.
- HDFS follows a write-once-read-many model, which means that once a file is written, it cannot be modified. However, it can be appended or deleted.
- HDFS provides high availability and reliability by replicating each block on multiple DataNodes (default 3). This ensures that the data is not lost even if some DataNodes fail or become inaccessible.
- HDFS also supports rack awareness, which means that it tries to place the replicas of a block on different racks in the cluster. This improves the network bandwidth utilization and the fault tolerance of the system.
- HDFS allows the clients to access the data through a standard interface (such as Java API, WebHDFS, or command-line tools). It also supports integration with other frameworks such as MapReduce, Spark, and Hive for data processing and analysis.

Here is a simple diagram to illustrate the HDFS architecture:

```
    +-----------------+
    |    Client       |
    +-----------------+
          |
          |  (1) Request file /foo/bar.txt
          |
          v
    +-----------------+
    |    NameNode     |<-----------------+
    +-----------------+                  |
          |                              |
          |  (2) Return block locations  |
          |                              |
          v                              |
    +-----------------+                  |
    |    DataNode 1   |<-------------+   |
    +-----------------+              |   |
          |                          |   |
          |  (3) Read block B1       |   |
          v                          |   |
    +-----------------+              |   |
    |    DataNode 2   |<----------+  |   |
    +-----------------+           |  |   |
          |                       |  |   |
          |  (4) Read block B2    |  |   |
          v                       |  |   |
    +-----------------+           |  |   |
    |    DataNode 3   |<-------+  |  |   |
    +-----------------+        |  |  |   |
          |                    |  |  |   |
          |  (5) Read block B3 |  |  |   |
          v                    |  |  |   |
    +-----------------+        |  |  |   |
    |    DataNode 4   |        |  |  |   |
    +-----------------+        |  |  |   |
                               |  |  |   |
                               |  |  |   |
                               |  |  |   |
                               |  |  |   |
                               |  |  |   |
                               v  v  v   v
    +-----------------+        +-----------------+
    |    Client       |<-------|    Data Blocks  |
    +-----------------+        +-----------------+
                               | B1 | B2 | B3 | B4|
                               +-----------------+
```

- The client requests the NameNode for the file /foo/bar.txt
- The NameNode returns the locations of the blocks that make up the file, such as B1, B2, B3, and B4
- The client contacts the DataNodes that store the blocks and reads them in parallel
- The client combines the blocks and gets the file content

Some mnemonics and learning tricks for how does HDFS store are:

- HDFS = Hadoop Distributed File System = Huge Data Files Splitted
- NameNode = Name and Metadata of files and blocks
- DataNode = Data and blocks of files
- Replication = Redundancy and Reliability of data
- Rack awareness = Resource and Resilience optimization