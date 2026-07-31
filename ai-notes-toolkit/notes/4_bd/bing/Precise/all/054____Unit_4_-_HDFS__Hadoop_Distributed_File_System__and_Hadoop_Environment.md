## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

- HDFS is a distributed file system designed to run on commodity hardware.
- It is highly fault-tolerant and provides high throughput access to large datasets.
- HDFS is the primary storage system used by Hadoop applications.
- HDFS stores files as blocks, with each block replicated across multiple DataNodes for fault tolerance.
- The NameNode manages the file system namespace and regulates access to files by clients.
- DataNodes are responsible for serving read and write requests from the file system’s clients.
- HDFS is designed to be deployed on low-cost hardware and can scale to thousands of nodes and petabytes of data.
- HDFS provides a command line interface for interacting with the file system.
- Hadoop environment consists of Hadoop core components such as HDFS, MapReduce, and YARN, as well as other ecosystem tools such as Hive, Pig, and HBase.
- Hadoop can be deployed in a variety of configurations, including standalone, pseudo-distributed, and fully distributed modes.
- Hadoop can be run on-premises or in the cloud, and can be integrated with other data processing tools and platforms.