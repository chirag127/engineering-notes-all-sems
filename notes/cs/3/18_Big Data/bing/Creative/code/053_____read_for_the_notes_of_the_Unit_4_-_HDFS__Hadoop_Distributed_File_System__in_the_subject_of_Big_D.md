Hello, I am Sydney, your AI assistant. I will help you with your request. Here are the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data:

```markdown
# Unit 4 - HDFS (Hadoop Distributed File System)

## Introduction
- HDFS is a distributed file system that runs on commodity hardware and provides high throughput access to large datasets.
- HDFS is designed to store and process very large files (typically in the range of gigabytes to terabytes) across multiple nodes in a cluster.
- HDFS is one of the core components of the Apache Hadoop framework, which supports various data-intensive applications such as MapReduce, Spark, Hive, HBase, etc.
- HDFS follows a master-slave architecture, where a single NameNode manages the file system namespace and metadata, and multiple DataNodes store and serve the actual data blocks.
- HDFS provides fault tolerance, scalability, reliability, and high availability by replicating data blocks across multiple DataNodes and performing checksums and automatic recovery in case of failures.

## Features of HDFS
- HDFS supports a write-once-read-many model, where files are appended to but not modified after creation.
- HDFS supports a hierarchical file system namespace, where files are organized into directories and subdirectories.
- HDFS supports a default block size of 128 MB, which can be configured for different files and applications.
- HDFS supports a default replication factor of 3, which can be configured for different files and directories.
- HDFS supports rack awareness, where the NameNode tries to place replicas of data blocks on different racks to improve data locality and network bandwidth utilization.
- HDFS supports various commands and APIs to interact with the file system, such as `hadoop fs`, `hdfs dfs`, `hadoop fsck`, `hdfs admin`, etc.
- HDFS supports various tools and utilities to monitor and manage the file system, such as `hdfs dfsadmin`, `hdfs balancer`, `hdfs fsimage`, `hdfs oiv`, etc.

## Components of HDFS
- NameNode: The master node that maintains the file system namespace and metadata, such as file names, permissions, locations, etc. The NameNode also coordinates the data access and replication among the DataNodes. The NameNode stores the metadata in memory for fast access and in persistent storage for durability. The NameNode can be configured to run in a single or a high-availability mode, where a standby NameNode takes over in case of a failure.
- DataNode: The slave node that stores and serves the data blocks of the files. The DataNode periodically sends heartbeat and block report messages to the NameNode to report its status and the blocks it holds. The DataNode also performs local checksum verification and block recovery in case of corruption or disk failure. The DataNode can be configured to run on a single or multiple disks per node.
- Secondary NameNode: An optional node that performs periodic checkpoints of the NameNode's metadata and merges it with the edit log to create a new fsimage file. The Secondary NameNode helps to reduce the startup time of the NameNode and the size of the edit log. The Secondary NameNode is not a backup or a failover for the NameNode, and it does not serve any client requests.
- Client: The node that accesses the file system and performs read and write operations. The client interacts with the NameNode to obtain the metadata and the locations of the data blocks, and then directly communicates with the DataNodes to transfer the data. The client also performs caching, buffering, and checksum verification to optimize the data access and ensure data integrity.

## Data Flow in HDFS
- Write Operation: The client initiates a write operation by requesting the NameNode to create a new file in the file system namespace. The NameNode checks the permissions and the availability of the file name, and returns a successful response to the client. The client then requests the NameNode for a list of DataNodes to store the first block of the file. The NameNode returns a list of DataNodes based on the replication factor and the rack awareness policy. The client then writes the data to the first DataNode in the list, which in turn replicates the data to the next DataNode in the list, and so on. The client receives an acknowledgment from the last DataNode in the list, and then requests the NameNode for a new list of DataNodes for the next block of the file. The process repeats until the file is complete. The client then closes the file and notifies the NameNode.
- Read Operation: The client initiates a read operation by requesting the NameNode for the locations of the data blocks of the file. The NameNode