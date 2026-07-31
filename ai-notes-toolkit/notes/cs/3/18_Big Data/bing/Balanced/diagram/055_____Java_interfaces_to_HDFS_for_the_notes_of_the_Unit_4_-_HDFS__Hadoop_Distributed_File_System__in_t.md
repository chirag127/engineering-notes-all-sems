### Java interfaces to HDFS

- HDFS is a distributed file system that runs on a cluster of nodes and stores large amounts of data in a fault-tolerant way.
- HDFS provides a Java API for interacting with the file system, which is the primary way of accessing data in HDFS.
- The Java API consists of two main classes: FileSystem and Path.
  - FileSystem is an abstract class that represents a generic file system and provides methods for creating, deleting, reading, writing, and querying files and directories.
  - Path is a class that represents a file or directory name in a file system. A Path object can be absolute or relative, and can refer to a local or remote file system.
- To use the Java API, one needs to create a FileSystem object by passing a Configuration object that contains the Hadoop settings and the URI of the file system to connect to.
  - For example, to create a FileSystem object for the default HDFS, one can use the following code:

```java
Configuration conf = new Configuration();
FileSystem fs = FileSystem.get(conf);
```

  - To create a FileSystem object for a specific HDFS, one can use the following code:

```java
Configuration conf = new Configuration();
URI uri = new URI("hdfs://namenode:8020");
FileSystem fs = FileSystem.get(uri, conf);
```

- To read data from a file in HDFS, one needs to create a Path object for the file name, and then use the FileSystem object to open an FSDataInputStream object, which is a subclass of Java's InputStream class.
  - For example, to read the first 100 bytes of a file in HDFS, one can use the following code:

```java
Path path = new Path("/path/to/file");
FSDataInputStream in = fs.open(path);
byte[] buffer = new byte[100];
int bytesRead = in.read(buffer);
in.close();
```

- To write data to a file in HDFS, one needs to create a Path object for the file name, and then use the FileSystem object to create an FSDataOutputStream object, which is a subclass of Java's OutputStream class.
  - For example, to write the string "Hello, world!" to a file in HDFS, one can use the following code:

```java
Path path = new Path("/path/to/file");
FSDataOutputStream out = fs.create(path);
out.writeUTF("Hello, world!");
out.close();
```

- To query the file system, one can use the FileSystem object to perform various operations, such as listing files and directories, checking the existence and status of a file or directory, getting the file system capacity and usage, and so on.
  - For example, to list the files and directories in the root directory of HDFS, one can use the following code:

```java
Path path = new Path("/");
FileStatus[] status = fs.listStatus(path);
for (FileStatus s : status) {
  System.out.println(s.getPath());
}
```