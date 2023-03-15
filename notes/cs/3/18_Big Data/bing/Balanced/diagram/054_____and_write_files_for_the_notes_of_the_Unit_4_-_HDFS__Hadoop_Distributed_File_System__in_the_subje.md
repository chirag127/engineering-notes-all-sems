# Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that handles large data sets running on commodity hardware. It is used to scale a single Apache Hadoop cluster to hundreds (and even thousands) of nodes. HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN.

## HDFS Architecture

HDFS has a master-slave architecture that consists of the following components:

- **NameNode**: The master node that manages the file system namespace and regulates access to files by clients. It also maintains the metadata of the file system, such as the file hierarchy, the locations of blocks, the replication factor, etc. There is only one active NameNode in a cluster, and it is a single point of failure. To avoid data loss, the NameNode stores its metadata in multiple locations, such as local disk, remote disk, and memory.

- **DataNode**: The slave nodes that store and serve the data blocks of files. They also perform block operations, such as creation, deletion, replication, etc., as instructed by the NameNode. There can be multiple DataNodes in a cluster, and each DataNode can store multiple blocks of data.

- **Secondary NameNode**: An optional node that performs periodic checkpoints of the file system metadata from the NameNode. It is not a backup or failover node, but rather a helper node that reduces the startup time of the NameNode and the size of the edit log.

- **Client**: The node that accesses the file system and performs read and write operations on files. The client interacts with the NameNode to get the metadata of files and blocks, and with the DataNodes to read and write the data blocks.

The following diagram illustrates the HDFS architecture:

![HDFS Architecture](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/images/hdfsarchitecture.png)

## HDFS Features

HDFS has the following features that make it suitable for storing and processing large data sets in a distributed environment:

- **Fault-tolerance**: HDFS can tolerate failures of nodes and disks by replicating the data blocks across multiple DataNodes. The default replication factor is 3, which means that each block is stored on three different DataNodes. The NameNode monitors the health and availability of the DataNodes, and initiates the replication or recovery of blocks when needed.

- **Scalability**: HDFS can scale horizontally by adding more DataNodes to the cluster. The NameNode can handle millions of files and blocks, and the DataNodes can store petabytes of data. The file system namespace can also be federated by having multiple NameNodes that manage different portions of the namespace.

- **High-throughput**: HDFS can provide high-throughput access to data by using large blocks (typically 128 MB or 256 MB) and streaming data transfer. Large blocks reduce the overhead of managing the metadata and the number of disk seeks, and streaming data transfer utilizes the network bandwidth efficiently.

- **Data locality**: HDFS can optimize the data processing by moving the computation to the data, rather than moving the data to the computation. This reduces the network traffic and improves the performance. HDFS works well with MapReduce, which is a programming model that exploits the data locality by running the map tasks on the nodes where the data blocks are located.

- **Simple and robust**: HDFS has a simple and robust design that is easy to use and maintain. It follows the write-once-read-many model, which means that the files are not modified once they are written. This simplifies the data consistency and concurrency issues. HDFS also provides a command-line interface and a web interface for users and administrators to interact with the file system.

## HDFS Operations

HDFS supports the following operations on files and directories:

- **Create**: To create a new file or directory in HDFS, the client contacts the NameNode and requests for a new file or directory name. The NameNode checks if the name already exists or not, and if not, it allocates a new inode for the file or directory and updates the file system metadata.

- **Read**: To read a file from HDFS, the client contacts the NameNode and requests for the locations of the blocks of the file. The NameNode returns the list of DataNodes that store the blocks of the file. The client then contacts one of the DataNodes and requests for the block data. The DataNode sends the block data to the client in a streaming manner.

- **Write**: To write a file