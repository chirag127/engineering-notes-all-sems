### Hive - Apache Hive architecture and installation

- Apache Hive is an open-source data warehouse system built on Apache Hadoop. It offers a SQL-like query language called HiveQL, which is used to analyze large, structured datasets. The Hive metastore holds metadata about Hive tables, such as their schema and location.
- Hive architecture consists of four main components: Hive clients, Hive services, Processing framework and Resource Management, and Distributed Storage.
  - Hive clients are the interfaces that allow users to interact with Hive, such as Hive shell, Hive web interface, JDBC/ODBC drivers, and HiveServer2.
  - Hive services are the components that provide the core functionality of Hive, such as the compiler, the metastore, the driver, and the execution engine.
  - Processing framework and Resource Management are the components that handle the execution of Hive queries, such as MapReduce, Tez, or Spark, and the allocation of resources, such as YARN or Mesos.
  - Distributed Storage is the component that stores the data for Hive tables, such as HDFS, S3, or Azure Blob Storage.
- To install Hive, you can download a stable release of Hive by downloading and unpacking a tarball, or you can download the source code and build Hive using Maven (release 0.13 and later) or Ant (release 0.12 and earlier) .
  - Hive installation has these requirements: Java 1.7 (preferred). Note: Hive versions 1.2 onward require Java 1.7 or newer. Hive versions 0.14 to 1.1 work with Java 1.6 as well .
  - You also need to have Hadoop installed and configured, as Hive relies on Hadoop for distributed processing and storage.
  - You can follow the steps in the official documentation to install and configure Hive: https://cwiki.apache.org/confluence/display/Hive/AdminManual+Installation