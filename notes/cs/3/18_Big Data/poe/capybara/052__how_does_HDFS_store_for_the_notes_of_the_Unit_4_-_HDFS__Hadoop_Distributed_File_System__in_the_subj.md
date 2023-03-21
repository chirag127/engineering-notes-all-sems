### How Does HDFS Store

HDFS (Hadoop Distributed File System) is the primary storage system used in Hadoop. It is designed to store large amounts of data across a cluster of commodity hardware. Here's how HDFS stores data:

- Data is divided into blocks: When a file is added to HDFS, it is divided into smaller blocks of a fixed size, typically 128 MB or 256 MB. These blocks are then distributed across the nodes in the cluster.

- Replication: HDFS stores multiple copies of each block to ensure data availability and reliability. By default, each block is replicated three times, but this can be configured based on the needs of the system.

- Namenode and Datanodes: HDFS consists of two types of nodes - Namenode and Datanodes. The Namenode stores the metadata of the files, such as the location of the blocks and their replicas. The Datanodes store the actual data blocks.

- Rack Awareness: HDFS is aware of the rack topology of the cluster. It tries to store the replicas of a block on different racks to ensure data reliability in case of a rack failure.

- Data locality: HDFS prioritizes data locality, which means that it tries to store data on the node where it will be processed. This reduces network traffic and improves performance.

- Balancing the cluster: HDFS continuously monitors the usage of the nodes in the cluster and balances the data across the nodes to ensure that no node is overloaded or underutilized.

- Checksums: HDFS uses checksums to ensure data integrity. It calculates a checksum for each block and verifies it during reads to ensure that the data has not been corrupted.

In summary, HDFS stores data by dividing it into blocks, replicating each block, storing metadata on the Namenode, and actual data on the Datanodes. It is designed to ensure data availability, reliability, and performance across a cluster of commodity hardware.