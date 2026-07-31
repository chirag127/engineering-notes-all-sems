### Data Replication in HDFS

- Data replication is the process of copying data from one HDFS service to another, or to and from other storage systems such as Amazon S3 or Microsoft ADLS.
- Data replication is used for fault tolerance, backup, disaster recovery, and data availability.
- HDFS stores each file as a sequence of blocks, which are replicated across different nodes in the cluster .
- The block size and the replication factor are configurable per file . The default block size is 128 MB and the default replication factor is 3.
- The NameNode is responsible for managing the metadata of the files and blocks, and assigning the replication targets for each block .
- The DataNodes are responsible for storing the blocks and performing the replication tasks as instructed by the NameNode .
- The replication process follows these steps:
  - A client writes data to an HDFS file with a specified replication factor.
  - The NameNode retrieves the list of DataNodes using a replication target choosing algorithm. This list contains the DataNodes that will store the replicas of the block.
  - The client writes data to the first DataNode in the list. The first DataNode starts receiving the data in small packets and stores each packet in a temporary file.
  - The first DataNode forwards the data packets to the second DataNode in the list. The second DataNode does the same as the first DataNode and forwards the data packets to the third DataNode, and so on.
  - When the block is written, the first DataNode notifies the NameNode. The NameNode updates the metadata of the file and the block, and marks the block as completed.
  - The NameNode periodically receives block reports from the DataNodes, which contain the list of blocks stored on each DataNode. The NameNode uses these reports to verify the consistency and availability of the blocks in the cluster.
  - If a block is under-replicated (i.e., the number of replicas is less than the replication factor), the NameNode initiates the replication of the block to another DataNode. If a block is over-replicated (i.e., the number of replicas is more than the replication factor), the NameNode deletes the excess replicas.