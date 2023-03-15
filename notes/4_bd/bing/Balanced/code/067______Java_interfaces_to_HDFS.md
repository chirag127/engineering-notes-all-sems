HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing. HDFS provides Java interfaces for applications to interact with the file system. Here is some code to illustrate how to use the Java interfaces to HDFS:

#### Java interfaces to HDFS

```java
// Import the necessary classes
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;

// Create a configuration object and set the HDFS URI
Configuration conf = new Configuration();
conf.set("fs.defaultFS", "hdfs://namenode:8020");

// Get a FileSystem instance
FileSystem fs = FileSystem.get(conf);

// Create a Path object for the file to read or write
Path file = new Path("/path/to/file.txt");

// Check if the file exists
if (fs.exists(file)) {
  System.out.println("File exists");
} else {
  System.out.println("File does not exist");
}

// Read data from the file using FSDataInputStream
FSDataInputStream in = fs.open(file);
byte[] buffer = new byte[1024];
int bytesRead = in.read(buffer);
// Process the data in the buffer
in.close();

// Write data to the file using FSDataOutputStream
FSDataOutputStream out = fs.create(file);
byte[] data = "Hello, HDFS!".getBytes();
out.write(data);
out.close();

// Query the file system for some information
long fileSize = fs.getFileStatus(file).getLen();
System.out.println("File size: " + fileSize);
boolean isDirectory = fs.isDirectory(file);
System.out.println("Is directory: " + isDirectory);

// Close the FileSystem
fs.close();
```