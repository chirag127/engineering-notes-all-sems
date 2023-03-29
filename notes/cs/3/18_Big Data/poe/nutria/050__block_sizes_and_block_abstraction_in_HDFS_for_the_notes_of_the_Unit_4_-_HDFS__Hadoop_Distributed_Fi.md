
### Block Sizes and Block Abstraction in HDFS

* Hadoop Distributed File System (HDFS) is a distributed file system that stores data across multiple nodes in a Hadoop cluster.
* HDFS uses a block abstraction to store data. Each file is divided into blocks, with each block having a size of 128MB by default. 
* Blocks are stored on different nodes in the cluster, allowing for parallel processing of data.
* HDFS also uses a block abstraction to provide fault tolerance. When a block is written to the HDFS, multiple replicas of the block are created and stored on different nodes. This ensures that the data is still available even if one of the nodes fails.
* HDFS also provides data locality, meaning that data is stored on the node that is closest to the node that needs to process it. This reduces the amount of time needed to process the data.
* HDFS also provides access control, allowing users to specify which users and groups can access the data stored in HDFS.