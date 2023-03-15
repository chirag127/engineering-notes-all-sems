A block in HDFS is a fixed-size unit of data that is stored on one or more nodes in a cluster. The default block size in HDFS is 128 MB, but it can be configured manually by changing the dfs.block.size property in hdfs-site.xml. HDFS distributes the blocks of a file across different nodes, and the master node (NameNode) stores the metadata about the block locations. The block size and replication factor are configurable per file. All blocks in a file except the last block are the same size, while the last block can be smaller than the configured block size.

Here is a diagram of how blocks are stored in HDFS:

#### Block sizes in HDFS

```
+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |
|    Block 1      |    Block 2      |    Block 3      |    Block 4      |    Block 5      |
|                 |                 |                 |                 |                 |
|   128 MB        |   128 MB        |   128 MB        |   128 MB        |   88 MB         |
|                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |
|   File A        |   File A        |   File A        |   File A        |   File A        |
|                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |
|   Node 1        |   Node 2        |   Node 3        |   Node 4        |   Node 5        |
|                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+
```