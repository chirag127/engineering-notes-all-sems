 Here is the content in markdown format for the topic ## Unit 4 - HDFS (Hadoop Distributed File System):

## Unit 4 - HDFS (Hadoop Distributed File System)

- HDFS stands for Hadoop Distributed File System. It is a distributed file system designed to hold very large amounts of data (terabytes or petabytes), and provide high-throughput access to this information.
- HDFS works on the master-slave architecture. The NameNode is the master server that manages the file system namespace and regulates access to files by clients. DataNodes are slave nodes that store the blocks and serve read/write requests from the clients.
- HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware. It provides high throughput access to application data and is suitable for applications that have large data sets.
- The key benefits of HDFS are:

- Scalability - HDFS can scale to store and manage PBs of data.
- Fault Tolerance - Data is replicated across multiple DataNodes, so if a few servers fail, the data can still be accessed from other replicas.
- Streaming Access - HDFS supports streaming access of large files.
- Simple Coherency Model - HDFS assumes that the applications using the file system will be responsible for coherency between the replicas of the file. This simplifies the design of HDFS.
- Moving Computation is Cheaper than Moving Data - HDFS moves the computation to where the data is located to reduce data transfer over the network, thereby increasing performance.

- Some key points about HDFS:

- Files are split into blocks of fixed size (typically 128MB).
- Blocks are replicated for fault tolerance. The replication factor can be 3 or more.
- The NameNode keeps the file system namespace and regulates access to files by clients.
- DataNodes store the blocks and serve read/write requests from clients.
- HDFS uses the master-slave architecture.
- HDFS is suitable for streaming access of large files.
- The HDFS client library interacts with the NameNode to locate DataNodes that hold the desired data.

[Detailed diagrams and examples can be added here to explain the HDFS architecture and key concepts]

[Advantages and disadvantages of HDFS can be listed here with comparisons to other file systems]

[Applications of HDFS can be listed here with examples of companies using HDFS]