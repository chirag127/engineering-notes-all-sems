#### HDFS concepts

Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It is used to scale a single Apache Hadoop cluster to hundreds (and even thousands) of nodes . HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN .

HDFS is a block-structured file system. Each HDFS file is broken into blocks of fixed size, usually 128 MB, which are stored across various data nodes on the cluster . HDFS is designed to store vast amounts of data on low-cost commodity hardware while ensuring high-speed processing of data . Its design is based on the design of the Google File System and its notion is "Write Once, Read Multiple times" .

Important components in HDFS architecture are:
- **Blocks**: HDFS is a block-structured file system .
- **Name Node**: The Name Node is the centerpiece of an HDFS file system. It keeps the directory tree of all files in the file system, and tracks where across the cluster the file data is kept .
- **Data Nodes**: Data Nodes are responsible for storing the data blocks of files .

HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware . It is mainly designed for working on commodity hardware devices, working on a distributed file system design .