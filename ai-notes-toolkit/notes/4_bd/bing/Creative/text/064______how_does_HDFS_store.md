#### How does HDFS store

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system for storing large amounts of data in a distributed manner.
- HDFS splits a file into one or more blocks, each of which has a fixed size (default 128 MB, but configurable) and a unique identifier.
- HDFS stores these blocks on different DataNodes, which are the worker nodes in the Hadoop cluster. Each DataNode can store multiple blocks from different files.
- HDFS also maintains a file system namespace, which is a hierarchical structure of directories and files. The namespace is managed by the NameNode, which is the master node in the Hadoop cluster.
- The NameNode keeps track of the metadata of the files and blocks, such as the file name, size, permissions, locations of the blocks, etc. The NameNode does not store the actual data of the blocks, only the metadata.
- The NameNode communicates with the DataNodes to perform file system operations, such as creating, deleting, reading, and writing files. The NameNode also monitors the health and status of the DataNodes, and balances the load and replication of the blocks across the cluster.
- HDFS provides high availability, reliability, and scalability by replicating each block on multiple DataNodes (default 3, but configurable). This ensures that the data is not lost or corrupted due to node failures, network issues, or disk errors.
- HDFS also supports fault tolerance and recovery mechanisms, such as heartbeat messages, block reports, checksums, snapshots, and safemode. These features help to detect and handle failures, and restore the system to a consistent state.