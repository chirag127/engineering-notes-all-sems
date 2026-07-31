#### Data replication in HDFS

- Data replication is the process of copying data from one HDFS service to another, or to and from other storage systems such as Amazon S3 or Microsoft ADLS.
- Data replication is used for fault tolerance, backup, disaster recovery, and data availability.
- HDFS stores each file as a sequence of blocks, and each block is replicated across multiple DataNodes according to a replication factor .
- The default replication factor is 3, which means that each block is stored on 3 different DataNodes.
- The replication factor can be configured per file, per directory, or globally .
- The NameNode is responsible for managing the replication of blocks, and it uses a replication target choosing algorithm to select the best DataNodes for each block  .
- The algorithm considers factors such as rack awareness, network bandwidth, disk space, load balancing, and data locality  .
- The client writes data to the first DataNode in the list, and the first DataNode forwards the data to the second DataNode, and so on, until the replication factor is met  .
- The NameNode periodically receives block reports and heartbeat messages from the DataNodes, and it detects any missing or corrupted blocks .
- The NameNode initiates the replication of missing or corrupted blocks to maintain the desired replication factor .
- The NameNode also balances the distribution of blocks across the cluster to avoid hotspots and ensure even utilization of resources .