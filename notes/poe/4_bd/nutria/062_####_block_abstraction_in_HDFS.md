
#### Block Abstraction in HDFS

- HDFS (Hadoop Distributed File System) is a distributed, highly fault-tolerant file system designed to run on commodity hardware. 
- It provides high throughput access to application data and is suitable for applications that have large data sets. 
- HDFS is designed to be highly fault-tolerant and to use low-cost hardware. 
- HDFS has a master/slave architecture where the master is called the NameNode and the slaves are called DataNodes. 
- The NameNode is responsible for managing the filesystem namespace and regulating access to files by clients. 
- The DataNodes are responsible for serving read and write requests from the file system’s clients. 
- Data is stored in blocks, and each block is replicated across multiple DataNodes for redundancy and reliability. 
- The block abstraction in HDFS is the mechanism by which HDFS stores data. 
- Blocks are the smallest unit of data that can be stored in HDFS. 
- Blocks are typically 64 MB in size, but this can be configured. 
- Blocks are stored in a distributed fashion across multiple DataNodes, and each block is replicated to ensure reliability and fault-tolerance. 
- Blocks are stored on DataNodes in a “write-once, read-many” fashion, meaning that once a block is written, it cannot be modified or deleted. 
- Blocks are identified by a unique block ID, and the block ID is stored in the NameNode. 
- When a client requests a file, the NameNode will provide a list of block IDs that make up the file. 
- The client will then request each block from the DataNodes, which will return the block’s data. 
- The client will then assemble the blocks into a complete file. 
- The block abstraction in HDFS is a key component of the file system, as it enables HDFS to store data reliably and efficiently.