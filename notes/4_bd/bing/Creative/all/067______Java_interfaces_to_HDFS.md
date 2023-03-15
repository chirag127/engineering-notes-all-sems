#### Java interfaces to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing.
- HDFS provides a Java API for interacting with the filesystem, which is the primary way of accessing data stored in HDFS.
- The Java API is based on the abstract FileSystem class, which defines the common operations for different filesystem implementations, such as local, HDFS, S3, etc.
- To use the Java API, one needs to create a FileSystem object with a configuration object that specifies the filesystem URI and other parameters.
- The FileSystem object can then be used to perform various operations on files and directories, such as create, open, read, write, append, delete, rename, list, etc.
- The FileSystem class also provides methods for querying the filesystem status, such as getCapacity, getUsed, getContentSummary, getFileStatus, etc.
- The Java API supports both sequential and random access to files in HDFS, using the FSDataInputStream and FSDataOutputStream classes, which extend the standard Java InputStream and OutputStream classes.
- The FSDataInputStream class provides methods for seeking to a specific position in the file, as well as reading data in different formats, such as byte, short, int, long, float, double, etc.
- The FSDataOutputStream class provides methods for writing data in different formats, as well as flushing and syncing the data to the underlying storage.
- The Java API also supports compression and decompression of data in HDFS, using the CompressionCodec and CompressionInputStream/CompressionOutputStream classes, which can be obtained from the CompressionCodecFactory class.
- The Java API also supports checksum verification of data in HDFS, using the ChecksumFileSystem and ChecksumInputStream/ChecksumOutputStream classes, which wrap the underlying FileSystem and InputStream/OutputStream classes.
- The Java API also supports encryption and decryption of data in HDFS, using the CryptoFileSystem and CryptoInputStream/CryptoOutputStream classes, which wrap the underlying FileSystem and InputStream/OutputStream classes.
- The Java API also supports erasure coding of data in HDFS, using the ErasureCodingFileSystem and ErasureCodingInputStream/ErasureCodingOutputStream classes, which wrap the underlying FileSystem and InputStream/OutputStream classes.
- The Java API also supports accessing HDFS through other interfaces, such as WebHDFS, which is a RESTful web service that exposes the HDFS operations as HTTP methods, and libhdfs, which is a C library that uses the Java Native Interface (JNI) to call the Java API.

- Here is an example of using the Java API to create a file in HDFS and write some data to it:

```java
// Import the necessary classes
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FSDataOutputStream;

// Create a configuration object with the HDFS URI
Configuration conf = new Configuration();
conf.set("fs.defaultFS", "hdfs://namenode:8020");

// Create a FileSystem object with the configuration
FileSystem fs = FileSystem.get(conf);

// Create a Path object for the file to be created
Path path = new Path("/path/to/file.txt");

// Create a FSDataOutputStream object to write to the file
FSDataOutputStream out = fs.create(path);

// Write some data to the file
out.writeBytes("Hello, HDFS!\n");

// Close the stream and the filesystem
out.close();
fs.close();
```