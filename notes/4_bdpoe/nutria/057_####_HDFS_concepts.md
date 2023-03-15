
#### HDFS Concepts

* HDFS stands for Hadoop Distributed File System. It is a distributed, scalable, and fault-tolerant file system that runs on commodity hardware and is used for storing large amounts of data. 
* HDFS is designed to store very large files (typically in the range of gigabytes to terabytes) across multiple machines. 
* It is designed to be reliable, with automatic failover and data replication. 
* HDFS is composed of two main components: the NameNode and the DataNode. The NameNode is the master node that stores the file system metadata, such as the file names, block locations, and other attributes. The DataNodes are the slave nodes that store the actual data blocks. 
* HDFS is designed to be highly fault-tolerant, meaning that it can handle hardware and software failures without any data loss. This is achieved by replicating the data blocks across multiple nodes. 
* HDFS also provides high availability, meaning that it can be accessed from multiple nodes at the same time. This is achieved by using the NameNode and DataNodes. 
* HDFS is optimized for streaming data access, meaning that it can efficiently read and write large files. It is not optimized for random access, meaning that it is not suitable for applications that require frequent random reads and writes. 
* HDFS is commonly used for Big Data applications, such as data mining, machine learning, and analytics. 
* Mnemonic: HDFS stands for Hadoop Distributed File System.