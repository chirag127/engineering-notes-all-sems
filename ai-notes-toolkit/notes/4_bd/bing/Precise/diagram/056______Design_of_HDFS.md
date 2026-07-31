#### Design of HDFS

HDFS is designed to store and manage very large files across multiple machines. It is based on the principle of data locality, which means that data is stored on the same machine where it is processed. Here is an ASCII diagram of the design of HDFS:

```
+----------------+     +----------------+
| NameNode       |     | DataNode       |
| (Master)       |     | (Worker)       |
|                |     |                |
| +------------+ |     | +------------+ |
| | Filesystem | |     | | Block      | |
| | Namespace  | |     | | Server     | |
| +------------+ |     | +------------+ |
|                |     |                |
| +------------+ |     | +------------+ |
| | Block      | |     | | Data       | |
| | Management | |     | | Management | |
| +------------+ |     | +------------+ |
+----------------+     +----------------+
```

The NameNode is the master server that manages the file system namespace and regulates access to files by clients. The DataNodes are worker nodes that store and manage the data blocks. The NameNode and DataNodes communicate with each other to ensure that data is stored and retrieved reliably.
