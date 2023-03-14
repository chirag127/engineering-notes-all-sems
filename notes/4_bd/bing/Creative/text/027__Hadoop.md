### Hadoop

Hadoop is an open-source software framework for storing and processing large-scale data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage.  

Hadoop consists of the following core modules:

- Hadoop Common: contains libraries and utilities needed by other Hadoop modules;
- Hadoop Distributed File System (HDFS): a distributed file-system that stores data on commodity machines, providing very high aggregate bandwidth across the cluster;
- Hadoop YARN: a platform responsible for managing computing resources in clusters and using them for scheduling users' applications;  
- Hadoop MapReduce: an implementation of the MapReduce programming model for large-scale data processing.

Hadoop also has an ecosystem of additional software packages that can be installed on top of or alongside Hadoop, such as Apache Pig, Apache Hive, Apache HBase, Apache Phoenix, Apache Spark, Apache ZooKeeper, Apache Impala, Apache Flume, Apache Sqoop, Apache Oozie, and Apache Storm.  

Hadoop is based on the following key principles:

- Data locality: Hadoop moves computation to the data, rather than the other way around, to reduce network traffic and increase performance. 
- Scalability: Hadoop can scale linearly by adding more nodes to the cluster, without requiring any changes to the application logic or data formats.
- Fault tolerance: Hadoop can handle failures at the application layer, by replicating data blocks across multiple nodes and automatically re-executing failed tasks. 
- Flexibility: Hadoop can store and process any kind of data, whether structured, semi-structured, or unstructured, using various formats and schemas.
- Cost-effectiveness: Hadoop can run on commodity hardware, which lowers the cost of ownership and maintenance. 

Hadoop is widely used for various applications, such as:

- Data warehousing and analytics: Hadoop can store and analyze large volumes of historical data, such as web logs, clickstream data, social media data, etc., using tools like Hive, Pig, and Impala.
- Machine learning and data mining: Hadoop can run complex algorithms and models on massive data sets, using tools like Spark, Mahout, and TensorFlow.
- Search and recommendation: Hadoop can index and query large collections of documents, images, videos, etc., using tools like Solr, Lucene, and Nutch.
- Data integration and transformation: Hadoop can extract, transform, and load (ETL) data from various sources and formats, using tools like Flume, Sqoop, and Oozie.
- Data security and governance: Hadoop can protect and manage data access, quality, and lineage, using tools like Ranger, Atlas, and Knox.