#### Data flow in HDFS

HDFS is a distributed file system that stores data in blocks across multiple nodes in a cluster. The data flow in HDFS involves the following steps:

1. The client contacts the NameNode and requests to read a file. The NameNode checks the file permissions and returns the locations of the blocks that make up the file. The locations are ordered by their proximity to the client.
2. The client contacts the closest DataNode that has a copy of the first block of the file. The DataNode transfers the block data to the client.
3. The client reads the data from the block and then contacts the next DataNode that has a copy of the next block of the file. The process repeats until the client has read all the blocks of the file.
4. The client closes the file and notifies the NameNode.

The following diagram illustrates the data flow in HDFS using ASCII characters:

```
    +----------+     +----------+     +----------+
    | Client   |     | NameNode |     | DataNode |
    +----------+     +----------+     +----------+
         |                |                |
         | open(file)     |                |
         |--------------->|                |
         |                |                |
         | block locations|                |
         |<---------------|                |
         |                |                |
         | read(block1)   |                |
         |------------------------------>   |
         |                |                |
         | block data     |                |
         |<------------------------------   |
         |                |                |
         | read(block2)   |                |
         |------------------------------>   |
         |                |                |
         | block data     |                |
         |<------------------------------   |
         |                |                |
         | ...            |                |
         | ...            |                |
         | ...            |                |
         |                |                |
         | close(file)    |                |
         |--------------->|                |
         |                |                |
         |                |                |
```