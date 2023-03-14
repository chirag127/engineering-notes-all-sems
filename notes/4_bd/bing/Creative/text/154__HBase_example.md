#### HBase example

HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). It provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

HBase applications are written in Java™ much like a typical Apache MapReduce application. HBase does support writing applications in Apache Avro, REST and Thrift. An HBase system is designed to scale linearly. It comprises a set of standard tables with rows and columns, much like a traditional database. Each table must have an element defined as a primary key, and all access attempts to HBase tables must use this primary key.

HBase allows for many attributes to be grouped together into column families, such that the elements of a column family are all stored together. This is different from a row-oriented relational database, where all the columns of a given row are stored together. With HBase you must predefine the table schema and specify the column families. However, new columns can be added to families at any time, making the schema flexible and able to adapt to changing application requirements.

HBase relies on ZooKeeper for high-performance coordination. ZooKeeper is built into HBase, but if you’re running a production cluster, it’s suggested that you have a dedicated ZooKeeper cluster that’s integrated with your HBase cluster. HBase works well with Hive, a query engine for batch processing of big data, to enable fault-tolerant big data applications.

Some examples of HBase use cases are:

- In the healthcare sector, HBase is used for storing genome sequences and disease history of people or a particular area.
- In the field of e-commerce, HBase is used for storing logs about customer search history and it also performs analytics and target advertisement for better business insights.
- In sports, HBase is used to store match details and the history of each match.

To create tables and insert data in HBase, you can use SSH to connect to HBase clusters and then use Apache HBase Shell to create HBase tables, insert data, and query data. For most people, data appears in the tabular format:

| Row | Column Family: guru99 | Column Family: education |
| --- | --- | --- |
| 1 | name: John | course: Hadoop |
| 2 | name: Mary | course: Java |

In HBase, the same data looks like:

| Row | Column | Value |
| --- | --- | --- |
| 1 | guru99:name | John |
| 1 | education:course | Hadoop |
| 2 | guru99:name | Mary |
| 2 | education:course | Java |

To create a table in HBase with the specified name and column families, you can use the create command in HBase Shell. For example:

```
hbase (main):001:0> create 'education','guru99','course'
0 rows (s) in 0.312 seconds =>Hbase::Table – education
```

To insert data into the table, you can use the put command in HBase Shell. For example:

```
hbase (main):002:0> put 'education','1','guru99:name','John'
0 rows (s) in 0.031 seconds
hbase (main):003:0> put 'education','1','course:course','Hadoop'
0 rows (s) in 0.015 seconds
hbase (main):004:0> put 'education','2','guru99:name','Mary'
0 rows (s) in 0.015 seconds
hbase (main):005:0> put 'education','2','course:course','Java'
0 rows (s) in 0.015 seconds
```

To query data from the table, you can use the get or scan command in HBase Shell. For example:

```
hbase (main):006:0> get 'education','1'
COLUMN CELL
course:course timestamp=1639519070, value=Hadoop
guru99:name timestamp=1639519060, value=John
1 row (s) in 0.015 seconds
hbase (main):007:0> scan 'education'
ROW COLUMN CELL
1 course:course timestamp=163951