#### HDFS concepts

HDFS (Hadoop Distributed File System) is a distributed file system designed to run on commodity hardware. It is highly fault-tolerant and is designed to be deployed on low-cost hardware. HDFS provides high throughput access to application data and is suitable for applications that have large data sets.

Some of the key concepts of HDFS include:

- **NameNode and DataNode**: HDFS has a master/slave architecture. The NameNode is the master server that manages the file system namespace and regulates access to files by clients. The DataNodes are the slave servers that manage the storage attached to the nodes that they run on.

- **Block size**: HDFS stores large files as a sequence of blocks. The default block size is 64MB, but it can be configured by the user.

- **Replication**: HDFS replicates each block of data on multiple DataNodes to ensure high availability and fault tolerance. The default replication factor is 3, but it can be configured by the user.

- **Rack awareness**: HDFS is designed to be aware of the network topology of the cluster. It tries to place replicas of data blocks on different racks to improve data reliability and availability.

- **Data locality**: HDFS tries to schedule tasks on the same node where the data is stored, or as close as possible, to reduce network traffic and improve performance.

- **Scalability**: HDFS is designed to scale to thousands of nodes and petabytes of data.
