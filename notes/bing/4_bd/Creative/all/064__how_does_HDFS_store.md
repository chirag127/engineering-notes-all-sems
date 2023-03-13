#### How does HDFS store

- HDFS stands for Hadoop Distributed File System, which is the primary storage system used by Hadoop applications.
- HDFS stores data in a distributed manner, meaning that it divides the data into small pieces and stores them on different DataNodes in the cluster .
- Each piece of data is called a block, and the default size of each block is 128 MB, which can be configured in the hdfs-site.xml file.
- HDFS replicates each block across multiple DataNodes for fault tolerance and high availability. The default replication factor is 3, which can also be configured in the hdfs-site.xml file.
- HDFS has a master-slave architecture, where the master node is called the NameNode and the slave nodes are called the DataNodes.
- The NameNode manages the file system namespace and the metadata of all the files and directories. It also coordinates the placement and replication of blocks across the DataNodes.
- The DataNodes store the actual blocks of data and serve read and write requests from the clients. They also send periodic reports to the NameNode about the blocks they are storing and their health status.
- HDFS provides a way for MapReduce to process a subset of large data sets broken into blocks, parallelly on several nodes. This reduces the network overhead and increases the performance of data processing.

A possible mnemonic to remember the key components of HDFS is:

**H**adoop **D**istributed **F**ile **S**ystem = **H**uge **D**ata **F**ragmented and **S**tored

A possible ascii diagram to illustrate the HDFS architecture is:

```
    +-----------------+
    |    NameNode     |
    | (Master node)   |
    +-----------------+
    /       |        \
   /        |         \
  /         |          \
 /          |           \
+-----------+-----------+-----------+
| DataNode | DataNode | DataNode |
| (Slave node) | (Slave node) | (Slave node) |
+-----------+-----------+-----------+
| Block 1 | Block 2 | Block 3 |
| Block 4 | Block 5 | Block 6 |
| Block 7 | Block 8 | Block 9 |
+-----------+-----------+-----------+
```