#### HDFS concepts

HDFS stands for Hadoop Distributed File System. It is a distributed file system that runs on a cluster of commodity hardware (low-cost machines) and provides high-throughput access to large data sets. HDFS is one of the core components of Apache Hadoop, along with MapReduce and YARN.

Some of the key concepts of HDFS are:

- **Blocks**: HDFS stores files as a sequence of fixed-size blocks, usually 128 MB or 256 MB. Each block is replicated across multiple data nodes (usually three) for fault tolerance. The block size and replication factor are configurable per file or per cluster.
- **NameNode**: The NameNode is the master node of HDFS. It maintains the metadata of the file system, such as the file names, directories, permissions, and locations of blocks. The NameNode also coordinates the read and write operations from clients and manages the replication and recovery of blocks. There is only one active NameNode in a cluster, and optionally one or more standby NameNodes for high availability.
- **DataNode**: The DataNode is the worker node of HDFS. It stores and serves the blocks of files to clients and other DataNodes. It also performs periodic block reports and heartbeats to the NameNode to indicate its health and availability. There can be hundreds or thousands of DataNodes in a cluster, depending on the scale and configuration.
- **Client**: The client is the application or user that interacts with HDFS. The client can perform operations such as creating, reading, writing, appending, deleting, or renaming files and directories. The client communicates with the NameNode to get the metadata of the file system and with the DataNodes to read or write the blocks of files.
- **Rack Awareness**: HDFS is rack-aware, meaning that it considers the physical location of the DataNodes in a cluster when placing or replicating blocks. HDFS tries to minimize the network bandwidth consumption by placing blocks on the same or nearby racks as much as possible. This also improves the reliability and performance of the file system.

A possible mnemonic to remember these concepts is:

**B**ig **N**erds **D**o **C**ool **R**esearch

where B stands for Blocks, N for NameNode, D for DataNode, C for Client, and R for Rack Awareness.