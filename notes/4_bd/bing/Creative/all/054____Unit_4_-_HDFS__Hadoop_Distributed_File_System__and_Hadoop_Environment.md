# Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

- HDFS is a distributed file system that handles large data sets running on commodity hardware.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN.
- HDFS provides high throughput access to application data, high availability, fault tolerance, and scalability .
- HDFS has a master-slave architecture, where the master node is called the NameNode and the slave nodes are called the DataNodes.
- The NameNode manages the file system namespace, the metadata, and the access control.
- The DataNodes store the actual data blocks and perform read and write operations as instructed by the NameNode.
- HDFS follows a write-once-read-many model, where files are split into fixed-size blocks (default 64 MB) and distributed across the DataNodes.
- HDFS maintains multiple replicas of each block for fault tolerance and load balancing.
- HDFS supports a command-line interface, a web interface, and a Java API for interacting with the file system.
- Hadoop is an open source framework that can store, process, and analyze large volumes of data using HDFS, MapReduce, and YARN .
- Hadoop is designed to run on clusters of commodity hardware, where each node can perform both storage and computation tasks.
- Hadoop supports various programming languages, such as Java, Python, Scala, and R, and various data formats, such as text, binary, JSON, and XML.
- Hadoop also provides a rich ecosystem of tools and applications for data ingestion, transformation, analysis, and visualization, such as Hive, Pig, Spark, HBase, Sqoop, Flume, and Oozie.