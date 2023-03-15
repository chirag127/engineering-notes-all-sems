### Hadoop Distributed File System

- Hadoop Distributed File System (HDFS) is a distributed file system that provides high-performance access to data across highly scalable Hadoop clusters   .
- HDFS is the primary data storage system used by Hadoop applications and is one of the core components of Apache Hadoop, along with MapReduce and YARN  .
- HDFS splits files into large blocks and distributes them across nodes in a cluster. It then transfers packaged code into nodes to process the data in parallel using the MapReduce programming model .
- HDFS has a master-slave architecture that consists of a NameNode and multiple DataNodes. The NameNode manages the file system namespace and regulates access to files by clients. The DataNodes store and retrieve blocks when they are told to by the NameNode or clients.
- HDFS is designed to handle large data sets running on commodity hardware and to tolerate hardware failures. It provides high-throughput, fault-tolerance, scalability, and data locality optimization   .