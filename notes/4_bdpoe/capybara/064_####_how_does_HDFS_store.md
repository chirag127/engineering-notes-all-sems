#### How Does HDFS Store?

Hadoop Distributed File System (HDFS) is a distributed file system that provides high throughput access to application data. It is designed to store and manage large amounts of data reliably and efficiently. Here are the key points to understand how HDFS stores data:

1. HDFS stores data in blocks: HDFS stores data in blocks of fixed size (default 128 MB), which are distributed across the nodes in the cluster. Each block is replicated across multiple nodes for fault tolerance.

2. HDFS uses a master-slave architecture: HDFS consists of a single NameNode that manages the file system namespace and regulates access to files by clients. It also maintains the metadata of the files such as file name, size, permissions, and block locations. The DataNodes store the actual data blocks and report to the NameNode periodically.

3. HDFS ensures data reliability: HDFS replicates each block across multiple DataNodes (default 3), which ensures that if a DataNode fails, the data is still available from other nodes. HDFS also maintains multiple copies of the metadata on different nodes to prevent metadata loss.

4. HDFS supports parallel data access: HDFS allows multiple clients to read and write data in parallel, which enables high throughput access to data. Clients can also access the same file concurrently, which allows parallel processing of large datasets.

5. HDFS supports data locality: HDFS stores data blocks on the nodes where the data is processed to minimize network traffic and improve performance. This ensures that the data is processed where it is stored, which reduces the amount of data transferred across the network.

Mnemonics and Learning Tricks:

- The acronym HDFS can be remembered as "Hadoop Distributed File System" or "Highly Dependable File Storage".
- To remember the block size, think of it as a "128 MB block party" where each block represents a partygoer.
- To remember the replication factor, think of it as "3's a charm" where each block is replicated thrice for reliability.
- To remember the master-slave architecture, think of the NameNode as the "mastermind" that controls the file system, and the DataNodes as the "slaves" that store the data.
- To remember the data locality feature, think of it as "location, location, location" where the data is stored and processed in the same location for efficiency.

Overall, understanding how HDFS stores data is essential for anyone working with big data and Hadoop ecosystem. With the above points and mnemonic tricks, one can easily remember the key concepts and features of HDFS.