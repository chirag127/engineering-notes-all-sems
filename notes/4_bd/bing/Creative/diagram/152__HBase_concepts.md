HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). It provides fast and random access to large amounts of structured data. It is based on the Google Bigtable data model and uses the Hadoop ecosystem components such as ZooKeeper, MapReduce, and Hive for coordination, processing, and querying.

#### HBase concepts

The following diagram illustrates the basic architecture and concepts of HBase using ASCII art.

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    HBase        |     |    HBase        |     |    HBase        |
|    Master       |     |    Master       |     |    Master       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    ZooKeeper    |     |    ZooKeeper    |     |    ZooKeeper    |
|    Quorum       |     |    Quorum       |     |    Quorum       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
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
|    HBase        |     |    HBase        |     |    HBase        |
|    Region       |     |    Region       |     |    Region       |
|    Server 1     |     |    Server 2     |     |    Server 3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    HBase        |     |    HBase        |     |    HBase        |
|    Region       |     |    Region       |     |    Region       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    HBase        |     |    HBase        |     |    HBase        |
|    Store        |     |    Store        |     |    Store        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +