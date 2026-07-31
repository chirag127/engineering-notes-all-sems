# Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that handles large data sets running on commodity hardware. It is one of the major components of Apache Hadoop, the others being MapReduce and YARN.

## HDFS Architecture

HDFS has a master-slave architecture that consists of the following components:

- **NameNode**: The master node that manages the file system namespace and regulates access to files by clients. It also maintains the metadata of the file system, such as the file hierarchy, the locations of blocks, the replication factor, etc. There is only one active NameNode in a cluster, and it is a single point of failure.
- **DataNode**: The slave nodes that store and serve the data blocks of files. They also perform block operations such as creation, deletion, replication, etc. as instructed by the NameNode. There can be multiple DataNodes in a cluster, and each DataNode can store multiple blocks of different files.
- **Secondary NameNode**: An optional node that periodically merges the namespace image and the edit log of the NameNode to prevent the edit log from becoming too large. It also acts as a backup for the NameNode in case of failure. It is not a standby NameNode, and it does not serve client requests.
- **Client**: The node that accesses the file system and performs read and write operations. It interacts with the NameNode to get the metadata of the file system and the locations of the blocks, and then directly communicates with the DataNodes to transfer the data.

The following diagram illustrates the HDFS architecture:

![HDFS Architecture](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/images/hdfsarchitecture.png)

## HDFS Features

HDFS has the following features that make it suitable for storing and processing large-scale data  :

- **Scalability**: HDFS can scale horizontally by adding more DataNodes to the cluster without affecting the performance. It can also scale vertically by increasing the storage capacity of each DataNode. HDFS can support thousands of nodes and petabytes of data in a single cluster.
- **Fault-tolerance**: HDFS can tolerate failures of nodes, disks, and network by replicating the data blocks across multiple DataNodes. It also detects and recovers from failures automatically by re-replicating the missing blocks or switching to another replica. HDFS also supports snapshots and backups for disaster recovery.
- **High-throughput**: HDFS can provide high-throughput access to data by using a large block size (typically 128 MB or 256 MB) and streaming data transfer. It also supports data locality by placing the data close to the computation, which reduces the network overhead and improves the performance.
- **Reliability**: HDFS ensures the reliability of data by performing checksum verification on each block. It also supports atomic and consistent operations on files, such as create, rename, delete, append, etc. HDFS also maintains the durability of data by syncing the metadata and the data to persistent storage.
- **Simplicity**: HDFS has a simple and intuitive file system namespace that follows the Unix conventions. It also has a simple and modular design that makes it easy to understand and extend. HDFS also provides a simple and uniform interface for accessing data from different sources and formats.

## HDFS Operations

HDFS supports the following operations on files and directories :

- **Create**: To create a new file or directory in the file system. The client specifies the file name, the replication factor, the block size, and the permission for the file. The NameNode allocates a unique file identifier and records the metadata of the file. The client then writes the data to the DataNodes in the form of blocks.
- **Read**: To read an existing file from the file system. The client requests the NameNode for the locations of the blocks of the file. The NameNode returns the list of DataNodes that have the replicas of the blocks. The client then reads the data from the DataNodes in parallel.
- **Write**: To write data to an existing file in the file system. The client requests the NameNode for a new block for the file. The NameNode returns the list of DataNodes that can store the replica of the block. The client then writes the data to the DataNodes in a pipeline fashion.
- **Append**: To append data to an existing file in the file system. The client requests the NameNode for the last block of the file.