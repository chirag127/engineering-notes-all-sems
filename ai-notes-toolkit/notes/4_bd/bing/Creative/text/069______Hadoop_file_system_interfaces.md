#### Hadoop file system interfaces

- Hadoop file system interfaces are the Java abstract classes and interfaces that define the client API to interact with various file systems in Hadoop.
- The main interface is org.apache.hadoop.fs.FileSystem, which represents a generic file system that can be local, distributed, or cloud-based.
- FileSystem provides methods to create, delete, rename, read, write, and list files and directories, as well as to get file status and configuration information.
- FileSystem also supports the concept of URI schemes, which allow users to specify the file system implementation and the location of the data using a uniform syntax.
- For example, hdfs://namenode:port/path is a URI scheme for HDFS, while s3a://bucket/path is a URI scheme for Amazon S3.
- Hadoop provides several concrete implementations of FileSystem, such as HDFS, LocalFileSystem, RawLocalFileSystem, FTPFileSystem, S3AFileSystem, AzureBlobFileSystem, and so on.
- Each implementation has its own configuration properties, performance characteristics, and limitations.
- Users can also extend FileSystem or its subclasses to create custom file system implementations for their specific needs.