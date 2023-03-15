A block in HDFS is a unit of data that is stored as an independent file on the distributed file system. The default block size in HDFS is 128 MB, which can be configured manually by changing the dfs.block.size property in hdfs-site.xml. The block size determines how the data is split and distributed across the cluster. Larger blocks reduce the amount of metadata stored on the namenode and improve the network bandwidth utilization, but they also increase the seek time and the risk of data loss.

A diagram for block sizes in HDFS can be drawn as follows:

#### Block sizes in HDFS

```
+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |
|    Block 1      |    Block 2      |    Block 3      |    Block 4      |    Block 5      |
|                 |                 |                 |                 |                 |
|    128 MB       |    128 MB       |    128 MB       |    128 MB       |     88 MB       |
|                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |                 |
|    File 1       |    File 1       |    File 1       |    File 1       |    File 1       |
|                 |                 |                 |                 |                 |
|    560 MB       |                 |                 |                 |                 |
|                 |                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+-----------------+
```

This diagram shows an example of a file of size 560 MB that is split into five blocks of size 128 MB each, except for the last block which is 88 MB. The blocks are stored as separate files on the HDFS cluster, and the namenode keeps track of their locations and metadata. The file name and the block size are shown below each block. Note that HDFS will use only as much space as needed, so the last block will not occupy 128 MB of disk space, but only 88 MB.