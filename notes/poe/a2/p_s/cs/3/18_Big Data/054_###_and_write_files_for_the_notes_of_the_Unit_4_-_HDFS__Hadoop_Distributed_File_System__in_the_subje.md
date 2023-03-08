 Here is the content in Markdown format for the notes on topic ### HDFS (Hadoop Distributed File System) ### for Unit 4 of Big Data:

HDFS (Hadoop Distributed File System)

- HDFS is a distributed file system that stores large data sets reliably, scalably and available across clusters of commodity servers.
- It has a master-slave architecture. The Master is called NameNode and slaves are called DataNodes.
- Data is stored in blocks of 128MB size. The blocks are replicated across multiple DataNodes for fault tolerance.
- Files are split into block-sized chunks which are stored as independent units. This enables streaming access of files.
- The NameNode manages the file system namespace and regulates access to files. It maintains the file system tree and the metadata for all the files and directories.
- The DataNodes store the blocks and serve read/write requests from clients.
- The benefits of HDFS are:
-- Scalability - HDFS can handle large amounts of data (in the range of Terabytes to Petabytes). It can scale to tens of thousands of servers.
-- Fault Tolerance - Data replication provides high availability and reliability. If a DataNode fails, the replicas can serve the data.
-- Economy - HDFS is designed to be deployed on low-cost hardware, thus reducing the cost of storage.
-- Streaming Access - HDFS supports streaming access of files, enabling applications to read or write large files quickly.

Applications of HDFS:
- Used by Hadoop ecosystem for storage in Big Data processing.
- Used for storing and processing large datasets in applications like web indexing, data mining, log processing, machine learning, etc.
- Acts as a storage layer for data lakes and data hubs.

[Include diagrams and codes if required]

Advantages and Disadvantages:
[Include key advantages and disadvantages of HDFS]