
#### How does HDFS store?

1. HDFS stores data across multiple nodes in a distributed environment. 
2. Each node contains a block of data, and the blocks are stored in a redundant fashion to ensure that data remains available even if a node fails. 
3. HDFS is designed to work with large files, and it is optimized for streaming reads of large files. 
4. HDFS is designed to be fault tolerant, meaning that it can continue to operate even if some of its nodes fail. 
5. HDFS also supports replication of data, so that multiple copies of the same data can be stored in different nodes. This ensures that the data remains available even if some of the nodes fail.