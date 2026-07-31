### Hadoop file system interfaces

- Hadoop file system interfaces are the Java classes and methods that allow applications to interact with various file systems in Hadoop, such as HDFS, S3, FTP, etc.
- The Java abstract class `org.apache.hadoop.fs.FileSystem` represents the client interface to a file system in Hadoop, and there are several concrete implementations for different file systems .
- Hadoop file system interfaces provide the following features and functionalities  :
  - Uniform access to different types of file systems using the URI scheme to select the appropriate file system instance to communicate with.
  - Streaming access to file system data, allowing applications to read and write large amounts of data efficiently.
  - Support for basic file operations, such as create, open, delete, rename, list, etc.
  - Support for advanced file operations, such as append, truncate, concat, snapshot, etc.
  - Support for file system metadata operations, such as get file status, get content summary, get file checksum, etc.
  - Support for file system permission and security operations, such as set owner, set permission, set ACL, etc.
  - Support for file system performance and reliability operations, such as set replication, set block size, set storage policy, etc.
  - Support for file system configuration and customization operations, such as set working directory, set default block size, set default replication, etc.
  - Support for file system delegation token operations, such as get delegation token, renew delegation token, cancel delegation token, etc.