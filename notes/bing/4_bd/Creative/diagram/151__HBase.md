HBase is a column-oriented data storage system that runs on top of HDFS and provides low-latency random access to large amounts of data. HBase has three main components: the client library, the master server, and the region servers. The client library provides the API for interacting with HBase. The master server manages the cluster metadata, such as the table schema, the region assignments, and the load balancing. The region servers host the regions, which are the horizontal partitions of a table. Each region server can serve multiple regions, and each region can store multiple column families. A column family is a logical grouping of columns that share the same compression, encoding, and storage options. Each column family consists of one or more columns, which are identified by a qualifier. Each column can store multiple versions of a value, which are distinguished by a timestamp. A row in HBase is identified by a unique row key, and it can have any number of columns from any column family. HBase stores the data in HDFS as files called HFiles, which are sorted by row key and column. HBase also uses a write-ahead log (WAL) to ensure durability of writes. The WAL records all the changes made to the regions in a region server, and it is also stored in HDFS. HBase also uses ZooKeeper, a distributed coordination service, to maintain the cluster state and handle failover.

The following diagram illustrates the basic architecture of HBase:

### HBase

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Client        |     |   Client        |     |   Client        |
|   Library       |     |   Library       |     |   Library       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   ZooKeeper     |     |   ZooKeeper     |     |   ZooKeeper     |
|   Ensemble      |     |   Ensemble      |     |   Ensemble      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Master        |     |   Master        |     |   Master        |
|   Server        |     |   Server        |     |   Server        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |