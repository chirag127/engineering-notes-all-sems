HDFS is a distributed file system that runs on clusters of commodity hardware and is designed for storing very large files with streaming data access patterns  . It is based on the Google File System and is a member of the Hadoop Ecosystem. HDFS has a master-slave architecture, where a single NameNode manages the namespace and metadata of the file system, and multiple DataNodes store the actual data blocks of the files . HDFS provides high throughput, fault tolerance, scalability, and data locality for applications that process large amounts of data.

#### Design of HDFS

The following diagram illustrates the basic architecture of HDFS using ASCII characters:

```
+-----------------+             +-----------------+
|                 |             |                 |
|    Client       |             |    Client       |
|                 |             |                 |
+-----------------+             +-----------------+
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
+-----------------+             +-----------------+
|                 |             |                 |
|    NameNode     |             |    DataNode     |
|                 |             |                 |
+-----------------+             +-----------------+
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |
        |                 |             |
        +-----------------+             |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |
        |                 |             |
        +-----------------+             |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |
        |                 |             |
        +-----------------+             |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |
        |                 |             |
        +-----------------+             |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |
        |                 |             |
        +-----------------+             |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |
        |                 |             |
        +-----------------+             |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |
        |                 |             |
        +-----------------+             |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |
        |                 |             |
        +-----------------+             |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        +-----------------+             |
        |                 |             |
        |    DataNode     |             |