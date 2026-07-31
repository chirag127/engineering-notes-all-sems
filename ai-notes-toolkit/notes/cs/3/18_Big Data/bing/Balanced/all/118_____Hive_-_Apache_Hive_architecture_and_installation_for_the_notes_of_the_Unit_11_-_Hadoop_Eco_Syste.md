# Hive - Apache Hive architecture and installation

## Introduction

- Hive is a data warehouse system built on top of Hadoop that allows users to query and analyze large, structured datasets using a SQL-like language called HiveQL.
- Hive provides a schema-on-read approach, which means that the data is not validated or transformed when it is loaded into Hive, but only when it is queried.
- Hive also supports user-defined functions (UDFs), user-defined aggregate functions (UDAFs), and user-defined table functions (UDTFs) to extend its functionality and express complex logic.

## Architecture

- The main components of Hive architecture are:

  - Hive clients: These are the applications or tools that interact with Hive, such as Hive shell, Hive web interface, JDBC/ODBC drivers, or Hive Thrift server.
  - Hive services: These are the components that provide the core functionality of Hive, such as:
    - Hive metastore: This is a repository that stores metadata about Hive tables, such as their schema, location, partitioning, and serialization/deserialization properties. The metastore can be configured to use different backends, such as Derby, MySQL, PostgreSQL, or Oracle.
    - Hive driver: This is the component that receives the HiveQL queries from the clients, compiles them into an execution plan, and submits them to the processing framework.
    - Hive compiler: This is the component that parses the HiveQL queries, performs semantic analysis, and generates an abstract syntax tree (AST) that represents the query logic.
    - Hive optimizer: This is the component that applies various optimizations to the AST, such as predicate pushdown, column pruning, join reordering, and map-side aggregation.
    - Hive executor: This is the component that executes the optimized plan using the processing framework and returns the results to the driver.
  - Processing framework: This is the component that provides the distributed execution engine for Hive queries, such as MapReduce, Tez, or Spark.
  - Resource management: This is the component that allocates and manages the resources for the processing framework, such as YARN or Mesos.
  - Distributed storage: This is the component that stores the data for Hive tables, such as HDFS, S3, or Azure Blob Storage.

## Installation

- To install Hive, you can either download a stable release of Hive from the official website and unpack it, or you can download the source code and build it using Maven or Ant.
- Hive installation has the following requirements:
  - Java 1.7 or newer (Hive versions 1.2 onward require Java 1.7 or newer, while Hive versions 0.14 to 1.1 work with Java 1.6 as well)
  - Hadoop 2.x or newer (Hive versions 2.0 onward require Hadoop 2.x or newer, while Hive versions 0.14 to 1.2 work with Hadoop 1.x as well)
  - A metastore backend, such as Derby (default), MySQL, PostgreSQL, or Oracle
- To configure Hive, you need to edit the following files in the conf directory of the Hive installation:
  - hive-site.xml: This is the main configuration file that contains the properties for Hive services, such as the metastore URI, the processing framework, the resource manager, and the distributed storage.
  - hive-env.sh: This is the shell script that sets the environment variables for Hive, such as the Java home, the Hadoop home, and the Hive classpath.
  - hive-log4j.properties: This is the configuration file that sets the logging options for Hive, such as the log level, the log file, and the log format.
- To start Hive, you can use the following commands in the bin directory of the Hive installation:
  - hive: This launches the Hive shell, which is a command-line interface that allows you to enter and execute HiveQL queries interactively.
  - hiveserver2: This starts the Hive server, which is a service that allows remote clients to connect to Hive using JDBC/ODBC drivers or Thrift protocol.
  - beeline: This launches the Beeline shell, which is a JDBC client that allows you to connect to the Hive server and execute HiveQL queries interactively.