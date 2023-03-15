### Java interfaces to HDFS

- Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware.
- HDFS provides high-throughput access to application data and is suitable for applications that have large data sets.
- Most Hadoop filesystem interactions are mediated through the Java API.
- The filesystem shell, for example, is a Java application that uses the Java FileSystem class to provide filesystem operations.
- By exposing its filesystem interface as a Java API, Hadoop makes it awkward for non-Java applications to access HDFS.
- A file in a Hadoop filesystem is represented by a Hadoop Path object.
- The Hadoop FileSystem class is the API for interacting with one of Hadoop’s filesystems.
- Some examples of using the Java API for HDFS include reading data using the FileSystem API, writing data using the FSDataOutputStream, and querying the filesystem.
- The command-line interface is one of the simplest ways to interact with HDFS.
- Command-line interface has support for filesystem operations like reading the file, creating directories, moving files, deleting data, and listing directories.