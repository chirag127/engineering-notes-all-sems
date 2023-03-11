### How Does HDFS Store

HDFS (Hadoop Distributed File System) is a distributed file system designed to store large files and data sets across multiple nodes in a Hadoop cluster. Here's how HDFS stores data:

1. **Data Blocks:** HDFS stores data in the form of blocks, which are typically 128 MB or 256 MB in size. These blocks are stored across multiple nodes in the cluster, ensuring that data is distributed and replicated for fault tolerance.

2. **Replication:** HDFS replicates data blocks across multiple nodes in the cluster to ensure redundancy and fault tolerance. By default, HDFS stores three replicas of each block, but this can be configured to a different number based on the requirements of the system.

3. **NameNode and DataNodes:** HDFS has two main components: the NameNode and DataNodes. The NameNode is responsible for managing the metadata of the file system, such as the location of data blocks and their replicas. The DataNodes are responsible for storing and managing the actual data blocks.

4. **Data Locality:** HDFS tries to ensure that data is stored and processed on the same node or rack as the computation that needs it. This is known as data locality and can help to reduce network congestion and improve performance.

5. **Checksums:** HDFS uses checksums to ensure data integrity. Each block is assigned a checksum, which is calculated by the DataNode before it is stored. When the block is read, the checksum is verified to ensure that the data has not been corrupted.

6. **Compression and Encryption:** HDFS supports compression and encryption of data at rest. Compression can help to reduce storage requirements, while encryption can improve security.

Overall, HDFS is designed to be a scalable and fault-tolerant file system that can handle large amounts of data. Its distributed nature and replication strategy help to ensure that data is always available, even in the event of node failures or other issues.