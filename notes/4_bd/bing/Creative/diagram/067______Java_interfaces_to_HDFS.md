#### Java interfaces to HDFS

Hadoop Distributed File System (HDFS) is a distributed file system that runs on a cluster of nodes. HDFS provides high availability, fault tolerance, scalability, and reliability for storing and processing large amounts of data.

HDFS can be accessed by various applications using different interfaces, such as command-line, web browser, REST API, or Java API. The Java API is the most commonly used interface for interacting with HDFS programmatically. The Java API exposes the Hadoop FileSystem class, which is an abstract class that represents a generic file system. FileSystem has several subclasses that implement the specific file system protocols, such as Hdfs, LocalFileSystem, S3FileSystem, etc.

The FileSystem class provides methods for creating, reading, writing, deleting, renaming, and listing files and directories in HDFS. A file in HDFS is represented by a Path object, which is a URI that specifies the scheme, authority, and path of the file. A Path object can be created by passing a string to its constructor, such as:

```java
Path path = new Path("hdfs://namenode:8020/user/hadoop/file.txt");
```

To access HDFS using the Java API, an application needs to create a FileSystem object by calling the static get() method and passing a Configuration object that contains the Hadoop settings. For example:

```java
Configuration conf = new Configuration();
FileSystem fs = FileSystem.get(conf);
```

The Configuration object can be initialized with the default Hadoop settings by loading the core-site.xml and hdfs-site.xml files from the classpath. Alternatively, the Configuration object can be customized by setting the properties programmatically, such as:

```java
conf.set("fs.defaultFS", "hdfs://namenode:8020");
conf.set("dfs.replication", "3");
```

The FileSystem object can then be used to perform various operations on HDFS, such as:

- Creating a file and writing data to it:

```java
FSDataOutputStream out = fs.create(path);
out.writeUTF("Hello, HDFS!");
out.close();
```

- Reading data from a file:

```java
FSDataInputStream in = fs.open(path);
String data = in.readUTF();
in.close();
```

- Deleting a file or a directory:

```java
fs.delete(path, true); // true for recursive deletion
```

- Renaming a file or a directory:

```java
fs.rename(path, newPath);
```

- Listing the files and directories in a directory:

```java
FileStatus[] status = fs.listStatus(path);
for (FileStatus s : status) {
  System.out.println(s.getPath());
}
```

The following diagram shows the Java interfaces to HDFS:

```
+------------------+      +-----------------+
|    Application   |      |   Hadoop CLI    |
+------------------+      +-----------------+
|                  |      |                 |
|  Java API        |      |  Shell commands |
|                  |      |                 |
+--------+---------+      +--------+--------+
         |                         |
         |                         |
         |                         |
         +-------------------------+
         |
         |
         v
+------------------+      +-----------------+
|    FileSystem    |      |    Hdfs         |
+------------------+      +-----------------+
|                  |      |                 |
|  Abstract class  |<-----|  Subclass       |
|                  |      |                 |
+--------+---------+      +--------+--------+
         |
         |
         v
+------------------+      +-----------------+
|    Path          |      |    URI          |
+------------------+      +-----------------+
|                  |      |                 |
|  File or dir     |<-----|  Scheme, host,  |
|  in HDFS         |      |  port, path     |
|                  |      |                 |
+------------------+      +-----------------+
```