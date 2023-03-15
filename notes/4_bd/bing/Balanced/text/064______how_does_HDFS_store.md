#### How does HDFS store

- HDFS stands for Hadoop Distributed File System, which is a scalable and fault-tolerant storage system for big data processing.
- HDFS stores data in a distributed manner, by dividing the files into fixed-size blocks (default 128 MB) and storing them on different DataNodes in the cluster.
- DataNodes are the slave nodes that store the actual data blocks and serve read and write requests from the clients.
- NameNode is the master node that maintains the file system namespace and the metadata of all the files and blocks in the cluster. It also manages the replication and placement of blocks across DataNodes.
- HDFS follows a write-once-read-many model, which means that once a file is written, it cannot be modified. However, it can be appended or deleted.
- HDFS provides high availability and reliability by replicating each block on multiple DataNodes (default 3) according to the replication factor. This ensures that the data is not lost even if some DataNodes fail or become inaccessible.
- HDFS also supports rack awareness, which means that it tries to place the replicas of a block on different racks (groups of nodes) to reduce the network bandwidth and increase the fault tolerance.
- HDFS allows users to access the files stored in the cluster through a variety of interfaces, such as the Hadoop command-line, the HDFS Java API, the HDFS REST API, or the HDFS web UI.