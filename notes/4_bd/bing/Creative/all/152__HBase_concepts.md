#### HBase concepts

- HBase is a **column-oriented** non-relational database management system that runs on top of **Hadoop Distributed File System (HDFS)** .
- HBase provides a **fault-tolerant** way of storing **sparse data sets**, which are common in many big data use cases .
- HBase is well suited for **real-time data processing** or **random read/write access** to large volumes of data .
- HBase is a data model that is similar to **Google’s big table** designed to provide quick random access to huge amounts of structured data.
- HBase does not support a structured query language like SQL; in fact, HBase isn’t a relational data store at all.
- HBase applications are written in **Java** much like a typical Apache MapReduce application.
- HBase does support writing applications in **Apache Avro, REST and Thrift**.
- HBase relies on **ZooKeeper** for high-performance coordination.
- HBase works well with **Hive**, a query engine for batch processing of big data, to enable fault-tolerant big data applications.
- HBase is a type of **NoSQL** database and is classified as a **key-value store**.
- HBase is a part of the Hadoop ecosystem that provides random real-time read/write access to data in the Hadoop File System.
- HBase is a **distributed** database and the tables in it are sorted by row.
- The table schema defines only **column families**, which are the key value pairs.
- A table can have multiple column families and each column family can have any number of columns.
- Subsequent column values are stored contiguously on the disk.
- Each cell value of the table has a **timestamp**.
- HBase provides fast lookups for larger tables.
- HBase internally uses **Hash tables** and provides random access, and it stores the data in indexed HDFS files for faster lookups.

A possible mnemonic to remember the main features of HBase is:

**H**adoop + **B**ig table + **A**vro + **S**parse + **E**xtra fast

A possible ascii diagram to illustrate the HBase data model is:

```
+-----------------+-----------------+-----------------+
| Row ID          | Column Family 1 | Column Family 2 |
+-----------------+-----------------+-----------------+
| row1            | col1:val1       | col2:val2       |
|                 | col3:val3       | col4:val4       |
+-----------------+-----------------+-----------------+
| row2            | col1:val5       | col2:val6       |
|                 | col3:val7       |                 |
+-----------------+-----------------+-----------------+
| row3            | col1:val8       | col2:val9       |
|                 |                 | col4:val10      |
+-----------------+-----------------+-----------------+
```