# Installation of Hive along with practice examples

Hive is a data warehousing solution built on top of the Hadoop Map-Reduce framework. It is used for managing and querying large datasets residing in distributed storage. Here are the steps to install Hive on Ubuntu:

1. **Download Hive**: Download the Hive 3.1.2 from the Apache website.
2. **Unzip and Install Hive**: After downloading Hive, unzip the `apache-hive-3.1.2-bin.tar.gz` file.
3. **Configuring Hive files**: Configure the necessary Hive files according to your system requirements.

After installing Hive, you can start practicing with some examples. Here is an example of creating a database and a table in Hive:

```sql
hive> create database Company;
hive> use Company;
hive> create table employee (id int, name String, salary String);
```

This will create a database named `Company` and a table named `employee` under the `Company` database. You can then insert data into the table and run queries on it.

Hive can also be integrated with other tools for additional capabilities. For example, Tableau can be used with Hive for data visualization, and Apache Tez can be integrated with Hive for real-time processing capabilities.