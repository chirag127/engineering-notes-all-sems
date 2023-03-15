### HBase

- HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS) .
- HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases .
- HBase is well suited for real-time data processing or random read/write access to large volumes of data .
- HBase is a non-relational column-oriented database, which means HBase doesn’t store relational data .
- HBase is ideal for high-scale real-time applications, such as a social media app or a streaming application .
- HBase does not have a fixed database schema, which allows developers to add new data without conforming to a schema model .
- HBase is an open-source, distributed, versioned database modeled after Google's Bigtable .
- HBase provides Bigtable-like capabilities on top of Hadoop and HDFS .
- HBase supports row-level transactions, strong consistency, and high availability .
- HBase has a master-slave architecture, where the master node manages the cluster metadata and the slave nodes (called region servers) store the data .
- HBase stores data in tables, which are composed of rows and columns. Each row has a unique identifier (called row key) and each column has a name and a value. Columns are grouped into column families, which share a common prefix and storage options .
- HBase also supports secondary indexes, filters, coprocessors, and replication .