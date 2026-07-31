#### Java interfaces to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing applications.
- HDFS provides several interfaces for accessing and manipulating data stored in its filesystem, such as command-line interface, web interface, and Java interface.
- The Java interface is the most commonly used interface for Hadoop filesystem interactions, as it exposes the Hadoop FileSystem class, which is the abstract base class for all Hadoop filesystem implementations.
- The FileSystem class provides methods for creating, reading, writing, deleting, renaming, and listing files and directories in HDFS, as well as obtaining metadata and statistics about the filesystem.
- To use the Java interface, one needs to create a FileSystem object by passing a Configuration object that contains the HDFS configuration parameters, such as the namenode address, the replication factor, and the block size.
- The FileSystem object can then be used to obtain a Path object, which represents a file or a directory in HDFS, and perform various operations on it using the FileSystem methods.
- For example, to create a file in HDFS, one can use the create() method of the FileSystem class, which returns a FSDataOutputStream object that can be used to write data to the file.
- Similarly, to read a file in HDFS, one can use the open() method of the FileSystem class, which returns a FSDataInputStream object that can be used to read data from the file.
- The FileSystem class also provides methods for appending, copying, moving, and deleting files and directories, as well as checking the existence, permission, and ownership of a Path object.
- Additionally, the FileSystem class provides methods for querying the filesystem, such as getting the status, capacity, usage, and block locations of a Path object, as well as listing the files and directories under a given Path object.
- The Java interface for HDFS is flexible and powerful, as it allows users to interact with different Hadoop filesystem implementations, such as HDFS, S3, and Azure Blob Storage, using the same FileSystem API.