### Java interfaces to HDFS

- Hadoop provides a Java API for interacting with its filesystems, which is represented by the `FileSystem` class.
- A file in a Hadoop filesystem is represented by a `Path` object.
- The `FSDataInputStream` class can be used to read data from a file in HDFS.
- The `FSDataOutputStream` class can be used to write data to a file in HDFS.
- The `FileSystem` class also provides methods for querying the filesystem, such as checking if a file exists.
- Here is an example of Java code for writing a file to HDFS:
```java
Configuration conf = new Configuration();
FileSystem fileSystem = FileSystem.get(conf);
Path path = new Path("/path/to/file.ext");
if (!fileSystem.exists(path)) {
    FSDataOutputStream out = fileSystem.create(path);
    // write data to file
    out.close();
}
```

- The filesystem shell is a Java application that uses the `FileSystem` class to provide filesystem operations.
- By exposing its filesystem interface as a Java API, Hadoop makes it awkward for non-Java applications to access HDFS.
- The command-line interface is another way to interact with HDFS, which has support for filesystem operations like reading files, creating directories, moving files, deleting data, and listing directories.