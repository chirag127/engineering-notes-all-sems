 Here is the formal write-up on data replication in HDFS:

#### Data Replication in HDFS

1. HDFS stores multiple replicas of data blocks across different DataNodes in the cluster to ensure high availability and fault tolerance. This replication of data blocks is known as data replication.
2. The default replication factor in HDFS is 3, which means that for every data block, there will be 3 replicas stored on different DataNodes. This can be configured as required.
3. Data replication provides protection against datanode failures, disk failures or rack failures. Even if one or two replicas are unavailable, the data can be accessed from the third replica. This ensures high availability of data.
4. The location of replicas is carefully selected by the NameNode for efficient data access while providing fault tolerance. The first replica is stored on the local rack, the second replica on a different rack, and the third replica on a different rack. This placement strategy minimizes data loss in case of rack failures or network partitions.
5. The replication process is fully automated and is handled by the NameNode. The NameNode tracks the number of replicas of data blocks and regularly checks for under-replicated or over-replicated blocks. It then triggers the replication of under-replicated blocks and the deletion of over-replicated blocks. This ensures that the right number of replicas are maintained for all data blocks across the cluster.
6. Data replication incurs additional storage space overhead but provides high data availability and fault tolerance. The replication factor can be adjusted based on the number of replicas required and the storage space availability.