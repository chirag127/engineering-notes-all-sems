
#### Block Sizes in HDFS

* HDFS (Hadoop Distributed File System) is a distributed file system designed to run on commodity hardware. 
* HDFS is designed to store very large files with streaming data access patterns, running on clusters of commodity hardware. 
* HDFS is a block-structured file system, which means that files are broken down into blocks and stored in a distributed manner across the cluster. 
* Each block is typically 64MB or 128MB in size, and can be stored on different nodes in the cluster. 
* The block size is configurable, and can be set to a different size according to the needs of the application. 
* The larger the block size, the more data can be stored in a single block, but the more overhead there is in managing the blocks. 
* The blocks are replicated across multiple nodes in the cluster, so that if one node fails, the data is still available from other nodes. 
* This replication factor is also configurable, and can be set according to the needs of the application. 
* HDFS is designed to be highly fault tolerant, and is able to recover from node and disk failures without losing data. 
* Mnemonics and learning tricks for block sizes in HDFS include: 
  * "64MB or 128MB" to remember the default block sizes. 
  * "Replication Factor" to remember the number of nodes that a block is replicated to.