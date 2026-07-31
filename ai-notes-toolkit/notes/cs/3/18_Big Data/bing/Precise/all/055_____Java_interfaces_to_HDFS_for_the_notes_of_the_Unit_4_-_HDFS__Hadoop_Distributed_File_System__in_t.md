# Java interfaces to HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It provides high-throughput access to application data and is suitable for applications that have large data sets.

Java interfaces to HDFS allow developers to interact with the Hadoop file system using the Java programming language. The primary Java interface for Hadoop file systems is the `FileSystem` class, which provides an API for interacting with one of Hadoop’s file systems.

## Reading Data Using the FileSystem API

A file in a Hadoop file system is represented by a `Path` object. The `FileSystem` class provides methods for reading data from a file, such as `open` which returns an `FSDataInputStream` object.

## Writing Data

The `FileSystem` class also provides methods for writing data to a file, such as `create` which returns an `FSDataOutputStream` object.

## Querying the Filesystem

The `FileSystem` class provides methods for querying the file system, such as `exists` which checks if a file or directory exists, and `getFileStatus` which returns information about a file or directory.

## Examples

Here is an example of Java code for writing a file in HDFS:

```java
Configuration conf = new Configuration();
FileSystem fileSystem = FileSystem.get(conf);
Path path = new Path("/path/to/file.ext");
if (!fileSystem.exists(path)) {
    FSDataOutputStream out = fileSystem.create(path);
    out.writeUTF("Hello, World!");
    out.close();
}
```

This code creates a `Configuration` object, gets a `FileSystem` object, and checks if the specified file exists. If the file does not exist, the code creates an `FSDataOutputStream` object and writes the string "Hello, World!" to the file.

## Conclusion

Java interfaces to HDFS provide a convenient way for developers to interact with the Hadoop file system using the Java programming language. The `FileSystem` class is the primary Java interface for Hadoop file systems, providing methods for reading and writing data, as well as querying the file system.