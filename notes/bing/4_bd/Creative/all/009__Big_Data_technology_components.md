### Big Data technology components

Big Data technology components are the software and hardware tools that enable the processing, storage, analysis, and visualization of large and complex data sets. Some of the main components are:

- **Hadoop**: An open-source framework that allows distributed processing of large data sets across clusters of computers using simple programming models. It consists of four modules: Hadoop Common, Hadoop Distributed File System (HDFS), Hadoop MapReduce, and Hadoop YARN.
  - Hadoop Common: The common utilities that support the other Hadoop modules.
  - Hadoop Distributed File System (HDFS): A distributed file system that provides high-throughput access to data across the Hadoop cluster.
  - Hadoop MapReduce: A programming model and software framework for writing applications that process large amounts of data in parallel on a cluster of nodes.
  - Hadoop YARN: A resource management system that allocates and schedules computing resources for applications running on the Hadoop cluster.
- **Spark**: An open-source cluster computing framework that provides fast and general data processing capabilities. It supports batch processing, streaming processing, machine learning, graph processing, and SQL queries. It can run on Hadoop, Mesos, Kubernetes, or standalone.
  - Spark Core: The foundation of the Spark framework that provides distributed task scheduling, memory management, fault recovery, and basic I/O functionalities.
  - Spark SQL: A module that supports structured and semi-structured data processing and querying using SQL or a DataFrame API.
  - Spark Streaming: A module that supports scalable and fault-tolerant stream processing of live data streams.
  - Spark MLlib: A module that provides scalable machine learning algorithms and utilities.
  - Spark GraphX: A module that supports graph processing and analysis using the GraphX API or the GraphFrames library.
- **Hive**: An open-source data warehouse system that facilitates data summarization, analysis, and querying using a SQL-like language called HiveQL. It runs on top of Hadoop and converts HiveQL queries into MapReduce, Tez, or Spark jobs.
- **Pig**: An open-source platform that provides a high-level language called Pig Latin for data analysis and manipulation. It runs on top of Hadoop and converts Pig Latin scripts into MapReduce, Tez, or Spark jobs.
- **Flume**: An open-source service that collects, aggregates, and moves large amounts of streaming data from various sources to a centralized data store such as HDFS or HBase. It uses a simple and flexible architecture based on streaming data flows.
- **Sqoop**: An open-source tool that transfers bulk data between Hadoop and structured data stores such as relational databases. It uses MapReduce to import and export data in parallel.
- **HBase**: An open-source distributed and scalable non-relational database that provides random, real-time read/write access to large data sets. It is modeled after Google's Bigtable and runs on top of HDFS.
- **Kafka**: An open-source distributed streaming platform that provides high-throughput, low-latency, and fault-tolerant data ingestion and processing. It uses a publish-subscribe model and maintains data in topics that are partitioned and replicated across multiple nodes.
- **Storm**: An open-source distributed real-time computation system that processes unbounded streams of data. It uses a directed acyclic graph (DAG) of spouts and bolts to define the data flow and the processing logic.
- **Zookeeper**: An open-source service that provides centralized coordination and configuration management for distributed systems. It maintains a hierarchical namespace of data nodes that store configuration and status information and enables synchronization, leader election, and group membership services.