## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

- HDFS is a distributed file system that handles large data sets running on commodity hardware. It is used to scale a single Apache Hadoop cluster to hundreds (and even thousands) of nodes.
- HDFS is one of the major components of Apache Hadoop, the others being MapReduce and YARN. HDFS should not be confused with or replaced by Apache HBase, which is a column-oriented non-relational database management system that sits on top of HDFS and can better support real-time data needs with its in-memory processing engine.
- HDFS provides fault-tolerance and high availability to the storage layer and the other devices present in that Hadoop cluster. HDFS is capable of handling larger size data with high volume velocity and variety makes Hadoop work more efficient and reliable with easy access to all its components.
- HDFS consists of two core components: a NameNode that manages the file system metadata and DataNodes that store the actual data. Clients contact NameNode for file metadata or file modifications and perform actual file I/O directly with the DataNodes.
- HDFS has been built to detect faults and automatically recover quickly. HDFS is intended more for batch processing versus interactive use, so the emphasis in the design is for high data throughput rates, which accommodate streaming access to data sets.
- HDFS provides high aggregate data bandwidth and can scale to hundreds of nodes in a single cluster. To facilitate adoption, HDFS is designed to be portable across multiple hardware platforms and to be compatible with a variety of underlying operating systems.
- HDFS supports shell-like commands to interact with HDFS directly. The NameNode and Datanodes have built in web servers that makes it easy to check current status of the cluster.
- HDFS also supports file permissions and authentication, rack awareness, safemode, fsck, fetchdt, balancer, upgrade and rollback, secondary NameNode, checkpoint node, backup node, import checkpoint, recovery mode, and DataNode hot swap drive.
- HDFS is vulnerable to various form of attack, such as the DoS attack, which accomplished by causing a crash of data or flooding the target with traffic. Name Node in HDFS is vulnerable to DoS attacks.
- HDFS is part of the Hadoop ecosystem, which includes other components such as Hive, Pig, Spark, HBase, Sqoop, Flume, Kafka, ZooKeeper, Oozie, and Mahout. These components provide various functionalities such as data processing, data analysis, data ingestion, data management, data orchestration, and machine learning on top of HDFS.

Some mnemonics and learning tricks for HDFS and Hadoop Environment are:

- HDFS: High Data For Storage
- NameNode: Names the files and nodes
- DataNode: Stores the data in blocks
- HBase: Hadoop + Database
- YARN: Yet Another Resource Negotiator
- Sqoop: SQL + Hadoop
- Flume: Flows data into Hadoop
- Kafka: Streams data like a coffee maker
- ZooKeeper: Keeps the cluster in sync
- Oozie: Makes workflows easy
- Mahout: Machine learning with Hadoop