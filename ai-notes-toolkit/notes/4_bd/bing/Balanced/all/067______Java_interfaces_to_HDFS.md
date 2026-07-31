#### Java interfaces to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing applications.
- HDFS provides several interfaces for accessing and manipulating data stored in its filesystem, such as command-line interface, web interface, and Java interface.
- The Java interface is the most commonly used interface for HDFS, as it allows users to programmatically interact with HDFS using the Java programming language.
- The Java interface for HDFS is based on the Java FileSystem class, which is an abstract class that defines the common operations for different types of filesystems, such as local, HDFS, S3, etc.
- The Java FileSystem class has several subclasses that implement the specific functionality for each filesystem type, such as DistributedFileSystem for HDFS, LocalFileSystem for local, S3FileSystem for S3, etc.
- The Java FileSystem class provides methods for creating, opening, reading, writing, deleting, renaming, and listing files and directories in HDFS, as well as querying the filesystem status, such as capacity, usage, replication, block size, etc.
- To use the Java interface for HDFS, users need to create a FileSystem object that represents the HDFS instance they want to access, and then use the methods of the FileSystem object to perform the desired operations.
- To create a FileSystem object, users need to pass a Configuration object that contains the Hadoop configuration properties, such as the HDFS URI, the default filesystem scheme, the user name, etc.
- The Configuration object can be created programmatically, or loaded from XML files, such as core-site.xml and hdfs-site.xml, that are located in the Hadoop installation directory or the classpath.
- The FileSystem object can be obtained by calling the static method FileSystem.get(Configuration conf) or FileSystem.get(URI uri, Configuration conf), which returns the appropriate subclass of FileSystem based on the configuration or the URI.
- For example, the following code snippet creates a FileSystem object that represents the HDFS instance with the URI hdfs://localhost:9000, and then lists the files and directories in the root directory of HDFS:

```java
// Create a Configuration object and set the HDFS URI
Configuration conf = new Configuration();
conf.set("fs.defaultFS", "hdfs://localhost:9000");

// Create a FileSystem object
FileSystem fs = FileSystem.get(conf);

// List the files and directories in the root directory of HDFS
FileStatus[] status = fs.listStatus(new Path("/"));
for (FileStatus s : status) {
  System.out.println(s.getPath());
}
```

- The Java interface for HDFS also provides classes for reading and writing data from and to HDFS files, such as FSDataInputStream and FSDataOutputStream, which are subclasses of the Java InputStream and OutputStream classes, respectively.
- The FSDataInputStream class provides methods for reading bytes, primitives, and objects from HDFS files, as well as seeking to a specific position in the file, and getting the current position in the file.
- The FSDataOutputStream class provides methods for writing bytes, primitives, and objects to HDFS files, as well as flushing and closing the output stream.
- For example, the following code snippet creates a FSDataOutputStream object that writes data to a HDFS file named /path/to/file.txt, and then closes the output stream:

```java
// Create a FileSystem object
FileSystem fs = FileSystem.get(conf);

// Create a FSDataOutputStream object that writes data to a HDFS file
FSDataOutputStream out = fs.create(new Path("/path/to/file.txt"));

// Write some data to the output stream
out.writeUTF("Hello, world!");
out.writeInt(42);

// Close the output stream
out.close();
```

- The Java interface for HDFS also provides classes for performing advanced operations on HDFS files, such as FileUtil, FSShell, and DistributedFileSystem.
- The FileUtil class provides static utility methods for manipulating HDFS files and directories, such as copying, moving, deleting, and comparing files and directories, as well as converting HDFS paths to URIs and vice versa.
- The FSShell class provides a Java implementation of the HDFS command-line interface, which allows users to execute HDFS commands programmatically, such as ls, cat, mkdir, rm, etc.
- The DistributedFileSystem class is a subclass of FileSystem that implements the specific functionality for HDFS, such as creating and deleting files and directories, setting and getting file permissions and ownership, getting file checksums, etc.
- For example, the following code snippet uses the DistributedFileSystem class to get the replication factor and