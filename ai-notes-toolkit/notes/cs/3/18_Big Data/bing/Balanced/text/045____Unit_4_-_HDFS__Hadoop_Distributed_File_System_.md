## Unit 4 - HDFS (Hadoop Distributed File System)

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
- HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware.
- HDFS employs a NameNode and DataNode architecture to implement a distributed file system that provides high-performance access to data across highly scalable Hadoop clusters.
- HDFS has the following characteristics:
  - It supports very large files, up to petabytes in size.
  - It stores file data in blocks, typically 128 MB or 256 MB in size.
  - It replicates each block across multiple nodes for fault tolerance and load balancing.
  - It uses a master-slave model, where the NameNode is the master and the DataNodes are the slaves.
  - It provides a command-line interface and a web interface for users and administrators.
  - It supports various file formats, such as text, binary, sequence, and compressed.
  - It supports various data access methods, such as batch, interactive, streaming, and real-time.