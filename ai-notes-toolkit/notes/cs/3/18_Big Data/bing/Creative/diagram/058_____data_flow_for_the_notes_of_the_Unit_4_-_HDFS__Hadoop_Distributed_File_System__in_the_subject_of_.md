### Data flow for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

- HDFS is a distributed file system that stores large data sets across multiple nodes in a cluster.
- HDFS provides high fault tolerance, scalability, and throughput by splitting the data into fixed-size blocks (typically 128 MB) and replicating them across different DataNodes .
- HDFS follows a master-slave architecture, where a single NameNode manages the metadata of the file system, such as the location, size, and replication factor of each block, and multiple DataNodes store the actual blocks of data.
- HDFS supports two types of operations: read and write. In both cases, the client interacts with the NameNode to get the metadata information and then directly communicates with the DataNodes to perform the data transfer.
- The data flow for the read operation is as follows:
  - The client requests the NameNode for the list of DataNodes that have the replicas of the blocks of the file to be read.
  - The NameNode returns the list of DataNodes in a sorted order based on the proximity to the client.
  - The client contacts the closest DataNode and establishes a data stream to read the block.
  - The client reads the block from the DataNode and verifies the checksum. If there is a checksum mismatch or an error, the client contacts the next DataNode in the list and repeats the process until the block is read successfully or the list is exhausted.
  - The client repeats the above steps for each block of the file until the entire file is read.
- The data flow for the write operation is as follows:
  - The client requests the NameNode for a new file name and the list of DataNodes to store the replicas of the first block of the file.
  - The NameNode checks if the file name already exists and if the client has the permission to write. If both conditions are satisfied, the NameNode allocates a new file name and returns the list of DataNodes to the client.
  - The client splits the data into blocks and sends the first block to the closest DataNode in the list. The DataNode stores the block and forwards it to the next DataNode in the list. This process continues until all the replicas of the block are stored.
  - The DataNodes send acknowledgments to the client after storing the block. The client verifies the acknowledgments and reports any errors to the NameNode.
  - The client repeats the above steps for each block of the file until the entire file is written.
  - The client tells the NameNode that the file write is complete. The NameNode marks the file as closed.