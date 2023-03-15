#### Write operations in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed and scalable file system that stores large amounts of data across multiple nodes in a cluster.
- To write data in HDFS, the client follows these steps:
  - The client contacts the NameNode and requests permission to create a new file in a given directory. The NameNode checks if the file already exists and if the client has the write access to the directory. If yes, the NameNode grants the permission and returns a list of DataNodes that can store the file blocks.  
  - The client splits the data into fixed-size blocks (default size is 128 MB) and writes them to a local buffer. The client also computes the checksum for each block and appends it to the block.  
  - The client creates a pipeline of DataNodes to write the first block. The pipeline size is determined by the replication factor of the file (default is 3). The client sends the block and its checksum to the first DataNode in the pipeline.  
  - The first DataNode stores the block and its checksum in its local disk and forwards them to the second DataNode in the pipeline. The second DataNode does the same and forwards them to the third DataNode. The process continues until the last DataNode in the pipeline receives the block and its checksum.  
  - The last DataNode sends an acknowledgement (ACK) to the previous DataNode, which sends an ACK to its previous DataNode, and so on until the first DataNode sends an ACK to the client. The client then verifies that the block has been successfully written to all the DataNodes in the pipeline.  
  - The client repeats the steps 3 to 5 for the remaining blocks of the file. The client can choose different DataNodes for each block to achieve load balancing and fault tolerance.  
  - The client notifies the NameNode that the file write operation is complete. The NameNode updates its metadata and makes the file available for read.  

- The advantages of write operations in HDFS are:
  - High throughput: The data is written in parallel to multiple DataNodes, which increases the write speed and reduces the network congestion. 
  - High reliability: The data is replicated to multiple DataNodes, which ensures the data availability and durability in case of node failures. 
  - High scalability: The data is distributed across multiple nodes, which allows the system to handle large volumes of data and to add more nodes as needed. 

- The disadvantages of write operations in HDFS are:
  - High latency: The data is written to multiple DataNodes, which involves multiple network hops and disk I/O operations, which increase the write latency. 
  - Write-once-read-many: The data is immutable once written to HDFS, which means the client cannot modify or append to the existing file. The client has to create a new file or overwrite the existing file to update the data.  
  - No random access: The data is stored in fixed-size blocks, which means the client cannot access a specific byte or record within a block. The client has to read the entire block to access the data.