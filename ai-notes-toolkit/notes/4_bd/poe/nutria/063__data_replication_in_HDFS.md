
#### Data Replication in HDFS

1. HDFS (Hadoop Distributed File System) is a distributed file system designed to store and manage large datasets across clusters of commodity servers.
2. HDFS is designed to be fault-tolerant, meaning that it can recover from hardware and software errors that occur in the system.
3. To achieve this, HDFS replicates data across multiple nodes in the cluster.
4. The replication factor is the number of replicas of a file stored in the HDFS cluster.
5. The default replication factor is three, meaning that each file is stored on three separate nodes in the cluster.
6. The replication factor can be adjusted to increase or decrease the number of replicas stored.
7. Increasing the replication factor increases the availability of the data, but also increases the amount of disk space used.
8. The replication factor can also be adjusted on a per-file basis, allowing for different levels of fault-tolerance for different files.
9. HDFS also supports block replication, which allows for blocks of data to be replicated across multiple nodes in the cluster.
10. This allows for more efficient use of disk space and better fault-tolerance for large datasets.