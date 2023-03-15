
#### Data Flow in HDFS

* HDFS stands for Hadoop Distributed File System, a framework used to store and process large datasets.
* HDFS is based on a master-slave architecture, where the master node is known as the NameNode and the slave nodes are known as DataNodes.
* The NameNode is responsible for managing the file system namespace and providing access to the data stored in the DataNodes.
* The DataNodes are responsible for storing the actual data and replicating them across the cluster for fault tolerance.
* Data is stored in HDFS in the form of blocks, with the default block size being 128 MB.
* Data is read from and written to HDFS in the form of a pipeline, which consists of the following steps:
    1. Client applications send read/write requests to the NameNode.
    2. The NameNode determines which DataNode contains the requested data.
    3. The DataNode streams the requested data to the Client application.
    4. The Client application streams the data to the DataNode.
    5. The DataNode stores the data in the form of blocks.
* HDFS provides fault tolerance by replicating the data across multiple DataNodes. The default replication factor is 3, which means that each block of data is stored on 3 different DataNodes.
* HDFS is optimized for streaming large datasets, so it is not suitable for random reads and writes.
* HDFS also provides a mechanism for data integrity, by calculating checksums for each block of data and comparing them with the checksums stored on the DataNodes.
* HDFS is widely used for storing and processing big data in the form of log files, images, videos, etc.