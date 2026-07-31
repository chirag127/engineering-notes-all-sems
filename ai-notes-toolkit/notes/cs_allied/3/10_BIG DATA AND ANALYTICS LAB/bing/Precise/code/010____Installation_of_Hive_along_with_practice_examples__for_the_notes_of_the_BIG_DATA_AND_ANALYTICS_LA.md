## Installation of Hive along with practice examples

Hive is a data warehousing solution built on top of the Hadoop Map-Reduce framework. It is used for managing and querying large datasets residing in distributed storage. Here are the steps to install Hive on Ubuntu:

1. **Download Hive**: Download the Hive 3.1.2 from the Apache website. Locate the `apache-hive-3.1.2-bin.tar.gz` file in your system .

2. **Extract the tar file**: Extract the `apache-hive-3.1.2-bin.tar.gz` file using the command: `tar -xzf apache-hive-3.1.2-bin.tar.gz` .

3. **Configure Hive files**: After extracting the tar file, you need to configure the Hive files .

Here is an example of how to create a database and a table in Hive:

```sql
hive> create database Company;
(database create)
Hive> use Company;
Hive> create table employee (id int, name String, salary String);
(this will create table employee under database Company because we have already executed the command Use database.)
```


Hive can also be integrated with other tools for additional capabilities. For example, Tableau along with Apache Hive can be used for Data Visualization, Apache Tez integration with Hive will provide you real-time processing capabilities, etc .