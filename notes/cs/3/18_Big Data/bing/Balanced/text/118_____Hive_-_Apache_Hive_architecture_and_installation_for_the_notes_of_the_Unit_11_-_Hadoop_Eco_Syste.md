### Hive - Apache Hive architecture and installation

- Apache Hive is a data warehouse system that facilitates querying and managing large data sets that reside in distributed storage systems, such as Hadoop.
- Hive provides a SQL-like language called HiveQL, which allows users to perform data analysis without writing complex Java MapReduce programs.
- Hive also supports user-defined functions (UDFs), user-defined aggregate functions (UDAFs), and user-defined table functions (UDTFs) to extend its functionality.
- Hive architecture consists of three main components: the Hive client, the Hive server, and the Hive metastore.
  - The Hive client is the interface that allows users to interact with Hive using HiveQL commands or APIs.
  - The Hive server is the component that receives the queries from the Hive client and converts them into MapReduce or Tez jobs that run on the Hadoop cluster.
  - The Hive metastore is the component that stores the metadata of the tables, partitions, columns, and schemas in a relational database.
- Hive installation requires the following prerequisites :
  - Java 1.7 or newer (Hive versions 1.2 and later) or Java 1.6 (Hive versions 0.14 to 1.1)
  - Hadoop 2.x or newer (Hive versions 1.2 and later) or Hadoop 1.x (Hive versions 0.13 and earlier)
  - A relational database for the Hive metastore, such as MySQL, PostgreSQL, Oracle, or Derby 
- Hive installation can be done by downloading a stable release of Hive from one of the Apache download mirrors and unpacking the tarball, or by downloading the source code and building Hive using Maven (release 0.13 and later) or Ant (release 0.12 and earlier) .
- Hive configuration involves setting the environment variables, such as HIVE_HOME, HADOOP_HOME, and JAVA_HOME, and editing the configuration files, such as hive-site.xml, hive-env.sh, and hive-log4j.properties .
- Hive can be run in three modes: local mode, pseudo-distributed mode, and fully-distributed mode .
  - Local mode is the simplest mode, where Hive runs on a single machine and does not use Hadoop .
  - Pseudo-distributed mode is the mode where Hive and Hadoop run on a single machine, but Hadoop runs as a cluster with one node .
  - Fully-distributed mode is the mode where Hive and Hadoop run on a cluster of multiple nodes, and each node performs a specific role, such as master, worker, or edge .
- Hive can be started using the hive command, which launches the Hive shell, or the hiveserver2 command, which launches the Hive server that can accept queries from clients, such as Beeline, JDBC, or ODBC .
- Hive can be stopped using the Ctrl+C command in the Hive shell, or the kill command in the terminal for the Hive server .

: https://cwiki.apache.org/confluence/display/Hive/GettingStarted
: https://cwiki.apache.org/confluence/display/Hive/AdminManual+Installation
: https://www.edureka.co/blog/apache-hive-installation-on-ubuntu
: https://hive.apache.org/
: https://data-flair.training/blogs/apache-hive-architecture/