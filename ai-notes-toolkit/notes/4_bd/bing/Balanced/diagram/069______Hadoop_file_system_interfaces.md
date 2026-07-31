Hadoop file system interfaces are the Java abstract classes and interfaces that represent the client interface to a file system in Hadoop. There are several concrete implementations of these interfaces, such as HDFS, S3, FTP, etc. Hadoop uses the URI scheme to select the appropriate file system instance to communicate with.

A simplified diagram of the Hadoop file system interfaces is shown below:

```
+---------------------+    +---------------------+
| org.apache.hadoop.fs|    | org.apache.hadoop.fs|
|       FileSystem    |    |     PathFilter      |
+---------------------+    +---------------------+
          ^  ^  ^                    ^
          |  |  |                    |
          |  |  +--------------------+
          |  |
          |  +---------------------+
          |                        |
          |                        |
+---------------------+    +---------------------+
| org.apache.hadoop.fs|    | org.apache.hadoop.fs|
|    FilterFileSystem |    |    LocalFileSystem  |
+---------------------+    +---------------------+
          ^                        ^
          |                        |
          |                        |
+---------------------+    +---------------------+
| org.apache.hadoop.fs|    | org.apache.hadoop.fs|
|    ChecksumFileSystem|   |    RawLocalFileSystem|
+---------------------+    +---------------------+
```

The FileSystem class is the base class for all file system implementations. It provides methods for accessing, creating, deleting, renaming, and copying files and directories. It also supports file system statistics, checksums, and permissions.

The PathFilter interface is used to filter paths based on some criteria. It has a single method, accept, that returns true if the path should be included or false otherwise.

The FilterFileSystem class is a wrapper class that delegates all file system operations to another file system. It can be subclassed to provide additional functionality or modify the behavior of the underlying file system.

The LocalFileSystem class is a file system implementation that provides access to the local disk. It uses the RawLocalFileSystem class to perform the actual operations, and adds checksum support on top of it.

The RawLocalFileSystem class is a file system implementation that provides access to the local disk without any checksum support. It is a low-level class that should not be used directly by applications.