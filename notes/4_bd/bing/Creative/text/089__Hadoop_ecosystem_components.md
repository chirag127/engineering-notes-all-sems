#### Hadoop ecosystem components

The Hadoop ecosystem is a collection of tools, libraries, and frameworks that help you build applications on top of Apache Hadoop. Hadoop is a software framework that enables you to store and process large amounts of data on a cluster of computers. Hadoop comprises two distinct parts:

- HDFS (Hadoop Distributed File System): It enables you to store large amounts of data across multiple servers in a distributed manner, so it's easier for you to access it via requests from your clients or applications.
- MapReduce: It enables your computer to process these requests quickly, no matter how large.

The Hadoop ecosystem extends this functionality with additional tools to make it easier to use Hadoop with other frameworks like Spark or Kafka for real-time processing or machine learning tasks. The Hadoop ecosystem architecture is made up of four main components: data storage, data processing, data access, and data management.

Some of the Hadoop ecosystem components are:

- Data Storage: This component includes tools that store and manage data in Hadoop. Some of the tools are:
  - HDFS: Hadoop Distributed File System is the backbone of Hadoop which runs on java language and stores data in Hadoop applications. They act as a command interface to interact with Hadoop. The two components of HDFS are Data node and Name Node.
  - HBase: It is an open-source framework storing all types of data and doesn’t support the SQL database. It is a column-oriented database that runs on top of HDFS and provides random access and strong consistency for large amounts of unstructured and semi-structured data.
  - Sqoop: It is a tool that transfers data between Hadoop and relational databases. It allows users to import data from external sources into Hadoop and export data from Hadoop to external sources.
- Data Processing: This component includes tools that process and analyze data in Hadoop. Some of the tools are:
  - MapReduce: It is a programming model that divides the input into small pieces, distributes them across many machines in the cluster, and combines the output from all machines into one file. It is suitable for batch processing of large and static data.
  - Spark: It is an open-source framework that provides fast and general-purpose cluster computing. It supports multiple languages and can run on top of Hadoop, Mesos, Kubernetes, or standalone. It can perform batch, streaming, interactive, and machine learning tasks.
  - Pig: It is a tool that allows you to write scripts in a language called Pig Latin that can be used to query large datasets stored in HDFS. It can perform data extraction, transformation, and loading (ETL) operations and supports user-defined functions.
- Data Access: This component includes tools that provide access and query data in Hadoop. Some of the tools are:
  - Hive: It is a tool that allows users to store data in tables similar to those already present in SQL databases. It provides a SQL-like interface called HiveQL to query and analyze data stored in HDFS. It can perform data summarization, query, and analysis.
  - Impala: It is a tool that provides fast and interactive SQL queries on data stored in HDFS or HBase. It uses the same metadata and SQL syntax as Hive, but it bypasses MapReduce and directly accesses the data, resulting in faster performance.
  - Presto: It is a tool that provides distributed SQL queries on data stored in HDFS, HBase, Cassandra, MongoDB, and other sources. It supports ANSI SQL and can perform complex analytical queries with low latency.
- Data Management: This component includes tools that manage and monitor the Hadoop cluster and its components. Some of the tools are:
  - YARN: It is a tool that manages the resources and scheduling of the Hadoop cluster. It acts as a central platform that allocates memory, CPU, disk, and network resources to applications running on the cluster. It also supports multiple frameworks such as MapReduce, Spark, and Tez.
  - Zookeeper: It is a tool that provides coordination and synchronization services for distributed applications. It maintains configuration information, naming, and group services for the Hadoop cluster and its components. It also ensures high availability and fault tolerance of the cluster.
  - Oozie: It is a tool that orchestrates and schedules workflows of Hadoop jobs. It allows users to define a sequence of actions that depend on each other and execute them as a single logical unit. It supports various