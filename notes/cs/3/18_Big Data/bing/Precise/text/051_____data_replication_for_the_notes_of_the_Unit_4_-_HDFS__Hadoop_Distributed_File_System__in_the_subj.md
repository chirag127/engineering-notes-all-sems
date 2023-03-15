### Data Replication in HDFS

- Data replication is the process of storing multiple copies of data across different nodes in a distributed system.
- In Hadoop Distributed File System (HDFS), data replication is used to ensure data availability and fault tolerance.
- When a file is uploaded to HDFS, it is split into blocks and each block is replicated across multiple DataNodes.
- The default replication factor in HDFS is 3, meaning that each block is stored on 3 different DataNodes.
- The replication factor can be configured by the user to meet the specific needs of their data and system.
- The NameNode is responsible for managing the replication of data blocks and keeping track of where each block is stored.
- In the event of a DataNode failure, the NameNode will initiate the replication of the lost blocks to other DataNodes to ensure data availability.
- Data replication in HDFS helps to prevent data loss and ensures that data is always available for processing, even in the event of hardware failures.