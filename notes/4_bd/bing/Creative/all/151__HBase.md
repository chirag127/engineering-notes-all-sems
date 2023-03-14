### HBase

- HBase is an open-source, distributed, versioned, non-relational database modeled after Google's Bigtable .
- HBase runs on top of Hadoop Distributed File System (HDFS) or Alluxio, providing Bigtable-like capabilities for Hadoop  .
- HBase is a column-oriented database, which means it stores data in columns rather than rows. Each column can have multiple versions and timestamps, allowing for efficient storage and retrieval of historical data .
- HBase is well suited for real-time data processing or random read/write access to large volumes of data. It can handle sparse data sets, which are common in many big data use cases  .
- HBase features compression, in-memory operation, and Bloom filters on a per-column basis as outlined in the original Bigtable paper .
- HBase tables can serve as the input and output for MapReduce jobs run in Hadoop, and may be accessed through the Java API but also through REST, Avro or Thrift gateway APIs .
- HBase is not a direct replacement for a classic SQL database, however Apache Phoenix project provides a SQL layer for HBase as well as JDBC driver that can be integrated with various analytics and business intelligence applications. The Apache Trafodion project provides a SQL query engine with ODBC and JDBC drivers and distributed ACID transaction protection across multiple statements, tables and rows that use HBase as a storage engine.
- HBase is a CP type system in the parlance of Eric Brewer's CAP Theorem, which means it guarantees consistency and partition tolerance, but not availability in the presence of network failures.
- HBase is designed to scale linearly. It comprises a set of standard tables with rows and columns, much like a traditional database. Each table must have an element defined as a primary key, and all access attempts to HBase tables must use this primary key.
- HBase has a master-slave architecture. The master node manages the cluster metadata and assigns regions (horizontal partitions of tables) to region servers (slave nodes). The region servers handle read and write requests from clients and perform local operations such as splits and compactions .
- HBase uses ZooKeeper, a distributed coordination service, to maintain the cluster state and configuration, and to perform leader election and failover .
- HBase supports replication, which means it can copy data from one cluster to another for backup or disaster recovery purposes. Replication can be configured at the table or column family level, and can be synchronous or asynchronous .
- HBase also supports snapshots, which are point-in-time copies of tables that can be used for backup or restore operations. Snapshots can be created and deleted without affecting the online performance of the cluster .
- HBase has a shell that is based on JRuby, which allows users to interact with the database using commands or scripts. The shell can also be used to perform administrative tasks such as creating and deleting tables, altering schemas, and monitoring the cluster status .
- HBase has a web-based user interface that provides information about the cluster, such as the master and region server status, the table and region details, the replication and snapshot status, and the metrics and logs .

Some mnemonics and learning tricks for HBase are:

- HBase is a Hadoop database, which means it runs on top of HDFS and provides Bigtable-like features for Hadoop.
- HBase is a column-oriented database, which means it stores data in columns rather than rows. You can remember this by thinking of the letter C in HBase as column.
- HBase is a CP type system, which means it guarantees consistency and partition tolerance, but not availability. You can remember this by thinking of the letter P in HBase as partition.
- HBase has a master-slave architecture, which means it has one master node and multiple region servers. You can remember this by thinking of the letter M in HBase as master.
- HBase uses ZooKeeper, which is a distributed coordination service. You can remember this by thinking of the letter Z in HBase as ZooKeeper.