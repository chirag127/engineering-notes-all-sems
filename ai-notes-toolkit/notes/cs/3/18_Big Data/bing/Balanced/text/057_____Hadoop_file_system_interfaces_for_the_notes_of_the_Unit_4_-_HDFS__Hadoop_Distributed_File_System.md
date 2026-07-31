### Hadoop file system interfaces

- Hadoop file system interfaces are the Java abstract classes and interfaces that define the client API to interact with various file systems in Hadoop.
- The main interface is `org.apache.hadoop.fs.FileSystem`, which represents a generic file system that can be local, distributed, or cloud-based.
- Hadoop file system interfaces use the URI scheme to select the appropriate file system implementation to communicate with. For example, `hdfs://` for HDFS, `file://` for local file system, `s3://` for Amazon S3, etc.
- Hadoop file system interfaces provide methods for creating, deleting, renaming, reading, writing, and appending files, as well as listing, moving, and copying directories.
- Hadoop file system interfaces also support file system metadata operations, such as getting file status, permissions, checksums, and block locations.
- Hadoop file system interfaces can be accessed through the command-line interface (`hadoop fs`), the Java API, or the web interface (namenode and datanode web servers).
- Some of the common file system implementations in Hadoop are:
  - HDFS: The default distributed file system for Hadoop, designed to store large amounts of data across multiple nodes with high fault-tolerance and scalability.
  - LocalFileSystem: A file system that accesses the local disk of the node where the client is running. It is mainly used for testing and debugging purposes.
  - RawLocalFileSystem: A file system that bypasses the checksum verification of LocalFileSystem and directly accesses the local disk. It is faster than LocalFileSystem but less reliable.
  - FTPFileSystem: A file system that accesses files on a remote FTP server. It is mainly used for data ingestion from external sources.
  - S3FileSystem: A file system that accesses files on Amazon S3, a cloud storage service. It is mainly used for data backup and archiving.
  - AzureFileSystem: A file system that accesses files on Microsoft Azure, a cloud platform. It is mainly used for data integration with Azure services.
  - ViewFileSystem: A file system that provides a unified view of multiple file systems. It is mainly used for federating multiple namespaces and mounting different file systems.