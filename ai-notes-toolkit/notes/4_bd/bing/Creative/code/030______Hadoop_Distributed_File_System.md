#### Hadoop Distributed File System

The Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is fault-tolerant and provides high throughput access to the data stored. HDFS stores large files across multiple machines and replicates them to ensure reliability. HDFS consists of two types of nodes: a NameNode and multiple DataNodes. The NameNode is the master server that manages the file system namespace and the metadata of the files and directories. The DataNodes are the workers that store the actual data blocks of the files.

To write code for HDFS, you need to use the Hadoop API, which provides classes and methods for interacting with the file system. For example, you can use the FileSystem class to create, delete, rename, or copy files and directories. You can also use the FileStatus class to get information about the files and directories, such as the size, modification time, replication factor, etc. You can also use the FSDataInputStream and FSDataOutputStream classes to read and write data from and to the files.

Here is a code example in Java that creates a file in HDFS and writes some text to it:

```java
// Import the Hadoop API classes
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FSDataOutputStream;

// Create a configuration object and set the HDFS URI
Configuration conf = new Configuration();
conf.set("fs.defaultFS", "hdfs://namenode:9000");

// Get a FileSystem object from the configuration
FileSystem fs = FileSystem.get(conf);

// Create a Path object for the file to be created
Path file = new Path("/user/hadoop/test.txt");

// Create a FSDataOutputStream object to write to the file
FSDataOutputStream out = fs.create(file);

// Write some text to the file
out.writeUTF("Hello, HDFS!");

// Close the output stream
out.close();

// Close the file system
fs.close();
```