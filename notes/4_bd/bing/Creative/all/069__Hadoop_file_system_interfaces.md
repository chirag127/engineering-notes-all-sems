#### Hadoop file system interfaces

- Hadoop file system interfaces are the Java APIs that define how applications can interact with the Hadoop file system (HDFS).
- Hadoop file system interfaces are divided into two categories: low-level and high-level.
- Low-level interfaces provide basic operations such as creating, deleting, renaming, and listing files and directories, as well as reading and writing data to files.
- High-level interfaces provide more advanced features such as compression, encryption, checksums, and replication.
- The main low-level interface is the `org.apache.hadoop.fs.FileSystem` class, which is an abstract class that defines the common methods for all file systems supported by Hadoop.
- The main high-level interface is the `org.apache.hadoop.fs.FileContext` class, which is a wrapper around the `FileSystem` class that provides a more convenient and consistent way of accessing the file system.
- The `FileContext` class also supports multiple file system implementations, such as local, HDFS, S3, FTP, etc., by using the `org.apache.hadoop.fs.AbstractFileSystem` class as an abstraction layer.
- The `AbstractFileSystem` class defines the methods that are specific to each file system implementation, such as creating and deleting files, setting permissions, etc.
- The `FileContext` class uses the `org.apache.hadoop.fs.FSDataInputStream` and `org.apache.hadoop.fs.FSDataOutputStream` classes to read and write data to files, respectively.
- The `FSDataInputStream` and `FSDataOutputStream` classes are subclasses of the `java.io.DataInputStream` and `java.io.DataOutputStream` classes, respectively, and provide additional methods for seeking, skipping, and getting the current position in the file.
- The `FileContext` class also uses the `org.apache.hadoop.fs.Path` class to represent the file system paths, which are URI-based and can include the scheme, authority, and path components.
- The `Path` class provides methods for manipulating and resolving paths, such as getting the parent, the name, the extension, etc.
- The `FileContext` class also supports various file system operations, such as creating and deleting directories, renaming and moving files, listing files and directories, checking the existence and status of files, etc., by using the `org.apache.hadoop.fs.FileStatus` class to represent the metadata of files and directories.
- The `FileStatus` class contains information such as the path, the length, the modification time, the permission, the owner, the group, the block size, the replication factor, etc., of a file or a directory.
- The `FileContext` class also supports various file system filters, such as the `org.apache.hadoop.fs.PathFilter` interface, which allows applications to filter out files or directories based on their paths, and the `org.apache.hadoop.fs.PathFilter` interface, which allows applications to filter out files or directories based on their statuses.
- The `FileContext` class also supports various file system utilities, such as the `org.apache.hadoop.fs.FileUtil` class, which provides methods for copying, moving, deleting, and comparing files and directories, and the `org.apache.hadoop.fs.FsShell` class, which provides a command-line interface for performing file system operations.