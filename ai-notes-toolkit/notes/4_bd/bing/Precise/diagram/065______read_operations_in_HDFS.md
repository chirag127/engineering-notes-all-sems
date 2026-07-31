#### Read operations in HDFS

Here is an ASCII diagram that illustrates the read operations in HDFS:

```
Client
  |
  | 1. Open file
  v
NameNode
  |
  | 2. Return block locations
  v
Client
  |
  | 3. Read data from DataNodes
  v
DataNode(s)
```

1. The client opens a file in HDFS by calling the `open()` method on the `FileSystem` object, which sends a request to the NameNode.
2. The NameNode returns the block locations for the file to the client.
3. The client reads the data from the DataNodes that store the blocks of the file.
