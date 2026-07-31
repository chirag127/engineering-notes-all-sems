# Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that is designed to run on commodity hardware and handle large data sets. It is a part of the Apache Hadoop project and provides high-throughput access to application data. HDFS has the following features and characteristics:

- **Fault-tolerance**: HDFS can tolerate failures of nodes and disks by replicating the data blocks across multiple DataNodes. The replication factor can be configured by the user. HDFS also performs checksum verification and periodic block scanning to detect and repair corrupted data.
- **Scalability**: HDFS can scale up to thousands of nodes and store petabytes of data. It distributes the data and computation across the cluster and balances the load among the nodes. HDFS also supports horizontal scaling, which means adding or removing nodes without disrupting the system.
- **High availability**: HDFS ensures that the data is always available to the applications by using a NameNode and a Secondary NameNode. The NameNode is the master server that manages the file system namespace and the metadata of the files and directories. The Secondary NameNode periodically checkpoints the namespace and helps the NameNode recover from failures. HDFS also supports Quorum Journal Manager (QJM) and ZooKeeper-based automatic failover for the NameNode.
- **Streaming access**: HDFS is optimized for streaming access to large files rather than random access to small files. It supports high bandwidth data transfer and sequential read and write operations. HDFS also relaxes some POSIX requirements to enable streaming access to file system data.
- **Simple and robust coherency model**: HDFS follows a write-once-read-many model, which means that a file can be written only once and then read by multiple readers. This simplifies the data coherency issues and avoids locking and concurrency problems. HDFS also provides atomic rename and append operations for files.

The architecture of HDFS consists of the following components:

- **NameNode**: The NameNode is the master server that manages the file system namespace and the metadata of the files and directories. It also controls the access to the files by the clients and coordinates the placement and replication of the data blocks among the DataNodes. The NameNode stores the metadata in its main memory for fast access and in persistent storage for durability. The NameNode does not store the actual data of the files.
- **DataNode**: The DataNode is the slave server that stores the actual data of the files in the form of blocks. Each block is typically 64 MB or 128 MB in size and has a unique identifier. The DataNode also performs read and write operations on the blocks as instructed by the NameNode or the clients. The DataNode periodically sends a report of the blocks it stores to the NameNode, called a block report.
- **Secondary NameNode**: The Secondary NameNode is an optional server that helps the NameNode in checkpointing and recovery. It periodically merges the namespace image and the edit log of the NameNode and creates a new namespace image. This reduces the startup time of the NameNode and the size of the edit log. The Secondary NameNode also acts as a backup for the NameNode in case of failures.
- **Client**: The client is the application that accesses the data stored in HDFS. The client interacts with the NameNode to perform file system operations such as creating, deleting, renaming, and listing files and directories. The client also interacts with the DataNode to read and write data blocks. The client caches the locations of the blocks for faster access and performs checksum verification to ensure data integrity.

The following diagram illustrates the architecture of HDFS:

![HDFS Architecture](https://hadoop.apache.org/docs/r1.2.1/images/hdfsarchitecture.gif)

Source: https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html

Some of the common commands for interacting with HDFS are:

- `hadoop fs -ls`: List the files and directories in a given path.
- `hadoop fs -mkdir`: Create a directory in a given path.
- `hadoop fs -put`: Copy a file from the local file system to HDFS.
- `hadoop fs -get`: Copy a file from HDFS to the local file system.
- `hadoop fs -cat`: Display the contents of a file in HDFS.
- `hadoop fs -rm`: Delete a file or a directory in HDFS.
- `hadoop fs -cp`: Copy a file or a directory within HDFS.
- `hadoop fs -mv`: Move or rename a file or a directory within HDFS.
- `h