### How does HDFS store data?

- HDFS (Hadoop Distributed File System) is a distributed file system that runs on a cluster of nodes and stores large amounts of data in a scalable and fault-tolerant way.
- HDFS exposes a file system namespace and allows user data to be stored in files.
- Internally, a file is split into one or more blocks and these blocks are stored in a set of DataNodes. A DataNode is a node in the cluster that stores and manages the data blocks.
- The default size of each data block is 128 MB, which can be configured in the hdfs-site.xml file.
- The NameNode is the master node in the cluster that executes file system namespace operations like opening, closing, and renaming files and directories. It also maintains the metadata of the file system, such as the file names, permissions, locations of the blocks, etc.
- The NameNode communicates with the DataNodes to manage the placement and replication of the blocks. It also handles the read and write requests from the clients.
- HDFS stores the data in a distributed manner. It divides the data into small pieces and stores it on different DataNodes in the cluster. In this manner, HDFS provides a way for MapReduce to process a subset of large data sets broken into blocks, parallelly on several nodes.
- HDFS also provides high availability and reliability by replicating the blocks across multiple DataNodes. The default replication factor is 3, which means each block is copied to 3 different DataNodes. This ensures that the data is not lost even if some DataNodes fail or become unavailable.
- HDFS also supports features such as compression, encryption, snapshots, quotas, trash, etc. to enhance the performance and security of the data.