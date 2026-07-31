# Hive - Apache Hive architecture and installation

Apache Hive is a data warehousing and SQL-like query language for Hadoop. It facilitates reading, writing, and managing large datasets residing in distributed storage using SQL. Hive provides a mechanism to project structure onto this data and query the data using a SQL-like language called HiveQL.

## Architecture

The architecture of Hive consists of the following components:

1. **Hive Clients**: These are the interfaces that allow users to interact with Hive, such as the Hive command line, the Hive web interface, and the Hive Thrift server.

2. **Hive Services**: These are the services that provide the core functionality of Hive, such as the Hive metastore, the Hive driver, and the Hive compiler.

3. **Hive Storage and Computing**: This is where the data is stored and processed. Hive uses Hadoop's HDFS for storage and MapReduce for computing.

## Installation

To install Hive, follow these steps:

1. Download the latest version of Hive from the Apache Hive website.

2. Extract the downloaded file to a directory of your choice.

3. Set the environment variable `HIVE_HOME` to the directory where you extracted Hive.

4. Add the `$HIVE_HOME/bin` directory to your `PATH` environment variable.

5. Start the Hive shell by running the `hive` command.

6. Verify that Hive is installed correctly by running a simple HiveQL query, such as `SHOW TABLES;`.