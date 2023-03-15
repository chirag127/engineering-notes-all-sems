#### HDFS concepts

- HDFS stands for Hadoop Distributed File System. It is a distributed file system that stores large-scale data across multiple nodes in a cluster.
- HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves).
- The NameNode is responsible for managing the namespace, metadata, and access control of the files and directories in HDFS. It also coordinates the replication and placement of data blocks among the DataNodes.
- The DataNodes are responsible for storing the actual data blocks of the files in HDFS. They also perform read and write operations on the data blocks as instructed by the NameNode.
- HDFS splits a file into fixed-size blocks (typically 128 MB) and distributes them across the DataNodes for storage. Each block is replicated a number of times (default is 3) for fault tolerance and availability.
- HDFS provides a high-level abstraction of the files and directories, hiding the details of the block storage and replication from the users. Users can access the files and directories in HDFS using a standard file system interface or a web browser.
- HDFS is designed to handle large-scale data (petabytes or more) with high throughput and low latency. It is optimized for batch processing and sequential access of data, rather than random access or interactive queries.
- HDFS is also designed to be resilient to failures and self-healing. It can detect and recover from node failures, network failures, disk failures, and data corruption. It can also balance the load and utilization of the cluster by moving data blocks across the DataNodes.