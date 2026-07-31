### HDFS

HDFS stands for Hadoop Distributed File System. It is a distributed file system that handles large data sets running on commodity hardware. It is one of the major components of Apache Hadoop, the others being MapReduce and YARN .

Some of the main features and benefits of HDFS are:

- It is fault-tolerant and can recover from hardware failures and network partitions  .
- It is scalable and can store and process petabytes of data across thousands of nodes  .
- It is optimized for high-throughput and low-latency data access  .
- It supports multiple data formats and types, such as structured, semi-structured, and unstructured data .
- It provides a simple and consistent interface for applications to interact with the data  .

Some of the main components and concepts of HDFS are:

- NameNode: The master node that manages the namespace and the metadata of the file system.
- DataNode: The worker node that stores and serves the data blocks of the files.
- Block: The smallest unit of data in HDFS, typically 64 MB or 128 MB in size.
- Replication: The mechanism of storing multiple copies of the same block on different DataNodes for fault-tolerance and load-balancing.
- Rack: A group of nodes that are physically close to each other and share a network switch.
- Client: The application or user that accesses the data in HDFS through the Hadoop API.