# How does HDFS store data?

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data processing.
- HDFS stores data in a distributed manner by dividing files into fixed-size blocks (typically 64 MB or 128 MB) and storing each block on a different node in the cluster.
- HDFS has a master-slave architecture, where the master node is called the NameNode and the slave nodes are called the DataNodes.
- The NameNode is responsible for managing the namespace, the metadata, and the access control of the files and directories in HDFS. It also maintains the mapping of blocks to DataNodes and the replication factor of each block.
- The DataNodes are responsible for storing the actual data blocks and serving read and write requests from clients. They also periodically send heartbeat and block report messages to the NameNode to report their status and the blocks they hold.
- HDFS provides high availability and fault tolerance by replicating each block across multiple DataNodes (usually three) in different racks. This ensures that the data can be accessed even if some DataNodes fail or become unavailable.
- HDFS also supports rack awareness, which means that the NameNode is aware of the physical location of the DataNodes in terms of racks. This helps to optimize the data placement and reduce the network bandwidth consumption.
- HDFS follows the write-once-read-many-times pattern, which means that the data blocks are immutable once written and can be read multiple times by different clients. This simplifies the concurrency control and improves the performance of data processing.