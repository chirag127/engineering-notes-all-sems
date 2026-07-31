### Data flow for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

- HDFS is a distributed file system that stores large data sets across multiple nodes in a cluster.
- HDFS provides high fault tolerance, scalability, and data locality for applications that process big data.
- HDFS divides the data into fixed-size blocks (default 128 MB) and distributes them across the DataNodes in the cluster.
- HDFS maintains multiple replicas (default 3) of each block for reliability and availability.
- HDFS has a master-slave architecture, where the NameNode is the master node that manages the metadata of the file system, and the DataNodes are the slave nodes that store the actual data blocks.
- HDFS supports two types of operations: read and write. The data flow for each operation is as follows:

#### Read operation
- The client contacts the NameNode and requests the location of the file to be read.
- The NameNode returns the list of DataNodes that have the replicas of the blocks of the file.
- The client chooses the closest DataNode and establishes a connection with it.
- The DataNode sends the data block to the client through a data stream.
- The client reads the data block and closes the connection with the DataNode.
- The client repeats the steps 2 to 5 for the remaining blocks of the file until the entire file is read.

#### Write operation
- The client contacts the NameNode and requests to write a file to HDFS.
- The NameNode checks if the file already exists or if the client has the permission to write the file.
- If the file does not exist and the client has the permission, the NameNode grants a write lease to the client and returns a list of DataNodes that can store the replicas of the first block of the file.
- The client splits the file into blocks and sends the first block to the first DataNode in the pipeline.
- The first DataNode stores the block and forwards it to the second DataNode in the pipeline.
- The second DataNode stores the block and forwards it to the third DataNode in the pipeline.
- The third DataNode stores the block and sends an acknowledgment to the second DataNode.
- The second DataNode sends an acknowledgment to the first DataNode.
- The first DataNode sends an acknowledgment to the client.
- The client contacts the NameNode and requests a list of DataNodes for the next block of the file.
- The client repeats the steps 4 to 10 for the remaining blocks of the file until the entire file is written.
- The client notifies the NameNode that the file write is complete.
- The NameNode commits the file creation and releases the write lease.

: https://www.linkedin.com/pulse/step-guide-data-flow-hdfs-read-operation-radhika-k
: https://data-flair.training/blogs/hadoop-hdfs-tutorial/
: https://www.ibm.com/topics/hdfs
: https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html
: https://www.spiceworks.com/tech/big-data/articles/hadoop-distributed-file-system-hdfs/