

#### Data Replication in HDFS

- Data replication in HDFS is the process of storing multiple copies of data across multiple machines to ensure reliability and fault tolerance.
- Data is replicated on multiple nodes in order to provide high availability and fault tolerance.
- Replication also helps in increasing the throughput of the system as multiple copies of data can be read from different nodes.
- HDFS uses a replication factor to determine how many copies of data should be stored. The default replication factor is 3, which means that each block of data is stored on three different nodes.
- The replication factor can be changed according to the user’s requirements. The replication factor should be higher for critical data and lower for non-critical data.
- The replication of data is done by the NameNode. The NameNode stores the metadata about the data blocks and the nodes on which they are stored.
- The NameNode also keeps track of the number of replicas of each block and ensures that the replication factor is maintained.
- The DataNodes periodically send heartbeats to the NameNode to indicate that they are alive and available.
- The NameNode uses this information to keep track of the nodes on which data is stored and to ensure that the replication factor is maintained.
- The NameNode also replicates data when a node fails or when a new node is added to the cluster.
- HDFS also provides the user with the ability to control the replication of data. The user can specify the replication factor for specific files or directories.
- Data replication in HDFS helps to ensure the reliability and availability of data. It also helps to improve the throughput of the system as multiple copies of data can be read from different nodes.