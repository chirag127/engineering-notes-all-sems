Write operations in HDFS involve the following steps:

1. The client contacts the NameNode and requests to create a new file in the HDFS namespace.
2. The NameNode checks if the file already exists or if the client has the permission to write the file. If not, it throws an exception to the client.
3. The NameNode returns a list of DataNodes that can host the replicas of the first block of the file to the client.
4. The client caches the list of DataNodes and writes the first block of the file to the first DataNode in the list using a TCP connection.
5. The first DataNode starts replicating the block to the second DataNode in the list, which in turn replicates it to the third DataNode, and so on. This forms a pipeline of DataNodes for each block.
6. When the first block is written, the client requests the NameNode for a new list of DataNodes for the second block, and repeats the same process until all the blocks of the file are written.
7. The client finalizes the file creation by calling close() on the output stream, which flushes the remaining packets to the DataNodes and notifies the NameNode.

The following diagram illustrates the basic architecture of a write operation in HDFS:

```
    +-----------+    create()    +----------+
    |   Client  | -------------> | NameNode |
    +-----------+                +----------+
         |                           |
         |    list of DataNodes     |
         |<--------------------------|
         |                           |
         |    write block 1         |
         |----------------------->  |  +-----------+
         |                          |  | DataNode1 |
         |                          |  +-----------+
         |                          |         |
         |                          |         |  replicate block 1
         |                          |         |----------------->  +-----------+
         |                          |                            | DataNode2 |
         |                          |                            +-----------+
         |                          |                                   |
         |                          |                                   |  replicate block 1
         |                          |                                   |----------------->  +-----------+
         |                          |                                                            | DataNode3 |
         |                          |                                                            +-----------+
         |                           |
         |    write block 2         |
         |----------------------->  |  +-----------+
         |                          |  | DataNode4 |
         |                          |  +-----------+
         |                          |         |
         |                          |         |  replicate block 2
         |                          |         |----------------->  +-----------+
         |                          |                            | DataNode5 |
         |                          |                            +-----------+
         |                          |                                   |
         |                          |                                   |  replicate block 2
         |                          |                                   |----------------->  +-----------+
         |                          |                                                            | DataNode6 |
         |                          |                                                            +-----------+
         |                           |
         |    close()               |
         |----------------------->  |  +-----------+
         |                          |  | DataNode1 |
         |                          |  +-----------+
         |                          |         |
         |                          |         |  notify NameNode
         |                          |         |----------------->  +----------+
         |                          |                            | NameNode |
         |                          |                            +----------+
         |                          |                                   |
         |                          |                                   |  update namespace
         |                          |                                   |----------------->  +----------+
         |                          |                                                            | NameNode |
         |                          |                                                            +----------+
         |                           |
         |    file created          |
         |<--------------------------|
         |                           |
         V                           V
```