# Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that is part of the Hadoop framework. It is designed to store and process large amounts of data across a cluster of commodity hardware. Some of the main features and characteristics of HDFS are:

- **Fault-tolerant**: HDFS can tolerate failures of nodes and disks by replicating the data blocks across multiple machines. It also detects and recovers from failures automatically.
- **High-throughput**: HDFS provides high performance for sequential read and write operations on large files. It is suitable for applications that have large data sets and need batch processing.
- **Scalable**: HDFS can scale up to thousands of nodes and petabytes of data. It can also add or remove nodes without disrupting the system.
- **POSIX-relaxed**: HDFS does not fully comply with the POSIX standards for file systems. It sacrifices some features, such as random access and file locking, to enable streaming access and high throughput.

## HDFS Architecture

HDFS follows a master/slave architecture, where a single NameNode (NN) manages the file system namespace and metadata, and multiple DataNodes (DN) store and serve the data blocks. The NameNode and DataNodes communicate with each other using heartbeats and block reports.

- **NameNode**: The NameNode is the master node that maintains the file system namespace and the mapping of files to blocks. It also handles client requests, such as creating, deleting, and renaming files and directories. The NameNode stores the metadata in memory and on disk. It also maintains a transaction log called the EditLog to record the changes to the file system. The NameNode is a single point of failure in HDFS, so it needs to be backed up by a Secondary NameNode (SNN) or a Standby NameNode (SBN) that can take over in case of failure.
- **DataNode**: The DataNode is the slave node that stores and serves the data blocks. It also performs block operations, such as replication, deletion, and verification, as instructed by the NameNode. The DataNode reports the list of blocks it has to the NameNode periodically. The DataNode also sends heartbeats to the NameNode to indicate its status and availability.

## HDFS Data Flow

HDFS stores files as a sequence of fixed-size blocks (typically 128 MB) that are distributed across the DataNodes. Each block is replicated a number of times (default is 3) for fault tolerance. The replication factor and the block size can be configured per file or per directory.

The data flow in HDFS involves the following steps:

- **Write**: When a client wants to write a file to HDFS, it first contacts the NameNode and requests a new file. The NameNode checks the permissions and the availability of the namespace, and returns a list of DataNodes that can store the first block of the file. The client then writes the data to the first DataNode, which in turn replicates it to the next DataNode in the pipeline, and so on. The client repeats this process for the subsequent blocks of the file, until the file is complete. The client then notifies the NameNode that the file is closed.
- **Read**: When a client wants to read a file from HDFS, it first contacts the NameNode and requests the locations of the blocks that make up the file. The NameNode returns a list of DataNodes that have the replicas of each block. The client then contacts the closest DataNode and reads the data from it. The client repeats this process for the subsequent blocks of the file, until the file is read.

## HDFS Commands

HDFS provides a set of commands that can be used to interact with the file system from the command line. Some of the common commands are:

- **hdfs dfs -ls**: List the files and directories in a given path.
- **hdfs dfs -mkdir**: Create a new directory in a given path.
- **hdfs dfs -put**: Copy a local file to HDFS.
- **hdfs dfs -get**: Copy a file from HDFS to the local file system.
- **hdfs dfs -cat**: Display the contents of a file in HDFS.
- **hdfs dfs -rm**: Delete a file or a directory in HDFS.
- **hdfs dfs -cp**: Copy a file or a directory from one HDFS location to another.
- **hdfs dfs -mv**: Move a file or a directory from one HDFS location to another.
- **hdfs dfs -du**: Display the