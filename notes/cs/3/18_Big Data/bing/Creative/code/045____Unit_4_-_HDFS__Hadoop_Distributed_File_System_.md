Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 4 - HDFS (Hadoop Distributed File System):

```markdown
# Unit 4 - HDFS (Hadoop Distributed File System)

## Introduction
- HDFS is a distributed file system that runs on commodity hardware and provides high throughput access to large data sets.
- HDFS is designed to store and process very large files (typically in the range of gigabytes to terabytes) across multiple nodes in a cluster.
- HDFS is one of the core components of the Apache Hadoop framework, which supports various data-intensive applications such as MapReduce, Spark, Hive, etc.

## Features of HDFS
- HDFS has the following features:
  - Fault tolerance: HDFS can tolerate failures of nodes, disks, and network by replicating data blocks across multiple nodes. HDFS also provides mechanisms for detecting and recovering from failures.
  - Scalability: HDFS can scale horizontally by adding more nodes to the cluster without affecting the performance or availability of the system.
  - High availability: HDFS can provide continuous service even in the presence of node failures by using techniques such as namenode federation and high availability (HA) namenode.
  - Data locality: HDFS tries to place data blocks close to the nodes where they are needed for processing, thus reducing the network overhead and improving the performance.
  - Rack awareness: HDFS can take into account the physical location of nodes in different racks and optimize the data placement and replication accordingly, thus enhancing the fault tolerance and network bandwidth utilization.
  - Compression and encryption: HDFS supports various compression and encryption algorithms to reduce the storage space and enhance the security of data.

## Architecture of HDFS
- HDFS has a master-slave architecture, where a single master node called the namenode manages the metadata of the file system, and multiple slave nodes called the datanodes store the actual data blocks of the files.
- A file in HDFS is divided into fixed-size blocks (default 128 MB) and distributed across multiple datanodes. Each block is replicated a number of times (default 3) for fault tolerance.
- The namenode maintains the namespace of the file system, which is a hierarchical directory tree of files and directories. The namenode also keeps track of the mapping of files to blocks and blocks to datanodes.
- The datanodes are responsible for storing, serving, and replicating the data blocks assigned to them. The datanodes periodically send heartbeat and block report messages to the namenode to report their status and the list of blocks they have.
- The clients interact with the namenode to perform operations such as creating, deleting, renaming, or opening files and directories. The namenode returns the list of datanodes that have the blocks of the requested file. The clients then directly communicate with the datanodes to read or write the data blocks.
- HDFS also has a secondary namenode, which is not a backup of the namenode, but a helper node that periodically merges the namenode's memory image (fsimage) and edit log (edits) into a new fsimage. This reduces the startup time of the namenode and the size of the edit log.

## HDFS Commands
- HDFS provides a command-line interface (CLI) to interact with the file system. The CLI can be accessed by using the `hdfs dfs` command, followed by the subcommand and arguments. For example, `hdfs dfs -ls /` lists the files and directories in the root directory of HDFS.
- Some of the common HDFS commands are:
  - `hdfs dfs -mkdir`: creates a directory in HDFS.
  - `hdfs dfs -put`: copies a file from the local file system to HDFS.
  - `hdfs dfs -get`: copies a file from HDFS to the local file system.
  - `hdfs dfs -cat`: displays the contents of a file in HDFS.
  - `hdfs dfs -rm`: deletes a file or directory in HDFS.
  - `hdfs dfs -cp`: copies a file or directory within HDFS.
  - `hdfs dfs -mv`: moves or renames a file or directory within HDFS.
  - `hdfs dfs -du`: displays the disk usage of a file or directory in HDFS.
  - `hdfs dfs -df`: displays the available and used space in HDFS.
  - `hdfs dfs -setrep`: changes the replication factor of a file or directory in HDFS.
  - `hdfs dfs -chmod`: changes the permissions of a file or directory