### Hadoop File System Interfaces

In the context of HDFS (Hadoop Distributed File System), there are various file system interfaces that are used for performing different operations. These interfaces are as follows:

- **FileSystem:** This interface provides an abstraction for the file system. It defines methods for creating, deleting, and modifying files and directories. It also provides methods for opening and closing streams, getting file status and permissions, and checking for the existence of files and directories.

- **Path:** This interface represents a path on the file system. It provides methods for manipulating paths such as resolving a path, getting the parent path, and getting the file name.

- **FSDataInputStream:** This interface provides an input stream for reading data from a file in the file system.

- **FSDataOutputStream:** This interface provides an output stream for writing data to a file in the file system.

- **FileStatus:** This interface represents the status of a file or directory in the file system. It provides methods for getting the file size, modification time, and permissions.

- **FileSystem.Statistics:** This interface provides statistics about the file system such as the number of bytes read and written, the number of files created and deleted, and the number of operations performed.

- **ChecksumFileSystem:** This interface extends FileSystem and adds support for data integrity checks using checksums. It provides methods for computing and verifying checksums.

- **DistributedFileSystem:** This interface extends FileSystem and provides support for distributed file systems. It provides methods for handling file replication, block sizes, and quotas.

- **FilterFileSystem:** This interface extends FileSystem and provides support for filtering operations on files and directories. It allows users to specify filters for file names, paths, and attributes.

By using these file system interfaces, developers can build applications that interact with HDFS in a variety of ways. These interfaces provide a standardized way of accessing and manipulating files and directories in HDFS, and they can be used with a variety of programming languages and frameworks.