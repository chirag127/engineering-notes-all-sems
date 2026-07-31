#### Read operations in HDFS

To read a file from HDFS, the client needs to interact with the NameNode, which stores the metadata about the file blocks and their locations on the DataNodes. The NameNode returns a list of DataNodes that have a copy of the requested file block. The client then contacts one of the DataNodes directly and reads the data from it. The client can also read the data from multiple DataNodes in parallel to improve the performance. The following diagram illustrates the read operation in HDFS:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Client       |      |    NameNode     |      |    DataNode     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       | 1. Open file         |                      |
       |--------------------->|                      |
       |                      |                      |
       | 2. Get block list    |                      |
       |<---------------------|                      |
       |                      |                      |
       | 3. Choose DataNode   |                      |
       |---------------------\|                      |
       |                      |                      |
       | 4. Read data         |                      |
       |----------------------|--------------------->|
       |                      |                      |
       | 5. Close file        |                      |
       |<---------------------|<---------------------|
       |                      |                      |
```