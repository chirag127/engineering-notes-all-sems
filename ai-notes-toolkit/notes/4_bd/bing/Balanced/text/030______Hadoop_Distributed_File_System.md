#### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is a distributed file system that provides high-throughput access to large data sets across scalable clusters of nodes.
- HDFS is the primary data storage system used by Hadoop applications and is one of the core components of the Apache Hadoop ecosystem, along with MapReduce and YARN.
- HDFS employs a master-slave architecture, where one node acts as the NameNode and manages the file system namespace and metadata, while the other nodes act as DataNodes and store the actual data in blocks.
- HDFS splits files into large blocks (typically 64 MB or 128 MB) and distributes them across the DataNodes in the cluster. The NameNode maintains the mapping of blocks to DataNodes and also replicates the blocks for fault tolerance and load balancing.
- HDFS supports a write-once-read-many model, where files are written by a single client and then read by multiple clients. HDFS also supports appending data to existing files, but not random writes or updates.
- HDFS is designed to run on commodity hardware and handle hardware failures gracefully. It can scale to thousands of nodes and store petabytes of data. HDFS also provides interfaces for applications to access the data, such as Java API, WebHDFS, NFS and Fuse.