Block abstraction in HDFS is a way of dividing a file into fixed-size chunks and storing them across a cluster of DataNodes. The NameNode is responsible for managing the file system namespace and the metadata of the blocks. The block size is usually 64MB-128MB and it is configurable. A file smaller than the block size does not occupy the whole block space. The advantage of having a large block size is to reduce the disk seek time and increase the data transfer rate.

Here is a diagram of block abstraction in HDFS using ASCII characters:

#### Block abstraction in HDFS

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    NameNode     |     |    DataNode 1   |     |    DataNode 2   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  File metadata  |     |  Block 1 (64MB) |     |  Block 2 (64MB) |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Block location |     |  Block 3 (64MB) |     |  Block 4 (64MB) |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  File namespace |     |  Block 5 (64MB) |     |  Block 6 (64MB) |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```