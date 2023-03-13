#### Hadoop file system interfaces

- Hadoop file system interfaces are the Java abstract classes and interfaces that define the client API to interact with various file systems in Hadoop.
- The main interface is org.apache.hadoop.fs.FileSystem, which represents a generic file system that can be implemented by different concrete classes.
- Hadoop uses the URI scheme to select the appropriate file system instance to communicate with, such as hdfs://, file://, s3://, etc.
- Hadoop file system interfaces provide methods for creating, deleting, renaming, reading, writing, and listing files and directories, as well as accessing file system metadata and configuration.
- Hadoop file system interfaces also support streaming access to file system data, which allows applications to process large amounts of data efficiently without loading the entire file into memory.
- Hadoop file system interfaces are designed to be highly fault-tolerant, scalable, and compatible with existing distributed file systems.