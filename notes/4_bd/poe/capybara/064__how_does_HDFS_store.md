#### How Does HDFS Store?

Hadoop Distributed File System (HDFS) is designed to store and manage large amounts of data on a cluster of commodity hardware. Here are the key points on how HDFS stores data:

- **Data is split into blocks:** When a file is uploaded to HDFS, it is split into multiple blocks of a fixed size (default is 128 MB). Each block is stored separately on different DataNodes in the cluster. This design ensures that large files can be processed efficiently by parallelizing the read/write operations across multiple nodes.

- **Replication:** To ensure data availability and fault tolerance, each block is replicated across multiple DataNodes (default is 3 replicas). HDFS replicates blocks across different racks to ensure that a single rack failure does not result in data loss.

- **NameNode and DataNodes:** HDFS has two types of nodes - NameNode and DataNodes. NameNode manages the file system namespace and maintains the metadata of all the files in HDFS. It keeps track of the location of each block on the DataNodes. DataNodes, on the other hand, store the actual data.

- **Data locality:** HDFS tries to maximize data locality by storing data on the node where it will be processed. When a client wants to read a file, the NameNode returns the location of the blocks, and the client reads the data from the nearest DataNode.

- **Checksums and replication:** HDFS uses checksums to ensure data integrity. When a client writes a block, HDFS computes a checksum for the data and stores it along with the block. When a DataNode receives a block, it verifies the checksum and reports any errors to the NameNode. If a replica is found to be corrupt, HDFS replicates it from another replica.

- **Balancing the data:** Over time, the distribution of data across DataNodes may become uneven. HDFS provides a tool called balancer to balance the data across nodes. The balancer moves blocks from heavily loaded nodes to lightly loaded nodes, ensuring that all nodes have roughly the same amount of data.

In summary, HDFS stores data by splitting it into blocks, replicating them across DataNodes, maintaining metadata on NameNode, maximizing data locality, ensuring data integrity with checksums, and balancing the data distribution across nodes.