# Design of HDFS

HDFS is a distributed file system that is designed to store and process very large files across clusters of commodity hardware. It is part of the Apache Hadoop ecosystem and is based on the Google File System. HDFS has the following design features and goals:

- **Fault tolerance:** HDFS can tolerate failures of nodes, disks, and network by replicating data blocks across multiple machines and providing mechanisms for detecting and recovering from faults.
- **Streaming data access:** HDFS is optimized for high-throughput data access rather than low-latency data access. It supports sequential reads and writes of large files, rather than random access of small files.
- **Scalability:** HDFS can scale to thousands of nodes and petabytes of data by distributing the file system metadata and data blocks across the cluster.
- **Simplicity:** HDFS aims to provide a simple and familiar file system interface for users and applications. It follows the POSIX semantics for file operations, such as create, read, write, delete, rename, and append, with some exceptions.
- **Portability:** HDFS can run on various platforms and hardware configurations, as long as they support the Java programming language and the Hadoop framework.