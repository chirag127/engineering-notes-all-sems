### Hadoop

Here is an ASCII diagram of the Hadoop architecture:

```
          +----------------+
          |                |
          |  Client        |
          |                |
          +-------+--------+
                  |
                  |
                  |
          +-------v--------+
          |                |
          |  NameNode      |
          |                |
          +-------+--------+
                  |
                  |
                  |
          +-------v--------+
          |                |
          |  DataNode      |
          |                |
          +----------------+
```

The diagram shows the basic architecture of Hadoop, which consists of a Client, a NameNode, and a DataNode. The Client communicates with the NameNode to access data stored on the DataNode. The NameNode manages the file system namespace and regulates access to files by clients. The DataNode stores data in the Hadoop Distributed File System (HDFS) and serves read and write requests from the file system's clients.