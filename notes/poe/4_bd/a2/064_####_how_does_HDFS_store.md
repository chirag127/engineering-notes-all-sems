 Here is the content in markdown format on how HDFS stores data:

#### How does HDFS store data?

- HDFS stores data in blocks of 128MB (configurable) size. This large block size has following benefits:
- It minimizes the number of blocks needed to store large files, hence reducing the metadata overhead.
- It increases I/O throughput as more data can be read/written in a single disk I/O operation.
- It simplifies the processing of files as most of the files will fit into a single block.

- The blocks of a file are replicated across multiple DataNodes for fault tolerance. The replication factor can be 3 or more (configurable).
- The blocks of a file are placed on DataNodes in a rack-aware manner. This ensures that the replicas are not placed on the same rack so that data is not lost in the event of a rack failure.

- The mapping of blocks to DataNodes is maintained by the NameNode. The client queries the NameNode for block locations whenever it wants to read/write a block.

- HDFS uses a master/slave architecture. The NameNode is the master that manages the file system namespace and regulates access to files by clients. The DataNodes are slaves which store the blocks and serve read/write requests from clients.

- The advantages of HDFS block structure are:
- Fault tolerance via block replication.
- Optimized for large files.
- Low cost as commodity hardware can be used.
- Streaming access of data.

- The disadvantages are:
- Not suitable for small files as the overhead of each block is significant.
- Reduced bandwidth due to replication of blocks.
- Compression not supported as it operates on streams of blocks.

[Include additional details/diagrams/examples/applications/advantages/disadvantages here if helpful for learning.]