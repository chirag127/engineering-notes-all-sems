#### Read operations in HDFS

- To read a file from HDFS, a client needs to interact with the NameNode, which stores the metadata about the file, such as its location, size, replication factor, and block IDs.
- The client requests the NameNode for the block locations of the file. The NameNode returns a list of DataNodes that have the replicas of the blocks of the file.
- The client chooses the closest DataNode from the list and connects to it. The DataNode serves the block data to the client.
- The client reads the data from the DataNode and then moves to the next DataNode in the list until it reads the entire file.
- The client can also read the file in parallel from multiple DataNodes if the file is large and split into multiple blocks.

A sample code to read a file from HDFS using Java API is as follows:

```java
// Create a configuration object
Configuration conf = new Configuration();

// Get an instance of the FileSystem
FileSystem fileSystem = FileSystem.get(conf);

// Create a Path object for the file to be read
Path path = new Path("/path/to/file.ext");

// Check if the file exists
if (!fileSystem.exists(path)) {
  System.out.println("File does not exist");
  return;
}

// Open an input stream to read the file
FSDataInputStream in = fileSystem.open(path);

// Read the file contents and display them on the console
int numBytes = 0;
while ((numBytes = in.read()) != -1) {
  System.out.write(numBytes);
}

// Close the input stream and the file system
in.close();
fileSystem.close();
```

Some mnemonics and learning tricks for the read operations in HDFS are:

- Remember the acronym **NDRD**: NameNode, DataNode, Read, Data. This is the sequence of steps involved in reading a file from HDFS.
- Think of the NameNode as a **directory** that tells you where to find the file you want to read. The DataNodes are the **storage devices** that actually store the file data.
- Imagine the file as a **puzzle** that is split into several pieces (blocks). The NameNode gives you a **map** of where to find the pieces. You have to visit each DataNode and collect the pieces to complete the puzzle. You can also collect the pieces in parallel if you have more than one map.