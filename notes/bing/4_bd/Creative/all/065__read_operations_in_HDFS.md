#### Read operations in HDFS

- To read a file from HDFS, a client needs to interact with the NameNode, which stores the metadata about the file location, size, block IDs, and DataNodes that store the blocks.
- The NameNode returns a list of DataNodes that have a copy of the file blocks, along with a token that authorizes the client to access the data.
- The client then contacts one of the DataNodes (preferably the closest one) and requests to read the file blocks.
- The DataNode sends the data to the client in a streaming fashion, using a TCP connection.
- The client can read the data from multiple DataNodes in parallel, to improve the performance and reliability of the read operation.
- If the client encounters any error or failure while reading from a DataNode, it can switch to another DataNode that has the same block and resume the read operation.
- The client periodically sends a heartbeat to the NameNode, to indicate that it is still reading the file and to renew the token.
- The client also verifies the checksum of the data received from the DataNode, to ensure the data integrity and quality.
- The read operation is completed when the client has read all the blocks of the file from the DataNodes.

A sample code to read a file from HDFS using Java API is as follows:

```java
// Create a configuration object and get a handle to the filesystem
Configuration conf = new Configuration();
FileSystem fileSystem = FileSystem.get(conf);

// Create a path object for the file to be read
Path path = new Path("/path/to/file.ext");

// Check if the file exists
if (!fileSystem.exists(path)) {
  System.out.println("File does not exist");
  return;
}

// Create an input stream to read the file
FSDataInputStream in = fileSystem.open(path);

// Read the file content and display it on the console
String line = in.readLine();
while (line != null) {
  System.out.println(line);
  line = in.readLine();
}

// Close the input stream and the filesystem
in.close();
fileSystem.close();
```

Some mnemonics and learning tricks for the read operations in HDFS are:

- Remember the acronym **NDRD**: NameNode, DataNode, Read, Data. This is the sequence of steps involved in reading a file from HDFS.
- Remember the formula **R = N * B / S**: Read time = Number of blocks * Block size / Streaming rate. This is an approximation of how long it takes to read a file from HDFS, assuming no failures or errors.
- Remember the difference between **replication** and **replica**: Replication is the process of creating multiple copies of a file block on different DataNodes, while replica is one of those copies. Replication improves the availability and reliability of the data, while replica provides the actual data to the client.