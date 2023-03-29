
### Data Replication for Unit 4 - HDFS (Hadoop Distributed File System)

1. Data replication is the process of making copies of data over a network, usually to ensure redundancy and to increase data availability.
2. HDFS (Hadoop Distributed File System) is a distributed file system designed to store and manage large amounts of data across a cluster of commodity hardware.
3. HDFS replicates data blocks across multiple nodes in the cluster to improve fault tolerance and availability of data.
4. The replication factor of a file is the number of times a file is replicated across the cluster. By default, HDFS will replicate each file three times.
5. The replication factor of a file can be changed to any number between 1 and the number of nodes in the cluster.
6. The replication factor of a file can be changed dynamically, allowing administrators to adjust the replication factor based on the importance of the data.
7. HDFS also provides a mechanism for rebalancing data across the cluster. This allows administrators to move blocks from over-utilized nodes to under-utilized nodes to ensure even distribution of data.