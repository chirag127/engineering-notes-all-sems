#### Data flow in HDFS

HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant file system that stores large amounts of data across multiple nodes in a cluster. HDFS follows a master-slave architecture, where the master node is called the NameNode and the slave nodes are called the DataNodes. The NameNode manages the metadata of the files and directories, such as the file name, size, location, permissions, etc. The DataNodes store the actual data blocks of the files, which are replicated across multiple nodes for fault tolerance.

The data flow in HDFS involves two main operations: read and write. The following points describe how these operations are performed in HDFS.

- **Read operation**: When a client wants to read a file from HDFS, it performs the following steps:

  1. The client contacts the NameNode and requests the metadata of the file, such as the block locations, the block size, the replication factor, etc.
  2. The NameNode returns the metadata of the file to the client, along with a list of DataNodes that have the replicas of the blocks of the file.
  3. The client chooses the closest DataNode from the list and contacts it to request the data block.
  4. The DataNode sends the data block to the client over the network.
  5. The client repeats steps 3 and 4 for each block of the file until it reads the entire file.
  6. The client closes the file and notifies the NameNode.

- **Write operation**: When a client wants to write a file to HDFS, it performs the following steps:

  1. The client contacts the NameNode and requests to create a new file in the HDFS namespace, with a specified block size and replication factor.
  2. The NameNode checks if the file already exists or if the client has the permission to write the file. If not, it returns an error to the client. If yes, it allocates a new file in the namespace and returns a confirmation to the client.
  3. The client splits the file into data blocks according to the block size and sends them to the DataNodes in a pipeline fashion. The client also sends a write request to the NameNode for each block, along with the DataNode ID and the block ID.
  4. The NameNode assigns a unique block ID to each block and returns it to the client. It also chooses a list of DataNodes to store the replicas of the block, based on the replication factor and the rack awareness policy.
  5. The client sends the data block to the first DataNode in the list, which then forwards it to the next DataNode in the list, and so on, until all the replicas are stored.
  6. The DataNodes send an acknowledgment to the client after storing the block successfully.
  7. The client repeats steps 3 to 6 for each block of the file until it writes the entire file.
  8. The client closes the file and notifies the NameNode.

The following diagram illustrates the data flow in HDFS for read and write operations:

![HDFS data flow diagram](https://www.geeksforgeeks.org/wp-content/uploads/HDFS-Read-Write-Operation.png)