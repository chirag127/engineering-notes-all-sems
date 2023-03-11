### Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system used by Hadoop to store and manage large amounts of data. It is designed to run on commodity hardware and can handle data-intensive workloads. In this unit, we will discuss the various aspects of HDFS and how it works.

#### Architecture of HDFS

HDFS has a master-slave architecture where there is a single NameNode that acts as a master and multiple DataNodes that act as slaves. The NameNode maintains the namespace and manages the file system metadata, while the DataNodes store the actual data. The clients interact with the NameNode to perform file system operations.

#### File System Operations

HDFS supports all the standard file system operations like create, read, write, delete, and rename. The clients communicate with the NameNode to perform these operations. When a file is created, the NameNode assigns a unique file ID and creates an entry in the namespace. The file is then divided into blocks and stored on the DataNodes.

#### Data Replication

HDFS uses data replication to ensure high availability and fault tolerance. By default, each block is replicated three times, and the replicas are stored on different DataNodes. This ensures that even if one or two DataNodes fail, the data can still be accessed from the remaining replicas.

#### Advantages of HDFS

- HDFS can handle large amounts of data and is designed to scale horizontally.
- It can provide high availability and fault tolerance through data replication.
- HDFS is optimized for batch processing and can handle data-intensive workloads.
- HDFS is open-source and can be easily integrated with other Hadoop tools and technologies.

#### Disadvantages of HDFS

- HDFS is not suitable for real-time processing as it has high latency.
- HDFS is not designed for small files as it has high overheads for file system metadata.
- HDFS does not support random access to files, and the entire file has to be read sequentially.

#### Applications of HDFS

HDFS is used in various industries for data-intensive workloads like:

- Log processing and analysis
- Image and video processing
- Scientific computing
- Machine learning and data mining

#### Conclusion

In this unit, we have learned about HDFS and its various aspects. HDFS is a distributed file system that can handle large amounts of data and is designed for data-intensive workloads. It provides high availability and fault tolerance through data replication and is used in various industries for processing and analyzing large amounts of data.