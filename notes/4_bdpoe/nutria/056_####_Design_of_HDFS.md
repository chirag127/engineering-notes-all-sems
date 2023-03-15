
#### Design of HDFS

- HDFS stands for Hadoop Distributed File System. It is a distributed file system designed to run on commodity hardware.
- HDFS has a master/slave architecture with a single NameNode as the master server and multiple DataNodes as the slave servers.
- The NameNode is responsible for storing the file system metadata such as the directory tree and file-block mapping.
- The DataNodes are responsible for storing the actual data blocks of the files.
- HDFS is designed to be fault tolerant, meaning that it can continue to operate even if one or more of its components fail.
- HDFS is also designed to be highly scalable, meaning that it can easily handle large amounts of data.
- HDFS supports high throughput access to data, allowing applications to access large amounts of data quickly.
- HDFS also supports data replication, meaning that data can be stored in multiple copies across the cluster to provide redundancy and fault tolerance.
- HDFS also supports data compression, meaning that data can be compressed before being stored on the cluster, which can help to reduce storage costs.
- HDFS also supports snapshotting, meaning that the file system can be quickly backed up and restored in the event of a failure.
- HDFS also supports data security, meaning that data can be encrypted before being stored on the cluster, which can help to protect it from unauthorized access.