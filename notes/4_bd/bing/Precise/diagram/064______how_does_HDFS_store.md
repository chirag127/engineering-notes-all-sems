Hadoop Distributed File System (HDFS) is a distributed file system designed to store large data sets across multiple machines. Here is an ASCII diagram that shows how HDFS stores data:

```
    +-----------------+     +-----------------+
    | NameNode        |     | DataNode        |
    |                 |     |                 |
    | +-------------+ |     | +-------------+ |
    | | File System | |     | | Block Pool  | |
    | | Namespace   | |     | |             | |
    | +-------------+ |     | +-------------+ |
    |                 |     |                 |
    +-----------------+     +-----------------+
```

In HDFS, data is split into blocks and distributed across multiple DataNodes. The NameNode is responsible for managing the file system namespace and regulating access to files by clients. The DataNodes are responsible for storing the data blocks and serving read and write requests from the clients.

#### How does HDFS store
```
+-----------------+     +-----------------+
| Client          |     | NameNode        |
|                 |     |                 |
|  +-----------+  |     | +-------------+ |
|  | Read/Write|  |     | | File System | |
|  | Request   |  |     | | Namespace   | |
|  +-----+-----+  |     | +------+------+ |
|        |        |     |        |        |
|        |        |     |        |        |
|        v        |     |        v        |
|  +-----+-----+  |     | +------+------+ |
|  | DataNode   |  |     | | Block Map   | |
|  |            |  |     | |             | |
|  +-----------+  |     | +-------------+ |
|                 |     |                 |
+-----------------+     +-----------------+
```

When a client wants to read or write data, it sends a request to the NameNode. The NameNode then returns the location of the data blocks to the client. The client then communicates directly with the DataNodes to read or write the data.
