#### Java interfaces to HDFS

- HDFS is the Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing.
- HDFS can be accessed and manipulated through various interfaces, such as command-line, web, REST, and Java.
- The Java interface of HDFS is based on the abstract FileSystem class, which defines the common operations for all file systems, such as create, delete, rename, copy, etc.
- HDFS provides a concrete implementation of the FileSystem class, called DistributedFileSystem, which extends the FileSystem class and implements the specific operations for HDFS, such as replication, block management, etc.
- To use the Java interface of HDFS, one needs to import the org.apache.hadoop.fs package, which contains the FileSystem and DistributedFileSystem classes, as well as other classes and interfaces related to HDFS.
- To create a FileSystem object, one can use the static get() method of the FileSystem class, which takes a Configuration object as a parameter. The Configuration object contains the HDFS configuration settings, such as the name node address, the default block size, the replication factor, etc.
- The FileSystem object can then be used to perform various operations on HDFS, such as creating, reading, writing, deleting, or listing files and directories. For example, to create a file in HDFS, one can use the create() method of the FileSystem object, which takes a Path object as a parameter. The Path object represents the HDFS file or directory name.
- To read or write data from or to a file in HDFS, one can use the FSDataInputStream or FSDataOutputStream classes, which are subclasses of the java.io.DataInputStream and java.io.DataOutputStream classes, respectively. These classes provide methods for reading and writing primitive data types, such as int, long, byte, etc.
- To close a FileSystem object, one can use the close() method of the FileSystem class, which releases the resources associated with the object.

Here is an example of a Java program that creates a file in HDFS and writes some data to it:

```java
// Import the HDFS classes
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FSDataOutputStream;

// Create a configuration object
Configuration conf = new Configuration();

// Set the HDFS name node address
conf.set("fs.defaultFS", "hdfs://namenode:8020");

// Create a file system object
FileSystem fs = FileSystem.get(conf);

// Create a path object for the file to be created
Path path = new Path("/user/hadoop/test.txt");

// Create a file in HDFS
FSDataOutputStream out = fs.create(path);

// Write some data to the file
out.writeInt(42);
out.writeUTF("Hello, HDFS!");

// Close the file and the file system
out.close();
fs.close();
```