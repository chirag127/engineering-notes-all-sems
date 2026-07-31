# Java Interfaces to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing.
- HDFS provides a Java API for interacting with the filesystem, which is the primary way of accessing data stored in HDFS.
- The Java API is based on the abstract FileSystem class, which defines the common operations for different filesystem implementations.
- HDFS is one of the subclasses of FileSystem, which implements the specific logic for communicating with the HDFS namenode and datanodes.
- To use the Java API, one needs to create a FileSystem object with a given configuration, which specifies the HDFS URI and other parameters.
- The FileSystem object provides methods for creating, reading, writing, deleting, renaming, and listing files and directories in HDFS.
- Some of the common methods are:

  - `create(Path f)`: Creates a new file in HDFS and returns an FSDataOutputStream for writing data to it.
  - `open(Path f)`: Opens an existing file in HDFS and returns an FSDataInputStream for reading data from it.
  - `delete(Path f, boolean recursive)`: Deletes a file or a directory in HDFS. If the second argument is true, it deletes the directory and all its contents recursively.
  - `rename(Path src, Path dst)`: Renames a file or a directory in HDFS from src to dst.
  - `exists(Path f)`: Checks if a file or a directory exists in HDFS.
  - `getFileStatus(Path f)`: Returns a FileStatus object that contains the metadata of a file or a directory, such as the length, the block size, the replication factor, the modification time, etc.
  - `listStatus(Path f)`: Returns an array of FileStatus objects that represent the files and directories under a given path in HDFS.

- The FSDataInputStream and FSDataOutputStream classes are subclasses of the standard Java InputStream and OutputStream classes, which provide methods for reading and writing bytes, primitives, and objects.
- The FSDataInputStream class also supports random access and seeking to any position in the file, which is useful for implementing input formats and record readers for MapReduce jobs.
- The FSDataOutputStream class also supports flushing and syncing the data to the underlying datanodes, which is useful for ensuring data durability and consistency.
- Here is an example of using the Java API to write a file in HDFS:

  ```java
  // Create a configuration object with the HDFS URI
  Configuration conf = new Configuration();
  conf.set("fs.defaultFS", "hdfs://namenode:8020");

  // Create a FileSystem object with the configuration
  FileSystem fs = FileSystem.get(conf);

  // Create a new file in HDFS
  Path path = new Path("/path/to/file.txt");
  FSDataOutputStream out = fs.create(path);

  // Write some data to the file
  out.writeUTF("Hello, world!");
  out.writeInt(42);

  // Close the stream and the filesystem
  out.close();
  fs.close();
  ```