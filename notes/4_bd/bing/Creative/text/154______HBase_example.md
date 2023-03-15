#### HBase example

- HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS).
- HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases.
- HBase is well suited for real-time data processing or random read/write access to large volumes of data.
- HBase stores data in tables, which consist of rows and columns. Each row has a unique identifier called a row key, and each column belongs to a column family.
- HBase supports CRUD (create, read, update, delete) operations, as well as scan and filter operations, on the tables using a shell command interface or a Java API.
- HBase also supports secondary indexes, coprocessors, replication, snapshots, and security features.

Some examples of HBase use cases are:

- In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area.
- In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights.
- In sports, HBase is used to store match details and the history of each match.

An example of HBase table creation is:

- To create a table in HBase with the name 'education' and the column family 'guru99', the shell command is:

```bash
hbase (main):001:0> create 'education','guru99'
```

- The output will be:

```bash
0 rows (s) in 0.312 seconds =>Hbase::Table – education
```

- This means that the table 'education' with the column family 'guru99' has been created successfully.