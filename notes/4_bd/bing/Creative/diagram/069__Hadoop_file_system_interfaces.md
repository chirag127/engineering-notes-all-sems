Hadoop file system interfaces are the Java abstract classes and interfaces that represent the client interface to a file system in Hadoop. There are several concrete implementations of Hadoop file system interfaces, such as HDFS, LocalFileSystem, FTPFileSystem, S3FileSystem, etc. Hadoop uses the URI scheme to choose the appropriate file system instance to communicate with.

#### Hadoop file system interfaces

The following diagram illustrates the basic architecture of Hadoop file system interfaces using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  LocalFileSystem|     |  FTPFileSystem  |     |  S3FileSystem   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
          |                     |                     |
          |                     |                     |
          |                     |                     |
          +---------------------+---------------------+
                            |
                            |
                            |
                    +-----------------+
                    |                 |
                    |   FileSystem    |
                    |                 |
                    +-----------------+
                            |
                            |
                            |
                    +-----------------+
                    |                 |
                    |   Configured    |
                    |                 |
                    +-----------------+
                            |
                            |
                            |
                    +-----------------+
                    |                 |
                    |   Configurable  |
                    |                 |
                    +-----------------+
                            |
                            |
                            |
                    +-----------------+
                    |                 |
                    |   Closeable     |
                    |                 |
                    +-----------------+
                            |
                            |
                            |
                    +-----------------+
                    |                 |
                    |   AutoCloseable |
                    |                 |
                    +-----------------+
```

The FileSystem class is the abstract base class for all the file system implementations. It extends the Configured class, which implements the Configurable interface. The Configurable interface allows the file system to access the Hadoop configuration. The FileSystem class also implements the Closeable and AutoCloseable interfaces, which allow the file system to be closed when it is no longer needed.

The LocalFileSystem, FTPFileSystem, S3FileSystem, etc. are the concrete subclasses of the FileSystem class. They implement the specific logic for interacting with different types of file systems, such as local disk, FTP server, Amazon S3, etc. They use the URI scheme to identify the file system, such as file://, ftp://, s3://, etc. They also override some of the methods of the FileSystem class to provide customized behavior for different file systems. For example, the LocalFileSystem class overrides the getDefaultReplication method to return 1, since local files do not have replication. The FTPFileSystem class overrides the getUri method to return the FTP server address and port. The S3FileSystem class overrides the create method to upload the data to S3 using multipart upload.