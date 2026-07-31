#### HBase example

HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

Some examples of how HBase is used in different domains are:

- In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area.
- In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights.
- In sports, HBase is used to store match details and the history of each match.

To create a table in HBase, we can use the HBase shell command `create` with the table name and the column family name as arguments. For example, to create a table named `education` with a column family named `guru99`, we can use the following command:

```
hbase (main):001:0> create 'education','guru99'
0 rows (s) in 0.312 seconds
=>Hbase::Table – education
```

To specify the HDFS directory where HBase stores its data, we can use the configuration property `hbase.rootdir` in the `hbase-site.xml` file. For example, to specify the HDFS directory `/hbase` where the HDFS instance’s namenode is running at `namenode.example.org` on port `9000`, we can set this value to:

```
hdfs://namenode.example.org:9000/hbase
```

By default, HBase writes to whatever `${hbase.tmp.dir}` is set to, which is usually `/tmp`, so we should change this configuration or else all data will be lost on machine restart.