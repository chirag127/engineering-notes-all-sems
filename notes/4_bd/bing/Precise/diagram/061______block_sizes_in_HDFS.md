#### Block sizes in HDFS

Hadoop Distributed File System (HDFS) is a distributed file system designed to store large files across multiple machines. HDFS stores files as blocks, and the default block size is 128 MB. Here is an ASCII diagram that illustrates how a file is split into blocks in HDFS:

```
+----------------+----------------+----------------+----------------+
|                |                |                |                |
|   Block 1      |   Block 2      |   Block 3      |   Block 4      |
|  (128 MB)      |  (128 MB)      |  (128 MB)      |  (128 MB)      |
|                |                |                |                |
+----------------+----------------+----------------+----------------+
```

Each block is stored on a different DataNode in the HDFS cluster. The NameNode keeps track of the location of each block and coordinates access to the file data.
