### Hadoop file system interfaces

- Hadoop provides a Java abstract class `org.apache.hadoop.fs.FileSystem` that represents the client interface to a file system in Hadoop  .
- Hadoop supports various file systems that can be implemented concretely, such as HDFS, S3, FTP, Azure, etc  .
- Hadoop uses the URI scheme to select the appropriate file system instance to communicate with, such as `hdfs://`, `s3://`, `ftp://`, etc .
- Hadoop also provides a command interface to interact with HDFS, such as `hadoop fs -ls`, `hadoop fs -put`, `hadoop fs -get`, etc.
- Hadoop file system interfaces allow streaming access to file system data, such as reading and writing files in blocks .
- Hadoop file system interfaces support fault tolerance, scalability, and high availability, by replicating data blocks across multiple nodes and handling failures gracefully.