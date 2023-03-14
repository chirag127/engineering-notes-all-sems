#### Java interfaces to HDFS

- HDFS is a distributed file system that is implemented in Java and runs on top of Hadoop.
- HDFS provides a Java interface for programming, which is based on the abstract class org.apache.hadoop.fs.FileSystem. This class represents the client interface to a file system in Hadoop, and there are several concrete implementations for different file systems, such as HDFS, local file system, S3, etc.
- To use the Java interface of HDFS, one needs to create a Configuration object that encapsulates the client's configuration, such as the HDFS URI, the user name, the replication factor, etc. The configuration can be set using XML files, such as core-site.xml and hdfs-site.xml, or programmatically.
- Then, one can use the static factory methods of FileSystem class to get an instance of the file system, such as FileSystem.get(conf) or FileSystem.get(uri, conf, user). The returned object is an instance of DistributedFileSystem, which is a subclass of FileSystem that implements the HDFS-specific features.
- The FileSystem class provides various methods for manipulating files and directories in HDFS, such as create, open, delete, rename, copy, list, etc. These methods take Path objects as arguments, which represent the HDFS file or directory names. A Path object can be created from a String or a URI, such as new Path("/user/hadoop/file.txt") or new Path("hdfs://namenode:8020/user/hadoop/file.txt").
- The FileSystem class also provides methods for getting file status, such as getFileStatus, listStatus, getContentSummary, etc. These methods return FileStatus objects, which contain information about the file or directory, such as the length, the block size, the owner, the permission, the modification time, etc.
- To read or write data from or to HDFS files, one can use the FSDataInputStream and FSDataOutputStream classes, which are subclasses of java.io.DataInputStream and java.io.DataOutputStream, respectively. These classes provide methods for reading and writing primitive data types, such as int, long, float, double, etc. They also implement the Seekable and PositionedReadable interfaces, which allow random access to the file data.
- To read or write data in a more efficient way, one can use the CompressionCodec and CompressionInputStream and CompressionOutputStream classes, which provide methods for compressing and decompressing data using various algorithms, such as gzip, bzip2, snappy, etc. These classes can be used in conjunction with the FSDataInputStream and FSDataOutputStream classes to reduce the network and disk usage.
- To read or write data in a more structured way, one can use the SequenceFile and MapFile classes, which provide methods for storing and retrieving key-value pairs in HDFS files. These classes can be used to store intermediate or final results of MapReduce jobs, or to store metadata or indexes for HDFS files. SequenceFile supports various compression and serialization options, such as record, block, and custom compression, and Writable, Avro, and Thrift serialization. MapFile is a subclass of SequenceFile that provides faster lookup for keys by using an index file.

Here is an example of using the Java interface of HDFS to create a file and write some data to it:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FSDataOutputStream;

public class HDFSWriteExample {

  public static void main(String[] args) throws Exception {
    // Create a configuration object
    Configuration conf = new Configuration();
    // Set the HDFS URI
    conf.set("fs.defaultFS", "hdfs://namenode:8020");
    // Get an instance of the file system
    FileSystem fs = FileSystem.get(conf);
    // Create a path object for the file to be created
    Path path = new Path("/user/hadoop/hello.txt");
    // Create a file output stream
    FSDataOutputStream out = fs.create(path);
    // Write some data to the file
    out.writeUTF("Hello, world!");
    // Close the stream
    out.close();
    // Close the file system
    fs.close();
  }
}
```