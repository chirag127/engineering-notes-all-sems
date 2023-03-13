Block abstraction in HDFS is a way of dividing a file into fixed-size chunks, which are stored as independent units across a cluster of DataNodes. The default block size in HDFS is 64 MB or 128 MB, which is much larger than the typical block size in other file systems. The advantage of having a large block size is to reduce the disk seek time and improve the data transfer rate. A file smaller than the block size does not occupy the whole block, but only the actual size of the file.

The following diagram illustrates the basic architecture of a block abstraction in HDFS:

#### Block abstraction in HDFS

```
+-----------------+    +-----------------+    +-----------------+
| NameNode        |    | DataNode 1      |    | DataNode 2      |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | File1       | |    | | Block1      | |    | | Block2      | |
| | 128 MB      | |    | | 64 MB       | |    | | 64 MB       | |
| | Block1,2    | |    | +-------------+ |    | +-------------+ |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| +-------------+ |    | | Block3      | |    | | Block4      | |
| | File2       | |    | | 64 MB       | |    | | 64 MB       | |
| | 64 MB       | |    | +-------------+ |    | +-------------+ |
| | Block3      | |    | +-------------+ |    | +-------------+ |
| +-------------+ |    | | Block5      | |    | | Block6      | |
| +-------------+ |    | | 32 MB       | |    | | 32 MB       | |
| | File3       | |    | +-------------+ |    | +-------------+ |
| | 64 MB       | |    |                 |    |                 |
| | Block4,5,6  | |    |                 |    |                 |
| +-------------+ |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

In this diagram, the NameNode is the master node that manages the file system namespace and the metadata of the files and blocks. The DataNodes are the slave nodes that store the actual data blocks and report to the NameNode periodically. The NameNode keeps track of which blocks belong to which file and where they are located in the cluster. The DataNodes are responsible for serving read and write requests from the clients and performing block creation, deletion, and replication as instructed by the NameNode.

As an example, File1 is a 128 MB file that is split into two 64 MB blocks, Block1 and Block2. These blocks are stored in DataNode 1 and DataNode 2 respectively. File2 is a 64 MB file that is stored as a single block, Block3, in DataNode 1. File3 is a 64 MB file that is split into three blocks, Block4, Block5, and Block6, each of 32 MB. These blocks are stored in DataNode 2, DataNode 1, and DataNode 2 respectively. The NameNode knows the location and size of each block and file, and can direct the clients to the appropriate DataNodes for accessing the data.