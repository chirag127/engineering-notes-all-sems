### Java interfaces to HDFS

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing.
- HDFS provides a Java API for interacting with its filesystems, which is the most common way of accessing HDFS data.
- The Java API is based on the abstract FileSystem class, which defines the common operations for different types of filesystems, such as local, HDFS, S3, etc.
- To use the Java API, one needs to create a FileSystem object with a configuration object that specifies the HDFS URI and other parameters.
- The FileSystem object can then be used to perform various operations on files and directories, such as creating, reading, writing, deleting, copying, moving, renaming, etc.
- The Java API also provides specialized classes for reading and writing data from HDFS files, such as FSDataInputStream and FSDataOutputStream, which extend the standard Java IO classes.
- FSDataInputStream supports random access and seek operations, which are useful for reading data in parallel or skipping over unwanted data.
- FSDataOutputStream supports appending data to existing files, which is useful for writing data in batches or streaming data.
- The Java API also provides methods for querying the filesystem metadata, such as file size, block locations, replication factor, checksum, etc.
- The Java API also supports accessing HDFS through other interfaces, such as WebHDFS, which is a RESTful web service that exposes HDFS operations over HTTP, or libhdfs, which is a C library that uses JNI to call the Java API.