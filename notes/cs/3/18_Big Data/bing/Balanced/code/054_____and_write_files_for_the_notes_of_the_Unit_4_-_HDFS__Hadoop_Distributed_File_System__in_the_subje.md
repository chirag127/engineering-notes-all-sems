# Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that is designed to run on commodity hardware and handle large data sets. It is a part of the Apache Hadoop project and provides high throughput, fault tolerance, and scalability.

## HDFS Architecture

HDFS has a master-slave architecture, where the master node is called the NameNode and the slave nodes are called the DataNodes. The NameNode manages the file system namespace, the metadata of the files and directories, and the access control of the clients. The DataNodes store the actual data blocks of the files and perform read and write operations as instructed by the NameNode.

A file in HDFS is divided into fixed-size blocks (typically 64 MB or 128 MB) and distributed across the DataNodes. Each block is replicated a number of times (default is 3) for fault tolerance. The NameNode maintains the mapping of the file blocks to the DataNodes and the replication factor of each block. The DataNodes periodically send heartbeat and block report messages to the NameNode to report their status and the blocks they are holding.

HDFS follows a write-once-read-many model, where a file once created, written, and closed, cannot be modified. This simplifies the data consistency and coherency issues. HDFS also supports appending data to existing files, but not random writes.

## HDFS Features

Some of the main features of HDFS are:

- **Scalability**: HDFS can scale up to thousands of nodes and store petabytes of data.
- **Fault tolerance**: HDFS can tolerate the failure of nodes by replicating the data blocks across multiple nodes. It also supports checksums to detect and correct corrupted blocks.
- **High throughput**: HDFS can provide high throughput access to the data by streaming the data blocks in parallel from multiple DataNodes.
- **Cost effectiveness**: HDFS can run on commodity hardware, which reduces the cost of storage and processing.
- **Portability**: HDFS can run on various platforms and operating systems, as it is implemented in Java.
- **Compatibility**: HDFS can integrate with other Hadoop components, such as MapReduce, YARN, Hive, Pig, etc.

## HDFS Commands

Some of the common HDFS commands are:

- `hadoop fs -ls`: List the files and directories in a given path.
- `hadoop fs -mkdir`: Create a directory in HDFS.
- `hadoop fs -put`: Copy a file from the local file system to HDFS.
- `hadoop fs -get`: Copy a file from HDFS to the local file system.
- `hadoop fs -cat`: Display the contents of a file in HDFS.
- `hadoop fs -rm`: Delete a file or directory in HDFS.
- `hadoop fs -du`: Display the disk usage of a file or directory in HDFS.
- `hadoop fs -df`: Display the available and used space in HDFS.
- `hadoop fs -chmod`: Change the permissions of a file or directory in HDFS.
- `hadoop fs -help`: Display the help message for a command or subcommand.