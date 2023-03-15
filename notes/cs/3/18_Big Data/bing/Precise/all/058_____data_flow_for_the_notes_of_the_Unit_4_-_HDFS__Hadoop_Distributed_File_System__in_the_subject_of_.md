# Data Flow in HDFS (Hadoop Distributed File System)

HDFS is a distributed file system designed to store large data sets reliably and to stream those data sets at high bandwidth to user applications. The data flow in HDFS involves the following steps:

1. **Client writes data to HDFS:** When a client wants to write data to HDFS, it first contacts the NameNode, which is the master server that manages the file system namespace and regulates access to files by clients. The NameNode responds with the identity of the DataNodes that will store the replicas of the data.

2. **Data is split into blocks:** The data is split into blocks, and each block is stored on a different DataNode. The default block size is 128 MB, but it can be configured by the user.

3. **Data is replicated:** HDFS replicates each block of data on multiple DataNodes for fault tolerance. The default replication factor is 3, but it can be configured by the user.

4. **Client reads data from HDFS:** When a client wants to read data from HDFS, it contacts the NameNode to determine the location of the data. The NameNode responds with the identity of the DataNodes that have the replicas of the data. The client then reads the data directly from the DataNodes.

5. **Data is transferred between DataNodes:** Data can be transferred between DataNodes for the purpose of rebalancing, replication, and recovery. The NameNode is responsible for orchestrating the data transfer.

6. **Data is checked for integrity:** HDFS uses checksums to ensure the integrity of data stored on DataNodes. When a client reads data from a DataNode, it verifies the checksums to ensure that the data has not been corrupted during transmission or storage.

In summary, the data flow in HDFS involves writing data to DataNodes, splitting data into blocks, replicating data for fault tolerance, reading data from DataNodes, transferring data between DataNodes, and checking data for integrity. The NameNode plays a central role in managing the file system namespace and regulating access to files by clients.