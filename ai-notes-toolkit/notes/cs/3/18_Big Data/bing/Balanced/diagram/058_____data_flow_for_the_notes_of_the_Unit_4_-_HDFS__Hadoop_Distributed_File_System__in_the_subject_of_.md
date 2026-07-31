### Data flow for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

- HDFS is a distributed file system that stores large data sets across multiple nodes in a cluster.
- HDFS provides high fault tolerance, scalability, and parallel processing of data.
- HDFS divides the data into fixed-size blocks (default 128 MB) and distributes them across the cluster.
- HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest are DataNodes (slaves).
- The NameNode manages the file system namespace, the metadata of the files and blocks, and the cluster configuration.
- The DataNodes store the actual data blocks and perform read and write operations as instructed by the NameNode.
- HDFS supports two types of data flow: read and write.
- In the read operation, the client contacts the NameNode to get the list of DataNodes that have the blocks of the file.
- The client then contacts one of the DataNodes directly and reads the data from it.
- The client can also read data from other DataNodes in parallel if the file is split into multiple blocks.
- In the write operation, the client contacts the NameNode to request permission to write a file.
- The NameNode checks if the file already exists and if the client has the right to write it.
- If the file does not exist, the NameNode allocates a new file in the namespace and returns the list of DataNodes that can store the blocks of the file.
- The client then contacts the first DataNode in the list and starts writing the data to it.
- The first DataNode replicates the data to the second DataNode in the list, and so on, forming a pipeline of DataNodes.
- The client receives an acknowledgment from the DataNodes when the write operation is complete.
- The client then informs the NameNode that the file is closed.
- The NameNode updates the file system metadata and marks the file as complete.

: https://www.linkedin.com/pulse/step-guide-data-flow-hdfs-read-operation-radhika-k
: https://data-flair.training/blogs/hadoop-hdfs-tutorial/
: https://www.ibm.com/topics/hdfs
: https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html
: https://www.spiceworks.com/tech/big-data/articles/hadoop-distributed-file-system-hdfs/