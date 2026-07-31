## Unit 4 - HDFS (Hadoop Distributed File System)

Hadoop Distributed File System (HDFS) is a distributed file system that is designed to store large data sets reliably and efficiently. It is one of the core components of the Apache Hadoop ecosystem and is widely used for big data processing.

### Features of HDFS

- Scalability: HDFS is designed to be scalable to handle large data sets. It can store petabytes of data by adding more nodes to the Hadoop cluster.

- Fault-tolerance: HDFS is designed to be fault-tolerant, which means that it can recover from hardware failures, software failures, and other types of failures without losing data.

- High throughput: HDFS is optimized for streaming data access, which means that it can handle high throughput of data.

- Data locality: HDFS stores data in a distributed manner across nodes in the Hadoop cluster. It also ensures that data processing is done on the same node where the data is stored, which improves performance.

### Architecture of HDFS

HDFS architecture consists of the following components:

- NameNode: It is the central component of HDFS that stores metadata about the files and directories in the Hadoop cluster. It also manages data access and ensures data reliability.

- DataNode: It is the component that stores data in the Hadoop cluster. It communicates with the NameNode to retrieve metadata and provides data to clients.

- Secondary NameNode: It is a helper component of the NameNode that periodically takes a snapshot of the metadata and stores it in a separate location.

### File operations in HDFS

HDFS supports the following file operations:

- Write: Clients can write data to HDFS by creating a new file or appending data to an existing file.

- Read: Clients can read data from HDFS by opening a file and reading its contents.

- Delete: Clients can delete a file or a directory from HDFS.

### Advantages of HDFS

- HDFS is designed to handle large data sets, which makes it ideal for big data processing.

- HDFS is fault-tolerant, which means that it can recover from failures without losing data.

- HDFS provides high throughput of data, which makes it suitable for streaming data access.

- HDFS provides data locality, which improves performance by processing data on the same node where it is stored.

- HDFS is open-source software, which means that it is free to use and can be customized according to the user's needs.

### Limitations of HDFS

- HDFS is not suitable for storing small files because it has high overheads for small files.

- HDFS is not suitable for real-time data processing because it has high latency for data access.

- HDFS does not support multiple writers for a file, which means that only one client can write to a file at a time.

- HDFS does not provide strong consistency guarantees, which means that the data may not be consistent across all nodes in the Hadoop cluster at all times.

### Conclusion

HDFS is a distributed file system that is designed for storing large data sets reliably and efficiently. It is an important component of the Apache Hadoop ecosystem and is widely used for big data processing. HDFS provides scalability, fault-tolerance, high throughput, and data locality, making it suitable for handling big data. However, it has limitations such as high overheads for small files, high latency for data access, and lack of strong consistency guarantees.