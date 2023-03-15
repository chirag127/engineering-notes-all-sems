#### How Does HDFS Store

Hadoop Distributed File System (HDFS) is a distributed file system that is designed to store large data sets reliably and efficiently across a cluster of commodity hardware. In HDFS, data is stored in a distributed manner across the nodes in the cluster. Here's how HDFS stores data:

1. Block Storage: HDFS stores data in blocks of fixed sizes. The default block size in HDFS is 128 MB, but it can be configured to any other size as well. The data is divided into blocks before being stored, and each block is replicated across multiple nodes in the cluster for fault tolerance.

2. NameNode: HDFS has a master-slave architecture, where one node acts as the master and is called the NameNode. The NameNode is responsible for managing the file system namespace, regulating access to files by clients, and maintaining the metadata about the blocks stored on the DataNodes.

3. DataNode: All other nodes in the cluster are called DataNodes. These nodes are responsible for storing the actual data blocks and their replicas. DataNodes communicate with the NameNode periodically, and report the list of blocks they are storing. If a DataNode fails, the NameNode can identify it and replicate the lost blocks to other DataNodes.

4. Replication: Data replication is the process of creating multiple copies of data blocks and storing them on different DataNodes in the cluster. This is done for fault tolerance, so that if a DataNode fails, the data blocks can still be accessed from other nodes. By default, HDFS replicates each block three times.

5. Rack Awareness: HDFS is rack-aware, which means it takes into account the network topology of the cluster while replicating data blocks. HDFS tries to place replicas of a block on different racks in the cluster to minimize the impact of rack failures on data availability.

6. Balancing: HDFS tries to balance the block distribution across all the DataNodes in the cluster. This is done to ensure that no node becomes a hot spot, and that the data can be accessed efficiently from all nodes in the cluster.

7. Compression: HDFS supports compression of data blocks to reduce their size and improve storage efficiency. HDFS uses the DEFLATE algorithm for compression by default, but other compression algorithms can also be used.

Learning Tricks:

- Remember the acronym "BNRDDCB" to recall the components of HDFS - Block Storage, NameNode, DataNode, Replication, Rack Awareness, Balancing, and Compression.
- Visualize the blocks being stored across multiple nodes in the cluster, with the NameNode managing the metadata and the DataNodes storing the actual data blocks and their replicas.