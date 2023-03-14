#### Hadoop file system interfaces

- Hadoop provides a Java abstract class org.apache.hadoop.fs.FileSystem that represents the client interface to a file system in Hadoop.
- There are several concrete implementations of FileSystem for different types of file systems, such as local, distributed, object stores, etc.
- Hadoop uses the URI scheme to select the appropriate FileSystem instance to communicate with.
- FileSystem provides methods for creating, deleting, renaming, reading, writing, and listing files and directories.
- FileSystem also supports some advanced features, such as replication, checksum, space reclamation, metadata persistence, communication protocols, etc .
- Hadoop also provides other interfaces to its file systems, such as a command-line interface, a web browser interface, and a REST API .