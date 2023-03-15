### HDFS (Hadoop Distributed File System) Notes

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN.
- HDFS exposes a file system namespace and enables user data to be stored in files.
- A file is split into one or more blocks that are stored in a set of DataNodes.
- The NameNode performs file system namespace operations, including opening, closing and renaming files and directories.
- HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware .
- HDFS provides high throughput access to application data and is suitable for applications that have large data sets .
- HDFS relaxes a few POSIX requirements to enable streaming access to file system data .
- HDFS follows a master/slave architecture, where the NameNode is the master and the DataNodes are the slaves .
- HDFS supports a single namespace for the entire cluster, which is maintained by the NameNode .
- HDFS supports a write-once-read-many model, where a file once created, written and closed, cannot be changed .
- HDFS supports replication of data blocks across multiple DataNodes for fault tolerance and reliability .
- HDFS supports rack-awareness, where the NameNode can choose DataNodes based on their rack location to improve network bandwidth and data locality .
- HDFS supports a command-line interface and a web-based interface for users and administrators to interact with the file system .
- HDFS supports a Java API and a REST API for application developers to access the file system programmatically .