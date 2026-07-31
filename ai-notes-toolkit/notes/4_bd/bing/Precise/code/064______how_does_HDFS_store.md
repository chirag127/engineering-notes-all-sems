#### How does HDFS store

Hadoop Distributed File System (HDFS) is a distributed file system designed to store large data sets across multiple machines. HDFS stores data by dividing it into blocks and distributing these blocks across the nodes in the cluster. Each block is typically 128 MB in size and is replicated multiple times (usually 3) across different nodes for fault tolerance. When a file is written to HDFS, the NameNode, which is the master node in the HDFS cluster, determines the location of the data blocks and coordinates the write operation with the DataNodes, which are the worker nodes that store the data blocks. When a file is read from HDFS, the NameNode provides the location of the data blocks to the client, which then reads the data directly from the DataNodes.

Here is an example of how HDFS stores data in Java:

```java
Configuration conf = new Configuration();
conf.set("fs.defaultFS", "hdfs://namenode:8020");
FileSystem fs = FileSystem.get(conf);

Path filePath = new Path("/path/to/file");
FSDataOutputStream outputStream = fs.create(filePath);

outputStream.write("Data to be written to HDFS".getBytes());
outputStream.close();
```

This code creates a `Configuration` object and sets the HDFS URI. It then creates a `FileSystem` object and uses it to create a file in HDFS. The `FSDataOutputStream` object is used to write data to the file, and the stream is closed when the write operation is complete. This code assumes that the HDFS cluster is running and that the client has the necessary permissions to write to the specified path in HDFS.