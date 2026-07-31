# Data flow for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

HDFS is a distributed file system that stores large data sets across multiple nodes in a cluster. It provides high throughput, fault tolerance, and scalability for big data applications. HDFS has a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as the DataNodes (slaves).

The data flow in HDFS involves the following steps:

- The client application splits the input data into fixed-size blocks (typically 128 MB or 256 MB) and writes them to HDFS.
- The client contacts the NameNode and requests permission to write the blocks to HDFS. The NameNode checks the available space and replication factor of the blocks and returns a list of DataNodes to the client.
- The client writes the first block to the first DataNode in the list. The DataNode replicates the block to the next DataNode in the list, and so on, until the replication factor is met. The client receives an acknowledgment from the DataNodes after the block is written and replicated.
- The client repeats the same process for the remaining blocks, writing them to different DataNodes in the cluster. The client also sends a block report to the NameNode, informing it about the location of the blocks.
- The NameNode maintains the metadata of the blocks, such as their names, sizes, locations, and replication factors, in its memory. The NameNode also periodically receives heartbeats from the DataNodes, indicating their status and availability.
- The client can read the data from HDFS by contacting the NameNode and requesting the location of the blocks. The NameNode returns the list of DataNodes that have the blocks, and the client reads the blocks from the closest DataNode. The client can also perform checksum verification to ensure the integrity of the data.