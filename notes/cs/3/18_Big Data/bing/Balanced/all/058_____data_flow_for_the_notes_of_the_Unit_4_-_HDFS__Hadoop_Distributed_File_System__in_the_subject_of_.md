# Data flow for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data

- HDFS is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS follows a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves).
- The NameNode is responsible for managing the namespace, the metadata, and the access control of the files and directories in HDFS.
- The DataNodes are responsible for storing the actual data blocks of the files in HDFS.
- HDFS splits a large file into fixed-size blocks (typically 128 MB or 256 MB) and distributes them across the DataNodes for parallel processing.
- HDFS replicates each block on multiple DataNodes (typically three) for fault tolerance and high availability.
- HDFS supports a write-once-read-many model, where a file can be written only once by a single writer, and then read by multiple readers.
- HDFS supports two types of data flow: write pipeline and read pipeline.

## Write pipeline

- The write pipeline is the process of writing a file to HDFS by a client application.
- The write pipeline involves the following steps:

  1. The client application contacts the NameNode and requests to create a new file in HDFS.
  2. The NameNode checks if the file already exists, and if the client has the permission to write the file.
  3. If the file does not exist and the client has the permission, the NameNode allocates a new file in the namespace, and returns a list of DataNodes to the client, where the first block of the file can be stored.
  4. The client connects to the first DataNode in the list, and starts sending the data for the first block.
  5. The first DataNode receives the data, and forwards it to the second DataNode in the list, forming a pipeline.
  6. The second DataNode receives the data, and forwards it to the third DataNode in the list, completing the pipeline.
  7. The third DataNode receives the data, and stores it locally.
  8. The DataNodes send acknowledgments back to the client, confirming the successful storage of the block.
  9. The client receives the acknowledgments, and contacts the NameNode again, requesting a new list of DataNodes for the next block of the file.
  10. The NameNode returns a new list of DataNodes to the client, where the second block of the file can be stored.
  11. The client repeats steps 4 to 10 until all the blocks of the file are written to HDFS.
  12. The client closes the file, and notifies the NameNode that the file is complete.
  13. The NameNode updates the metadata of the file, and makes it available for reading.

## Read pipeline

- The read pipeline is the process of reading a file from HDFS by a client application.
- The read pipeline involves the following steps:

  1. The client application contacts the NameNode and requests to read a file from HDFS.
  2. The NameNode checks if the file exists, and if the client has the permission to read the file.
  3. If the file exists and the client has the permission, the NameNode returns a list of DataNodes to the client, where the blocks of the file are stored.
  4. The client connects to the closest DataNode in the list, and requests the data for the first block of the file.
  5. The DataNode sends the data for the first block to the client.
  6. The client receives the data, and processes it.
  7. The client contacts the next DataNode in the list, and requests the data for the next block of the file.
  8. The DataNode sends the data for the next block to the client.
  9. The client repeats steps 6 to 8 until all the blocks of the file are read from HDFS.
  10. The client closes the file, and notifies the NameNode that the file is read.