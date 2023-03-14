 Here is the content written in markdown format for topic ### HDFS:

### HDFS

HDFS stands for Hadoop Distributed File System. It is the primary storage system used by Hadoop applications. Some key points about HDFS are:

- HDFS is designed for large files (typically GBs to TBs in size). It is not suitable for small files ( KB or MB sized).
- HDFS follows a master-slave architecture. The NameNode is the master that manages the file system namespace and regulates access to files by clients. DataNodes are slaves that store data in blocks and serve read/write requests from clients.
- Data is stored in blocks (typically 128MB in size). Blocks are replicated for fault tolerance. The default replication factor is 3.
- HDFS is highly fault tolerant. It uses replication and checksums to provide high availability and durability. If any DataNode fails or is lost, its blocks can be replicated from other DataNodes.
- HDFS prefers throughput over latency. It is optimized to handle large amounts of data efficiently.

Some key benefits of HDFS are:

- Scalability - HDFS can scale to large clusters with 10s of thousands of nodes
- Fault Tolerance - Data is replicated for high availability
- Low Cost - Commodity hardware can be used
- Streaming Access - Supports high throughput of data access

Some disadvantages of HDFS are:

- Not suitable for low latency data access
- Limited to supporting a fixed number of block sizes
- Single point of failure at the NameNode

Some applications using HDFS are:

- Hadoop MapReduce for running distributed applications
- HBase database
- Hive data warehouse
- Spark processing engine

[You can include diagrams, codes, tables, more points, examples, etc. here if required.]