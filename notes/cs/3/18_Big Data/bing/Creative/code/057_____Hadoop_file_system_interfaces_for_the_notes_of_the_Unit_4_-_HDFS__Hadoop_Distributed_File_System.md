### Hadoop file system interfaces

- Hadoop file system interfaces are the Java classes and methods that allow applications to interact with various file systems in Hadoop.
- The abstract class `org.apache.hadoop.fs.FileSystem` represents the client interface to a file system in Hadoop, and there are several concrete implementations for different file systems, such as HDFS, S3, FTP, etc.
- Hadoop file system interfaces provide the following functionalities:
  - Create, delete, rename, and move files and directories.
  - Read and write data to and from files.
  - Get file and directory metadata, such as size, modification time, permissions, etc.
  - Check the status and health of the file system.
  - Perform operations on file system blocks, such as replication, checksum, etc.
- Hadoop file system interfaces use the URI scheme to select the appropriate file system implementation to communicate with. For example, `hdfs://` for HDFS, `s3://` for S3, etc.
- Hadoop file system interfaces can be accessed through various ways, such as:
  - The Java API, which provides the classes and methods to manipulate files and directories programmatically.
  - The command-line interface, which provides the `hadoop fs` command to perform file system operations interactively or in scripts.
  - The web interface, which provides the built-in servers of namenode and datanode to check the status and browse the file system through a web browser.