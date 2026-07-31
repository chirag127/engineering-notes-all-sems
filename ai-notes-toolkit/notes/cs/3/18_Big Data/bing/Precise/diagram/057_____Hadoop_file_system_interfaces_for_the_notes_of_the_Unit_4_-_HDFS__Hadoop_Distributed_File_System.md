### Hadoop file system interfaces

Hadoop provides a variety of file system interfaces that can be implemented concretely. The Java abstract class `org.apache.hadoop.fs.FileSystem` represents a file system in Hadoop. Hadoop uses the URI scheme to choose the appropriate file system instance to communicate with .

- Hadoop is capable of running various file systems, and HDFS is just one single implementation .
- Most Hadoop file system interactions are mediated through the Java API .
- Hadoop provides a command interface to interact with HDFS .
- The built-in servers of namenode and datanode help users to easily check the status of the cluster .
- HDFS is a distributed file system designed to run on commodity hardware and is highly fault-tolerant .
- The `org.apache.hadoop.fs.FileSystem` class implements several interfaces, including `Closeable`, `AutoCloseable`, `Configurable`, `org.apache.hadoop.fs.PathCapabilities`, and `org.apache.hadoop.security.token.DelegationTokenIssuer` .
- There are several direct known subclasses of `org.apache.hadoop.fs.FileSystem`, including `AdlFileSystem`, `FilterFileSystem`, `FTPFileSystem`, `NativeAzureFileSystem`, `NativeS3FileSystem`, `RawLocalFileSystem`, and `ViewFileSystem` .