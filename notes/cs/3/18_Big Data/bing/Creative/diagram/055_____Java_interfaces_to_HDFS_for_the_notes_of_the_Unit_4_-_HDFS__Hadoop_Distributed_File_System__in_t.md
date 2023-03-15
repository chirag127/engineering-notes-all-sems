### Java interfaces to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing applications.
- HDFS provides a Java API for interacting with the filesystem, which is based on the abstract FileSystem class.
- The FileSystem class defines methods for creating, reading, writing, deleting, renaming, and listing files and directories in HDFS.
- To use the FileSystem API, one needs to create a FileSystem object by calling the static get() method and passing a Configuration object that contains the HDFS configuration parameters.
- The FileSystem object represents a connection to the HDFS cluster, and can be used to perform various operations on the files and directories.
- A file in HDFS is represented by a Path object, which encapsulates the URI of the file. A Path object can be created by passing a string or a URI to the constructor.
- To read data from a file in HDFS, one can use the open() method of the FileSystem class, which returns a FSDataInputStream object. This object implements the standard Java InputStream interface, and provides methods for reading bytes, arrays, and primitives from the file.
- To write data to a file in HDFS, one can use the create() method of the FileSystem class, which returns a FSDataOutputStream object. This object implements the standard Java OutputStream interface, and provides methods for writing bytes, arrays, and primitives to the file.
- To query the filesystem for information such as file size, modification time, replication factor, block size, etc., one can use the getFileStatus() method of the FileSystem class, which returns a FileStatus object. This object contains various attributes of the file or directory.
- To list the files and directories in a given path, one can use the listStatus() method of the FileSystem class, which returns an array of FileStatus objects. This method can also take a PathFilter object as an argument, which can be used to filter the results based on some criteria.
- Some examples of using the Java API for HDFS are:

  - Creating a file and writing some text to it:

  ```java
  Configuration conf = new Configuration();
  FileSystem fs = FileSystem.get(conf);
  Path path = new Path("/path/to/file.txt");
  FSDataOutputStream out = fs.create(path);
  out.writeUTF("Hello, HDFS!");
  out.close();
  ```

  - Reading a file and printing its contents:

  ```java
  Configuration conf = new Configuration();
  FileSystem fs = FileSystem.get(conf);
  Path path = new Path("/path/to/file.txt");
  FSDataInputStream in = fs.open(path);
  String text = in.readUTF();
  System.out.println(text);
  in.close();
  ```

  - Listing the files and directories in the root path:

  ```java
  Configuration conf = new Configuration();
  FileSystem fs = FileSystem.get(conf);
  Path path = new Path("/");
  FileStatus[] status = fs.listStatus(path);
  for (FileStatus s : status) {
    System.out.println(s.getPath());
  }
  ```