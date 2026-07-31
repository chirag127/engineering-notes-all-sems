### Unit 4 - HDFS (Hadoop Distributed File System)

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is a part of the Apache Hadoop project and is used to store and manage large data sets.

1. **Architecture:** HDFS has a master/slave architecture. The master node, called the NameNode, manages the file system namespace and regulates access to files by clients. The slave nodes, called DataNodes, store the actual data.
2. **Data Replication:** HDFS replicates data blocks across multiple DataNodes to ensure data availability and fault tolerance. The default replication factor is 3, meaning that each data block is stored on 3 different DataNodes.
3. **Data Blocks:** HDFS stores files as a sequence of blocks. The default block size is 128 MB, but it can be configured by the user.
4. **Data Integrity:** HDFS uses checksums to ensure data integrity. When a client writes data to HDFS, it computes a checksum for each data block and sends it to the DataNode along with the data. The DataNode verifies the checksum before storing the data.
5. **Scalability:** HDFS is designed to scale to thousands of nodes and petabytes of data. It can handle large files and high throughput.
6. **High Availability:** HDFS supports high availability through the use of multiple NameNodes. In this configuration, one NameNode is active and the others are in standby mode. If the active NameNode fails, one of the standby NameNodes can take over without any data loss.