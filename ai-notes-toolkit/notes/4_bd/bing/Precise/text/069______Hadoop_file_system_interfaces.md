#### Hadoop file system interfaces

- Hadoop has a variety of file systems that can be implemented concretely.
- The Java abstract class `org.apache.hadoop.fs.FileSystem` represents a file system in Hadoop.
- Hadoop provides numerous interfaces to its various filesystems, and it generally uses the URI scheme to choose the right filesystem instance to communicate with.
- Hadoop is capable of running various file systems and HDFS is just one single implementation.
- Hadoop provides a command interface to interact with HDFS.
- The built-in servers of namenode and datanode help users to easily check the status of the cluster.
- Hadoop is written in Java, so most Hadoop filesystem interactions are mediated through the Java API.
- The `org.apache.hadoop.fs.FileSystem` class implements several interfaces, including `Closeable`, `AutoCloseable`, `Configurable`, `org.apache.hadoop.fs.PathCapabilities`, and `org.apache.hadoop.security.token.DelegationTokenIssuer`.
- There are several direct known subclasses of `org.apache.hadoop.fs.FileSystem`, including `AdlFileSystem`, `FilterFileSystem`, `FTPFileSystem`, `NativeAzureFileSystem`, `NativeS3FileSystem`, `RawLocalFileSystem`, and `ViewFileSystem`.