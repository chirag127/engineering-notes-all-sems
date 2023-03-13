

#### How Does HDFS Store

HDFS (Hadoop Distributed File System) is a distributed, scalable, and fault-tolerant file system built on top of the Hadoop framework. It is designed to store large amounts of data reliably and efficiently. HDFS stores data across multiple machines, allowing for high throughput and fast access to data.

HDFS is a distributed file system, meaning that data is stored on multiple machines and not just one. This allows for high throughput and fast access to data. Data is stored in blocks, which are typically 64MB in size. Each block is stored on a different machine, and each block is replicated multiple times for fault tolerance.

HDFS is designed for large-scale data storage and processing. HDFS is optimized for streaming data access, meaning that it is designed to read and write large files quickly. HDFS also supports the ability to append data to existing files, making it ideal for logging applications.

HDFS also supports high availability and fault tolerance. If a machine fails, the data stored on that machine can be recovered from the replicas stored on other machines. This ensures that the data remains available and accessible, even in the event of a machine failure.

Mnemonics and Learning Tricks: 

- Hadoop Distributed File System: HDFS
- Blocks for Data Storage: BFS