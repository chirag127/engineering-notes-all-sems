# Hive - Apache Hive architecture and installation

- Hive is a data warehouse system built on top of Hadoop that allows users to query and analyze large, structured datasets using a SQL-like language called HiveQL.
- Hive has a client-server architecture that consists of the following components:

  - Hive clients: These are the applications that interact with Hive, such as the Hive shell, the Hive web interface, or the Hive JDBC/ODBC drivers. They send queries and commands to the Hive server and receive the results.
  - Hive server: This is the main component of Hive that handles the requests from the clients. It consists of two services: the Hive metastore and the HiveServer2.
    - Hive metastore: This is a service that stores the metadata of the Hive tables, such as their schema, location, partitions, etc. It also communicates with the Hadoop NameNode to access the HDFS files. The metastore can use different backends to store the metadata, such as Derby, MySQL, PostgreSQL, etc.
    - HiveServer2: This is a service that provides a JDBC/ODBC interface for the clients to execute HiveQL statements. It also supports a Thrift API for programmatic access. HiveServer2 parses, compiles, optimizes, and executes the HiveQL queries using the Hadoop MapReduce or Tez framework. It also interacts with the metastore to get the metadata information.
  - Processing framework and resource management: This is the layer that performs the actual data processing and resource allocation for the Hive queries. Hive supports two processing frameworks: MapReduce and Tez. MapReduce is the default framework that runs the queries as a series of map and reduce tasks. Tez is an alternative framework that runs the queries as a directed acyclic graph (DAG) of tasks, which can improve the performance and scalability of complex queries. Hive also supports two resource management systems: YARN and Mesos. YARN is the default system that manages the resources and scheduling of the Hadoop cluster. Mesos is an alternative system that can run multiple frameworks on the same cluster, such as Hadoop, Spark, etc.
  - Distributed storage: This is the layer that stores the actual data of the Hive tables. Hive uses the Hadoop Distributed File System (HDFS) as the default storage system, which provides high availability, scalability, and fault tolerance. Hive can also use other storage systems, such as Amazon S3, Google Cloud Storage, etc.

- To install Hive, you need to have the following requirements:

  - Java 1.7 or newer (Hive versions 1.2 onward require Java 1.7 or newer, while Hive versions 0.14 to 1.1 work with Java 1.6 as well)
  - Hadoop 2.x or newer (Hive supports Hadoop 3.x since version 3.0)
  - A relational database for the metastore backend (such as Derby, MySQL, PostgreSQL, etc.)

- The steps to install Hive are:

  - Download a stable release of Hive from the Apache website or the source code from the GitHub repository.
  - Unpack the tarball or build the source code using Maven (release 0.13 and later) or Ant (release 0.12 and earlier).
  - Set the environment variables HIVE_HOME and HADOOP_HOME to point to the Hive and Hadoop directories, respectively.
  - Configure the hive-site.xml file in the conf directory to specify the parameters for the Hive server, such as the metastore backend, the processing framework, the resource management system, etc.
  - Initialize the metastore schema using the schematool command with the -initSchema option and the appropriate database type (such as derby, mysql, postgres, etc.).
  - Start the Hive server using the hive --service hiveserver2 command.
  - Connect to the Hive server using the Hive shell (hive), the Hive web interface (http://localhost:10002), or the Hive JDBC/ODBC drivers.