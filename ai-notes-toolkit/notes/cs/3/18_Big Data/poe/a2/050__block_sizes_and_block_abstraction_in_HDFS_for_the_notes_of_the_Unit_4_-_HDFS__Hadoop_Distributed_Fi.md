 Here is the formal content written in Markdown format with header sizes and in points on the topic "block sizes and block abstraction in HDFS for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data":

### Block Sizes in HDFS

- HDFS divides files into block of 128MB size by default. This size is configurable.
- The blocks are replicated for fault tolerance. The replication factor is 3 by default but can be changed as per the requirements.
- The blocks are stored on different DataNodes in the cluster for balancing storage across nodes and high availability.
- The size of 128MB was chosen as it is sufficient for most of the applications and efficient in terms of management overhead. Very large block sizes can lead to wastage of space if the file size is small. Very small block sizes can lead to higher overhead in managing numerous blocks.

### Block Abstraction in HDFS

- The blocks in HDFS are abstracted and presented as a single file to the user. The location of blocks and replication is managed by the NameNode.
- The client interacts with the NameNode to get the location of the blocks of the file and then directly reads/writes the blocks from/to the DataNodes.
- This abstraction enables the user to use HDFS just like a regular file system without worrying about the block sizes, locations, replication, etc. The complexity is hidden and handled efficiently by HDFS.

The content is written in formal tone with headers and points as instructed. No emojis or external links are included. The content is written in Markdown format inside the specified header sizes. Please let me know if you would like me to modify or expand the content in any way.