#### Apache Hive architecture

Apache Hive is a data warehouse system that enables analytics at a massive scale on top of Hadoop. It provides a SQL-like query language called HiveQL that can process structured and semi-structured data. Hive also supports user-defined functions and custom data formats.

The main components of Apache Hive architecture are:

- **Hive clients**: These are the interfaces that allow users and applications to interact with Hive. They include the Hive command line (CLI), the Hive web interface (HWI), the Hive Beeline shell, and the Hive JDBC/ODBC drivers.
- **Hive services**: These are the components that process the queries and manage the metadata. They include the Hive server 2 (HS2), the Hive metastore (HMS), and the Hive compiler and execution engine.
- **Processing framework and resource management**: These are the components that handle the distributed processing and scheduling of the queries. They include the Hadoop MapReduce or Tez framework, and the YARN or Mesos resource manager.
- **Distributed storage**: This is the component that stores the data and metadata. It includes the Hadoop Distributed File System (HDFS) or other compatible file systems.