# Java interfaces to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing applications.
- HDFS provides several interfaces for accessing and manipulating data stored in its filesystem, such as command-line, web, and Java interfaces.
- The Java interface is the most commonly used interface for HDFS, as it allows users to programmatically interact with the filesystem using the Hadoop FileSystem class and its subclasses.
- The FileSystem class is an abstract class that defines the common operations for all Hadoop filesystems, such as opening, reading, writing, closing, deleting, renaming, and listing files and directories.
- The FileSystem class also provides methods for getting and setting the configuration, statistics, and status of the filesystem.
- The FileSystem class has several subclasses that implement the specific functionality for different types of Hadoop filesystems, such as LocalFileSystem, HdfsFileSystem, S3FileSystem, and FTPFileSystem.
- To use the Java interface for HDFS, users need to create a FileSystem object using the static get() method, which takes a Configuration object and a URI as parameters.
- The Configuration object contains the settings and properties for the Hadoop cluster and the filesystem, such as the namenode address, the replication factor, and the block size.
- The URI specifies the scheme, authority, and path of the filesystem, such as hdfs://namenode:port/path/to/file.
- The get() method returns a FileSystem object that corresponds to the given URI, which can be cast to a specific subclass if needed.
- For example, to create a FileSystem object for HDFS, users can write:

```java
Configuration conf = new Configuration();
FileSystem fs = FileSystem.get(new URI("hdfs://namenode:9000"), conf);
```

- To read data from HDFS using the Java interface, users can use the open() method of the FileSystem class, which takes a Path object as a parameter and returns a FSDataInputStream object.
- The Path object represents a file or a directory in a Hadoop filesystem, and can be constructed from a String or a URI.
- The FSDataInputStream object is a subclass of the Java InputStream class, which provides methods for reading bytes, characters, arrays, and primitives from the input stream.
- For example, to read the contents of a file in HDFS, users can write:

```java
Path path = new Path("/path/to/file.txt");
FSDataInputStream in = fs.open(path);
BufferedReader br = new BufferedReader(new InputStreamReader(in));
String line = null;
while ((line = br.readLine()) != null) {
  System.out.println(line);
}
br.close();
in.close();
```

- To write data to HDFS using the Java interface, users can use the create() method of the FileSystem class, which takes a Path object and some optional parameters as arguments and returns a FSDataOutputStream object.
- The FSDataOutputStream object is a subclass of the Java OutputStream class, which provides methods for writing bytes, characters, arrays, and primitives to the output stream.
- For example, to write some text to a file in HDFS, users can write:

```java
Path path = new Path("/path/to/file.txt");
FSDataOutputStream out = fs.create(path);
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));
bw.write("Hello, world!");
bw.close();
out.close();
```

- To query the filesystem using the Java interface, users can use the methods of the FileSystem class that return information about the files and directories, such as exists(), isFile(), isDirectory(), getFileStatus(), listStatus(), getContentSummary(), and getBlockLocations().
- For example, to check if a file exists in HDFS, users can write:

```java
Path path = new Path("/path/to/file.txt");
boolean exists = fs.exists(path);
System.out.println(exists);
```

- To perform other filesystem operations using the Java interface, users can use the methods of the FileSystem class that modify the files and directories, such as delete(), rename(), mkdirs(), copyFromLocalFile(), copyToLocalFile(), moveFromLocalFile(), and moveToLocalFile().
- For example, to delete a file in HDFS, users can write:

```java
Path path = new Path("/path/to/file.txt");
boolean deleted = fs.delete(path, true);
System.out.println(deleted);
```

- These are some of the examples of using the Java interface for HDFS. For more details and documentation, users can refer to the official Hadoop API .