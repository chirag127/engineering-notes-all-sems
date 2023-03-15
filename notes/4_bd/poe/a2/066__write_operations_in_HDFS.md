 Here is the content in Markdown format with formal tone and without emojis/external links:

#### Write operations in HDFS

1. Client first contacts the NameNode to get the block location for the file.
2. Data is then streamed directly to the DataNodes that contain the blocks.
3. As the data is written, it is buffered at the client/DataNode level to improve throughput.
4. Once a block is filled, it is marked as completed in the NameNode.
5. If there is an error, the NameNode rolls back the file modification to the last known good state.
6. At the end of the write, the file length and modification time is updated in the NameNode.
7. For performance, multiple blocks can be written in parallel. The client determines what blocks to write in parallel.
8. Append operations are supported and work in a similar fashion but only append to existing blocks or allocate new blocks if required.

The above points describe the key steps involved in write operations to HDFS. The interactions with the NameNode to locate blocks and update metadata ensure data consistency and fault tolerance in HDFS.