### The Hadoop Distributed File System

- The Hadoop Distributed File System (HDFS) is the primary data storage system used by Hadoop applications.
- HDFS is a distributed file system that provides high-throughput access to large data sets across highly scalable Hadoop clusters   .
- HDFS is designed to run on commodity hardware and handle hardware failures gracefully .
- HDFS employs a NameNode and DataNode architecture to implement the file system .
  - The NameNode is the master node that manages the file system namespace and regulates access to files by clients.
  - The DataNodes are the worker nodes that store and retrieve data blocks from local disks as instructed by the NameNode.
- HDFS splits files into large blocks (typically 128 MB or 256 MB) and distributes them across the DataNodes in the cluster  .
- HDFS maintains multiple replicas of each block (usually three) for fault tolerance and load balancing  .
- HDFS supports a write-once-read-many access model for files.
  - A file once created, written, and closed need not be changed.
  - This assumption simplifies data coherency issues and enables high throughput data access.
- HDFS is tightly coupled with the MapReduce framework, which is a programming model for parallel processing of large data sets .
  - MapReduce jobs can read and write data from and to HDFS directly.
  - HDFS provides data locality optimization by scheduling computation tasks on the nodes where the data blocks are stored .
- HDFS also provides interfaces for applications to access the file system, such as the Java API, the WebHDFS REST API, and the Hadoop shell commands.