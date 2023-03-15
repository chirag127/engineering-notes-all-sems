## Unit 4 - HDFS (Hadoop Distributed File System)

HDFS is a distributed file system that handles large data sets running on commodity hardware. It is used to scale a single Apache Hadoop cluster to hundreds (and even thousands) of nodes. HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN.

Some of the key features and benefits of HDFS are:

- **Fault-tolerance**: HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware. It can automatically detect and handle failures of nodes, disks, and network. It can also replicate data blocks across multiple nodes to ensure data availability and reliability.
- **Scalability**: HDFS can scale up to store and process petabytes or exabytes of data across thousands of nodes. It can also scale down to run on a single node for testing or development purposes. HDFS can support concurrent access by multiple clients and applications.
- **High-throughput**: HDFS can provide high-throughput access to data by optimizing the data transfer bandwidth and minimizing the disk seek time. It can also support streaming read and write operations, which are suitable for batch processing and analytics.
- **Compatibility**: HDFS can work with different types of data, such as structured, semi-structured, or unstructured data. It can also integrate with various tools and frameworks, such as Spark, Hive, Pig, HBase, and Kafka, to enable diverse data processing and analysis.
- **Simplicity**: HDFS has a simple and intuitive architecture that consists of two types of nodes: NameNode and DataNode. The NameNode is the master node that manages the metadata and namespace of the file system, while the DataNodes are the worker nodes that store and serve the data blocks. The clients can interact with the NameNode to perform operations such as creating, deleting, or renaming files or directories, and with the DataNodes to read or write data blocks.

: https://www.ibm.com/topics/hdfs
: https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html
: https://www.techtarget.com/searchdatamanagement/definition/Hadoop-Distributed-File-System-HDFS