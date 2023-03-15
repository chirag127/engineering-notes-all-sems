#### Write operations in HDFS

- To write data in HDFS, the client first interacts with the NameNode to get permission to write data and to get IPs of DataNodes where the client writes the data  .
- The client then directly interacts with the DataNodes for writing data  .
- The client initiates write operation by calling `create()` method of DistributedFileSystem object which creates a new file .
- The NameNode performs various checks such as the file name, permissions, disk space, etc. and returns a list of suitable DataNodes to the client  .
- The client then writes data to the first DataNode in the list, which in turn replicates the data to the next DataNode in the list, and so on  .
- The data is written in blocks of fixed size (default 64 MB) and each block is replicated across multiple DataNodes (default 3) for fault tolerance   .
- The client receives an acknowledgment from the DataNodes after the data is written and replicated  .
- The client then communicates with the NameNode to signal the completion of the file write operation  .

A sample code to write a file to HDFS in Java is as follows:

```java
FileSystem fileSystem = FileSystem.get(conf); // Get the HDFS file system object
// Check if the file already exists
Path path = new Path("/path/to/file.ext");
if (fileSystem.exists(path)) {
  System.out.println("File already exists");
  return;
}
// Create a new file and open an output stream
FSDataOutputStream outputStream = fileSystem.create(path);
// Write data to the file
outputStream.writeBytes("Hello, world!");
// Close the output stream
outputStream.close();
```

A possible mnemonic to remember the steps of write operation in HDFS is:

**C**reate a new file
**N**ameNode checks and returns DataNodes
**W**rite data to the first DataNode
**R**eplicate data to the next DataNodes
**A**cknowledge the data write
**C**omplete the file write
