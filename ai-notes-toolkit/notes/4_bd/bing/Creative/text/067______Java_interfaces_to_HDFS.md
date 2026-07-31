#### Java interfaces to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing applications.
- HDFS provides several interfaces for accessing and manipulating data stored in its filesystem, such as command-line interface, web interface, and Java interface.
- The Java interface is the most commonly used interface for Hadoop filesystem interactions, as it exposes the Hadoop FileSystem class, which is the abstract base class for all Hadoop filesystem implementations.
- The FileSystem class provides methods for creating, opening, reading, writing, deleting, renaming, and listing files and directories in a Hadoop filesystem.
- A file in a Hadoop filesystem is represented by a Hadoop Path object, which encapsulates the URI of the file. A Path object can be created from a string, such as `Path path = new Path("/path/to/file.ext");`
- To access a Hadoop filesystem, a Java application needs to create a FileSystem object, which can be obtained from a Configuration object, such as `FileSystem fileSystem = FileSystem.get(conf);`
- The Configuration object contains the settings and properties for the Hadoop cluster, such as the default filesystem URI, the replication factor, the block size, etc. The Configuration object can be created from a default or a custom configuration file, such as `Configuration conf = new Configuration();` or `Configuration conf = new Configuration(new Path("/path/to/config.xml"));`
- To read data from a file in a Hadoop filesystem, a Java application needs to create an FSDataInputStream object, which is a subclass of java.io.InputStream, such as `FSDataInputStream in = fileSystem.open(path);`
- The FSDataInputStream object supports random access to the file, as well as various methods for reading bytes, primitives, and objects from the stream, such as `in.read()`, `in.readInt()`, `in.readUTF()`, etc.
- To write data to a file in a Hadoop filesystem, a Java application needs to create an FSDataOutputStream object, which is a subclass of java.io.OutputStream, such as `FSDataOutputStream out = fileSystem.create(path);`
- The FSDataOutputStream object supports various methods for writing bytes, primitives, and objects to the stream, such as `out.write()`, `out.writeInt()`, `out.writeUTF()`, etc.
- To query the filesystem, a Java application can use the FileSystem class methods, such as `fileSystem.exists(path)`, `fileSystem.getFileStatus(path)`, `fileSystem.listStatus(path)`, etc.
- To close the filesystem, a Java application needs to call the `fileSystem.close()` method, which releases the resources associated with the FileSystem object.