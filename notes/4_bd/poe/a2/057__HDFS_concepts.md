 Here is the content in markdown format with formal tone and without any emojis or external links:

#### HDFS concepts

1. HDFS stands for Hadoop Distributed File System. It is the primary storage system used by Hadoop applications.

2. HDFS splits files into large blocks (typically 128MB) and stores multiple replicas of the blocks (typically 3) on different nodes in the cluster. This leads to high throughput access to the data.

3. The HDFS architecture consists of a NameNode which manages the file system namespace and regulates access to files by clients. DataNodes store the blocks and serve read/write requests from the clients.

4. The NameNode maintains the file system tree and the metadata for all the files and directories. The DataNodes store the actual data blocks.

5. HDFS provides high fault tolerance via data replication. If a DataNode fails, the data can be retrieved from one of the replicas. The replication factor can be configured as required.

6. HDFS is highly optimized for streaming access of large files. It is not suitable for random/frequent small reads/writes as it leads to inefficiency.

7. HDFS offers scalability and can handle very large data sets and large numbers of client requests concurrently. This makes it ideal for big data applications.

Does this look okay? Let me know if you would like me to modify or add anything.