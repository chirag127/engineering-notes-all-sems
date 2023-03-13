### HBase

- HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS) or Alluxio   .
- HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases .
- HBase is well suited for real-time data processing or random read/write access to large volumes of data  .
- HBase is modeled after Google's Bigtable, a distributed storage system for structured data .
- HBase does not store relational data, and does not have a fixed database schema . This allows developers to add new data without conforming to a schema model.
- HBase is ideal for high-scale real-time applications, such as social media apps or streaming applications.
- HBase consists of tables, which are composed of rows and columns. Each table has a row key and a column family. A column family can have multiple column qualifiers, which are the actual data values. Each cell in a table can have multiple versions, which are identified by timestamps .
- HBase supports CRUD (create, read, update, delete) operations, as well as scan and filter operations on tables .
- HBase also supports secondary indexes, coprocessors, replication, snapshots, and security features .
- HBase can be accessed through various APIs, such as Java, REST, Thrift, or Avro .
- HBase can be integrated with other Hadoop components, such as MapReduce, Spark, Hive, or Pig .

A simple example of an HBase table is shown below:

| Row key | Column family: info | Column family: score |
|---------|---------------------|----------------------|
| Alice   | name: Alice         | math: 90             |
|         | age: 20             | english: 85          |
| Bob     | name: Bob           | math: 80             |
|         | age: 21             | english: 75          |
| Charlie | name: Charlie       | math: 70             |
|         | age: 22             | english: 65          |

Some possible mnemonics and learning tricks for HBase are:

- HBase is a **H**adoop **base**d database that stores data in **H**orizontal columns.
- HBase is a **H**igh-scale **B**igtable-like database that supports **A**PIs, **S**cans, and **E**vents.
- HBase is a **H**uge database that can handle **B**illions of rows and **A**ny kind of data with **S**peed and **E**fficiency.