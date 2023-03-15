# Hive - Apache Hive architecture and installation

- Apache Hive is an open-source data warehouse system built on Apache Hadoop.
- Hive offers a SQL-like query language called HiveQL, which is used to analyze large, structured datasets.
- The Hive metastore holds metadata about Hive tables, such as their schema and location.
- Hive supports various file formats, such as text, sequence, RCFile, ORC, Parquet, and Avro.
- Hive can also integrate with other data processing tools, such as Spark, Pig, and MapReduce.

## Hive Architecture

- The Hive architecture consists of four main components:

  - Hive Clients: These are the applications that interact with Hive, such as the Hive shell, the Hive web interface, or the JDBC/ODBC drivers.
  - Hive Services: These are the services that provide the functionality of Hive, such as the HiveServer2, the metastore service, and the webHCat service.
  - Processing Framework and Resource Management: These are the components that execute the Hive queries, such as the MapReduce or Tez engine, and the YARN or Mesos framework.
  - Distributed Storage: This is the component that stores the data for Hive, such as the HDFS or S3 file system.

- The following diagram illustrates the Hive architecture:

![Hive Architecture](https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/09/Hive-Architecture.png)

## Hive Installation

- To install Hive, you need to have the following requirements:

  - Java 1.7 or newer
  - Hadoop 2.x or newer
  - A database for the metastore, such as MySQL, PostgreSQL, or Derby

- You can install a stable release of Hive by downloading and unpacking a tarball, or you can download the source code and build Hive using Maven.
- You can also use a pre-configured Hive environment, such as the one provided by Dataproc, a managed service for running Hadoop and Spark on Google Cloud Platform.
- To configure Hive, you need to set some environment variables, such as HIVE_HOME, HADOOP_HOME, and JAVA_HOME, and edit some configuration files, such as hive-site.xml, hive-env.sh, and hive-log4j.properties.
- To start Hive, you can use the hive command to launch the Hive shell, or the hiveserver2 command to launch the HiveServer2 service, which allows remote clients to connect to Hive using JDBC or ODBC drivers.
- To verify the installation, you can run some sample queries on the default database, such as show tables, describe table_name, and select * from table_name.