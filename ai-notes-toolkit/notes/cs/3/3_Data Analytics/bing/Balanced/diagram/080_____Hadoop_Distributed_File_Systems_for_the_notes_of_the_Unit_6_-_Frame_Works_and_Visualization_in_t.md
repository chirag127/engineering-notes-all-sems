### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is a distributed file system that provides high-performance access to data across highly scalable Hadoop clusters   .
- HDFS is one of the core components of Apache Hadoop, along with MapReduce and YARN .
- HDFS splits files into large blocks (typically 64 MB or 128 MB) and distributes them across nodes in a cluster .
- HDFS employs a master/slave architecture, where one node (called the NameNode) manages the file system namespace and metadata, and the other nodes (called the DataNodes) store the actual data in the local disks  .
- HDFS provides fault tolerance and reliability by replicating the blocks across multiple DataNodes, and by periodically checking the health and status of the nodes  .
- HDFS supports a write-once-read-many model, where files are written by a single client and then read by multiple clients.
- HDFS provides a command-line interface and a Java API for interacting with the file system, as well as a web-based browser.
- HDFS is designed to handle large data sets running on commodity hardware, and to scale up to thousands of nodes and petabytes of data .