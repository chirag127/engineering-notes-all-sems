### Java interfaces to HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It provides high-throughput access to application data and is suitable for applications that have large data sets. HDFS is one of the core components of the Hadoop ecosystem.

Most Hadoop filesystem interactions are mediated through the Java API. The filesystem shell, for example, is a Java application that uses the Java FileSystem class to provide filesystem operations.

1. **The Java Interface**: The Hadoop FileSystem class is the API for interacting with one of Hadoop’s filesystems.
2. **Reading Data Using the FileSystem API**: A file in a Hadoop filesystem is represented by a Hadoop Path object.
3. **FSDataInputStream**: This is used to read data from HDFS.
4. **Writing Data**: This can be done using the FSDataOutputStream.
5. **Querying the Filesystem**: This can be done using the Java API.
6. **Examples**: There are several examples of using the Java API for HDFS.

By exposing its filesystem interface as a Java API, Hadoop makes it awkward for non-Java applications to access HDFS. However, it is still possible to interact with HDFS using the command-line interface.