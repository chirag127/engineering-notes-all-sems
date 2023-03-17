
#### Querying Data in Hive

* Hive is an open source data warehouse system for querying and analyzing large datasets stored in Hadoop's distributed file system (HDFS). 
* HiveQL is a SQL-like language used to query data in Hive.
* Hive uses a directory structure known as a metastore to store table and partition information.
* Hive tables are logically made up of three parts: data, metadata and the schema.
* Data is stored in HDFS as files in a directory structure.
* Metadata is stored in the metastore and is used to define the structure of the data.
* The schema defines the columns and data types of the table, as well as the ordering of the columns.
* Hive queries can be written in HiveQL, a SQL-like language, or through the Hadoop Streaming API.
* Hive queries are translated into a series of MapReduce jobs and then executed on the Hadoop cluster.
* Hive supports a variety of data types, including primitive types (such as int, string, and float) and complex types (such as arrays, maps, and structs).
* Hive also supports user-defined functions (UDFs) and user-defined aggregate functions (UDAFs) for custom processing of data.