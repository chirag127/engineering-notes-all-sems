#### HBase example

- HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS) .
- HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases .
- HBase is well suited for real-time data processing or random read/write access to large volumes of data .
- An HBase table consists of rows and columns, where each column belongs to a column family .
- An HBase column represents an attribute of an object; for example, if the table is storing diagnostic logs from servers, each row might be a log record, and a typical column could be the timestamp of when the log record was written, or the server name where the record originated .
- HBase supports CRUD (create, read, update, delete) operations, as well as scan and filter operations, using a shell command or a Java API .
- HBase also supports secondary indexes, coprocessors, replication, and snapshots .

Here is an example of how to create a table in HBase with the specified name and column family using the shell command :

```
hbase (main):001:0> create 'education','guru99'
0 rows (s) in 0.312 seconds
=>Hbase::Table – education
```

The above example explains how to create a table in HBase with the name 'education' and the column family 'guru99'.

Some of the use cases of HBase are :

- In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area.
- In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights.
- In sports, HBase is used to store match details and the history of each match.