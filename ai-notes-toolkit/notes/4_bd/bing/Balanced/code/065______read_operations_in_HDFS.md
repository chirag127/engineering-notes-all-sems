#### Read operations in HDFS

To read a file from HDFS, a client needs to interact with the NameNode, which stores the metadata about the file location and the DataNodes that store the file blocks. The steps involved in the read operation are as follows  :

- The client contacts the NameNode and requests the file name and the list of DataNodes that have the blocks of the file.
- The NameNode returns the list of DataNodes and a token that authorizes the client to access the file.
- The client contacts the closest DataNode and requests the first block of the file using the token.
- The DataNode sends the block to the client as a stream of bytes.
- The client reads the data from the stream and writes it to the local file system or the standard output.
- The client repeats the steps 3 to 5 for the remaining blocks of the file until the end of the file is reached.

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

// Open the file and get an input stream
FSDataInputStream in = fileSystem.open(path);

// Read the data from the stream and write it to the local file system or the standard output
int numBytes = 0;
while ((numBytes = in.read()) != -1) {
  System.out.write(numBytes);
}

// Close the input stream and the file system
in.close();
fileSystem.close();
```