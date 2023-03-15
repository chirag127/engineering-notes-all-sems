#### Hadoop file system interfaces

- Hadoop has a variety of file systems that can be implemented concretely. 
- The Java abstract class `org.apache.hadoop.fs.FileSystem` represents a file system in Hadoop .
- Hadoop provides numerous interfaces to its various filesystems, and it generally uses the URI scheme to choose the right filesystem instance to communicate with .
- Hadoop is capable of running various file systems and HDFS is just one single implementation .
- Hadoop is written in Java, so most Hadoop filesystem interactions are mediated through the Java API .
- Hadoop provides a command interface to interact with HDFS .
- The built-in servers of namenode and datanode help users to easily check the status of the cluster .
- HDFS is a distributed file system designed to run on commodity hardware .
- HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware .
- Some of the direct known subclasses of `org.apache.hadoop.fs.FileSystem` are `AdlFileSystem`, `FilterFileSystem`, `FTPFileSystem`, `NativeAzureFileSystem`, `NativeS3FileSystem`, `RawLocalFileSystem`, `ViewFileSystem` .