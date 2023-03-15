### Data Flow in HDFS (Hadoop Distributed File System)

HDFS is a distributed file system designed to store large data sets across multiple machines. Here are some key points about data flow in HDFS:

1. **Data Blocks**: HDFS divides files into blocks, which are distributed across the nodes in the cluster. Each block is typically 128 MB in size.

2. **Data Replication**: HDFS replicates each block across multiple nodes to ensure data availability and fault tolerance. The default replication factor is 3, meaning that each block is stored on 3 different nodes.

3. **Data Writing**: When a client writes data to HDFS, the data is first written to the local disk of the client machine. The client then contacts the NameNode to obtain a list of DataNodes where the data blocks should be stored. The client then sends the data to the first DataNode in the list, which stores the data and forwards it to the next DataNode in the list, and so on.

4. **Data Reading**: When a client reads data from HDFS, it contacts the NameNode to obtain the locations of the data blocks. The client then reads the data directly from the DataNodes.

5. **Data Integrity**: HDFS uses checksums to ensure data integrity. When a client writes data to HDFS, it computes a checksum for each block and sends it along with the data. When a client reads data from HDFS, it verifies the checksum to ensure that the data has not been corrupted.

6. **Data Balancing**: HDFS periodically rebalances data across the nodes in the cluster to ensure that data is evenly distributed. This helps to ensure that the cluster is utilized efficiently and that data is available even if some nodes fail.
