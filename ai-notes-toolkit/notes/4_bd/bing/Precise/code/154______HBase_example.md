#### HBase Example

HBase is a distributed, column-oriented database that is built on top of the Hadoop Distributed File System (HDFS). It is an open-source project that is part of the Apache Hadoop ecosystem. HBase is designed to handle large amounts of data and is used for real-time read/write access to big data.

Here is an example of how to create a table in HBase:

1. Start the HBase shell by running the command `hbase shell`.
2. Create a table by running the command `create 'table_name', 'column_family'`. Replace `table_name` with the name of the table you want to create and `column_family` with the name of the column family.
3. Verify that the table was created by running the command `list`. This will show a list of all the tables in HBase.

This is a simple example of how to create a table in HBase. There are many other operations that can be performed in HBase, such as inserting data, querying data, and deleting data. These operations can be performed using the HBase shell or by using the HBase API in a programming language such as Java.