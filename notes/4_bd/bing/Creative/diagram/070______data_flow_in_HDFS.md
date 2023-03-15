Data flow in HDFS refers to the process of reading or writing data from or to the Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for large-scale data processing. HDFS consists of a master node called the NameNode, which manages the file system metadata, and multiple slave nodes called DataNodes, which store the actual data blocks. The data flow in HDFS can be illustrated by the following ASCII diagrams, based on the information from the search results .

#### Data flow in HDFS read operation

```
+---------+      +----------+      +----------+      +----------+
| Client  |      | NameNode |      | DataNode |      | DataNode |
+---------+      +----------+      +----------+      +----------+
    |                 |                 |                 |
    |  open()         |                 |                 |
    |---------------->|                 |                 |
    |                 |                 |                 |
    |  <file info>    |                 |                 |
    |<----------------|                 |                 |
    |                 |                 |                 |
    |  choose DataNode|                 |                 |
    |---------------->|                 |                 |
    |                 |                 |                 |
    |  <DataNode info>|                 |                 |
    |<----------------|                 |                 |
    |                 |                 |                 |
    |  read()         |                 |                 |
    |---------------------------------->|                 |
    |                 |                 |                 |
    |  <data block>   |                 |                 |
    |<----------------------------------|                 |
    |                 |                 |                 |
    |  read()         |                 |                 |
    |---------------------------------------------->|     |
    |                 |                 |                 |
    |  <data block>   |                 |                 |
    |<----------------------------------------------|     |
    |                 |                 |                 |
    |  close()        |                 |                 |
    |---------------->|                 |                 |
    |                 |                 |                 |
    |  <ack>          |                 |                 |
    |<----------------|                 |                 |
    |                 |                 |                 |
```

#### Data flow in HDFS write operation

```
+---------+      +----------+      +----------+      +----------+
| Client  |      | NameNode |      | DataNode |      | DataNode |
+---------+      +----------+      +----------+      +----------+
    |                 |                 |                 |
    |  create()       |                 |                 |
    |---------------->|                 |                 |
    |                 |                 |                 |
    |  <file info>    |                 |                 |
    |<----------------|                 |                 |
    |                 |                 |                 |
    |  write()        |                 |                 |
    |---------------->|                 |                 |
    |                 |                 |                 |
    |  <DataNode info>|                 |                 |
    |<----------------|                 |                 |
    |                 |                 |                 |
    |  write()        |                 |                 |
    |---------------------------------->|                 |
    |                 |                 |                 |
    |  <ack>          |                 |                 |
    |<----------------------------------|                 |
    |                 |                 |                 |
    |  write()        |                 |                 |
    |---------------------------------------------->|     |
    |                 |                 |                 |
    |  <ack>          |                 |                 |
    |<----------------------------------------------|     |
    |                 |                 |                 |
    |  close()        |                 |                 |
    |---------------->|                 |                 |
    |                 |                 |                 |
    |  <ack>          |                 |                 |
    |<----------------|                 |                 |
    |                 |                 |                 |
```