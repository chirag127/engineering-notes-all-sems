#### HBase Example

HBase is a distributed, column-oriented database that is built on top of the Hadoop Distributed File System (HDFS). It is an open-source, non-relational database that is designed to provide real-time read/write access to large datasets.

Here is an example of how to create a table in HBase:

1. Start the HBase shell by running the command `hbase shell`.
2. Create a table by running the command `create 'table_name', 'column_family'`. Replace `table_name` with the desired name for the table and `column_family` with the desired name for the column family.
3. Verify that the table was created by running the command `list`. This will display a list of all the tables in HBase.

This is a simple example of how to create a table in HBase. There are many other operations that can be performed, such as inserting data, querying data, and deleting data. These operations can be performed using the HBase shell or through the HBase API.