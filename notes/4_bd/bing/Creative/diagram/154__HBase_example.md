HBase is a distributed, scalable, and column-oriented database that runs on top of the Hadoop Distributed File System (HDFS). It is designed to store and process large and sparse data sets. HBase provides fast and random access to data, as well as MapReduce integration for batch processing.

An example of HBase is a table that stores diagnostic logs from servers in your environment. Each row might be a log record, and a typical column could be the timestamp of when the log record was written, or the server name where the record originated.

#### HBase example

The following diagram illustrates the basic architecture of a HBase table:

```
+-----------------+-----------------+-----------------+
| Row Key         | Column Family 1 | Column Family 2 |
+-----------------+-----------------+-----------------+
|                 | Column 1        | Column 3        |
|                 +-----------------+-----------------+
|                 | Column 2        | Column 4        |
+-----------------+-----------------+-----------------+
| Row 1           | Value 1         | Value 3         |
|                 +-----------------+-----------------+
|                 | Value 2         | Value 4         |
+-----------------+-----------------+-----------------+
| Row 2           | Value 5         | Value 7         |
|                 +-----------------+-----------------+
|                 | Value 6         | Value 8         |
+-----------------+-----------------+-----------------+
| Row 3           | Value 9         | Value 11        |
|                 +-----------------+-----------------+
|                 | Value 10        | Value 12        |
+-----------------+-----------------+-----------------+
```

Each row in a HBase table has a unique identifier called the row key. Each row can have one or more column families, which are groups of related columns. Each column family has a name and a schema. Each column within a column family has a qualifier, which is a byte array that identifies the column. Each cell in a HBase table has a value and a timestamp, which indicates when the value was written or updated.

HBase tables are physically stored as files in HDFS. Each column family is stored in a separate file, called a HFile. Each HFile is divided into smaller units called blocks, which are the units of I/O. Each HFile also has an index that maps the row keys to the blocks. HBase uses a data structure called a memstore to buffer the write operations in memory before flushing them to HFiles. HBase also uses a write-ahead log (WAL) to ensure durability of the write operations in case of a failure.

HBase supports CRUD (create, read, update, delete) operations on the table data, as well as scan operations to retrieve a range of rows. HBase also supports filters, coprocessors, and secondary indexes to enhance the query capabilities. HBase can be accessed through various APIs, such as Java, REST, Thrift, and Avro. HBase can also be integrated with other tools, such as Hive, Spark, and Pig, for data analysis and processing.