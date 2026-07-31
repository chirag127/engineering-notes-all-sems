
## Unit 4 - HDFS (Hadoop Distributed File System)

1. HDFS is a distributed file system that is designed to store and manage large amounts of data. It is implemented as part of the Hadoop framework and provides a scalable, reliable, and fault-tolerant storage layer for Hadoop clusters.

2. HDFS is a master-slave architecture, where the master node is known as the NameNode and the slave nodes are known as DataNodes. The NameNode is responsible for managing the file system namespace and mapping file blocks to DataNodes. The DataNodes are responsible for storing and retrieving file blocks from the local file system.

3. HDFS is designed to be highly fault-tolerant, which means that it can tolerate the failure of individual nodes without losing data. It does this by replicating data across multiple nodes, so that if one node fails, the data can be retrieved from another node.

4. HDFS is optimized for large files and streaming data access. It supports random read/write operations for small files, but is not optimized for them.

5. HDFS also supports features such as data compression, data encryption, and access control. These features can be used to improve performance and security.