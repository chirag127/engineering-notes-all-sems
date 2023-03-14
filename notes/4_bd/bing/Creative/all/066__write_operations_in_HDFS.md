#### Write operations in HDFS

- HDFS stands for Hadoop Distributed File System, which is the storage layer of Hadoop. It follows the write-once-read-many model, which means that files in HDFS cannot be edited, but only appended with new data.
- To write a file in HDFS, a client needs to interact with the master node, called the NameNode, which manages the namespace and the metadata of the file system. The NameNode provides the client with the addresses of the slave nodes, called the DataNodes, where the client can write the data blocks of the file.
- The client then directly writes data to the DataNodes, which create a data write pipeline to replicate the blocks to other DataNodes, according to the replication factor (default is 3). The replication factor determines how many copies of each block are stored in the cluster, for fault tolerance and availability.
- The data write pipeline works as follows: The client writes the first block of the file to the first DataNode in the pipeline. The first DataNode then forwards the block to the second DataNode in the pipeline, while the client writes the next block to the first DataNode. The second DataNode, in turn, forwards the block to the third DataNode in the pipeline, and so on. This way, the DataNodes can read and write data blocks simultaneously, without waiting for the client to finish writing the whole file.
- Once the last DataNode in the pipeline receives the block, it sends an acknowledgment back to the previous DataNode, which then sends an acknowledgment to the previous one, and so on, until the first DataNode sends an acknowledgment to the client. Only then, the write operation for that block is considered successful, and the client proceeds to write the next block in the same manner.
- After the client finishes writing the file, it notifies the NameNode, which finalizes the file creation and records the file locations in the metadata. The NameNode also periodically receives block reports from the DataNodes, which contain the list of blocks that each DataNode is responsible for. The NameNode uses these reports to monitor the health and the capacity of the cluster, and to balance the load and the replication of the blocks.

- A sample code to write a file to HDFS in Java is as follows:

```java
FileSystem fileSystem = FileSystem.get (conf); // Get the HDFS file system object
// Check if the file already exists
Path path = new Path (“/path/to/file.ext”);
if (fileSystem.exists (path)) {
  System.out.println(“File already exists”);
  return;
}
// Create a new file and open an output stream
FSDataOutputStream outputStream = fileSystem.create(path);
// Write some data to the file
outputStream.writeUTF(“Hello HDFS!”);
// Close the output stream
outputStream.close();
// Close the file system
fileSystem.close();
```

- A mnemonic to remember the steps of writing a file to HDFS is: **CRAWL**

  - **C**reate a FileSystem object
  - **R**equest the NameNode for permission and DataNode addresses
  - **A**ppend data blocks to the DataNodes
  - **W**ait for acknowledgments from the DataNodes
  - **L**et the NameNode finalize the file creation