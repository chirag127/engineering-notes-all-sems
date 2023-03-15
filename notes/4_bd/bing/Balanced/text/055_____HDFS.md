### HDFS

- HDFS stands for Hadoop Distributed File System. It is a distributed file system that handles large data sets running on commodity hardware .
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN. Hadoop is an open source framework for processing and storing big data.
- HDFS operates by rapidly transferring data between nodes in a cluster. It is fault-tolerant and designed to be deployed on low-cost, commodity hardware .
- HDFS has a master-slave architecture, where one node acts as the NameNode (master) and the others act as DataNodes (slaves). The NameNode manages the file system namespace and the metadata, while the DataNodes store the actual data in blocks.
- HDFS provides a command-line interface and a web interface for users to interact with the file system. It also supports a Java API for application development.
- HDFS is suitable for applications that have large data sets, sequential access patterns, and high throughput requirements. It is not suitable for applications that need low latency, random access, or multiple writers.