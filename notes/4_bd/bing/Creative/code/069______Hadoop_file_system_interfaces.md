#### Hadoop file system interfaces

Hadoop file system interfaces are the Java abstract classes and interfaces that define the client API to interact with various file systems in Hadoop. The main interface is org.apache.hadoop.fs.FileSystem, which represents a generic file system that can be implemented by different concrete classes. Some of the common implementations are:

- org.apache.hadoop.fs.LocalFileSystem: This class represents the local file system of the machine where Hadoop is running. It can be accessed using the URI scheme file://.
- org.apache.hadoop.hdfs.DistributedFileSystem: This class represents the Hadoop Distributed File System (HDFS), which is the default file system for Hadoop clusters. It can be accessed using the URI scheme hdfs://.
- org.apache.hadoop.fs.s3a.S3AFileSystem: This class represents the Amazon Simple Storage Service (S3) file system, which can be used to store and access data in the cloud. It can be accessed using the URI scheme s3a://.
- org.apache.hadoop.fs.ftp.FTPFileSystem: This class represents the File Transfer Protocol (FTP) file system, which can be used to transfer files between different machines. It can be accessed using the URI scheme ftp://.

To use a file system interface, one needs to create an instance of the corresponding class and configure it with the appropriate parameters. For example, to create an instance of the HDFS file system, one can use the following code:

```java
// Import the required classes
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

// Create a configuration object
Configuration conf = new Configuration();

// Set the HDFS URI
conf.set("fs.defaultFS", "hdfs://namenode:8020");

// Create a file system object
FileSystem fs = FileSystem.get(conf);

// Perform file system operations
fs.mkdirs(new Path("/user/hadoop"));
fs.copyFromLocalFile(new Path("/home/hadoop/input.txt"), new Path("/user/hadoop/input.txt"));
fs.delete(new Path("/user/hadoop/output"), true);
```

The file system interface provides various methods to perform common file system operations, such as creating, deleting, renaming, copying, moving, listing, and reading files and directories. Some of the methods are:

- boolean exists(Path f): Checks if the given path exists in the file system.
- boolean mkdirs(Path f): Creates the given directory and all the necessary parent directories.
- boolean delete(Path f, boolean recursive): Deletes the given path, and if recursive is true, deletes all the subdirectories and files as well.
- void copyFromLocalFile(Path src, Path dst): Copies a file from the local file system to the Hadoop file system.
- void copyToLocalFile(Path src, Path dst): Copies a file from the Hadoop file system to the local file system.
- void rename(Path src, Path dst): Renames the given path to a new path.
- FileStatus[] listStatus(Path f): Returns an array of FileStatus objects representing the files and directories under the given path.
- FSDataInputStream open(Path f): Returns an input stream to read the contents of the given file.
- FSDataOutputStream create(Path f): Returns an output stream to write the contents to the given file.

The file system interface also supports the concept of working directory, which is the default directory for relative paths. One can get and set the working directory using the following methods:

- Path getWorkingDirectory(): Returns the current working directory of the file system.
- void setWorkingDirectory(Path new_dir): Sets the current working directory of the file system to the given path.