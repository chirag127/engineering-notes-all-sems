 Here is the content in markdown format with points, without emojis or external links and in a formal tone:

#### Block Abstraction in HDFS

1. HDFS stores data in blocks of 128MB (configurable) size. This is the block size abstraction in HDFS.
2. A file is split into multiple blocks and each block is stored as an independent unit. This enables HDFS to read/write data in parallel thus increasing throughput.
3. Blocks are replicated for fault tolerance. The default replication factor is 3. This means for each block of data, there are 2 additional replica blocks stored on different DataNodes.
4. The NameNode keeps metadata of the blocks (block locations, block sizes, etc) but not the actual block data. The block data is stored on the DataNodes.
5. When reading a file, the NameNode provides the block locations to the application. The application can then read the multiple blocks in parallel, increasing read throughput.
6. When writing a file, the NameNode determines block locations and the client writes data directly to the DataNodes.
7. The block abstraction enables HDFS scalability, throughput and fault tolerance. The default 128MB block size was chosen as a size large enough to achieve high throughput (less metadata overhead) but small enough to minimize data loss in case of a block corruption (lost data can be replicated from other replicas).

How's that? I have written the points in a formal tone without any emojis or external links and have formatted the content in markdown within the specified header block. Please let me know if any changes are needed.