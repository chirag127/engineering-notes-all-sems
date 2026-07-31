#### Advanced Indexing in HBase

- HBase is a column-oriented NoSQL database management system that runs on top of the Hadoop Distributed File System (HDFS). It is modeled after Google’s Big Table and written in Java.
- In HBase, there are no indexes. The rowkey, column family, column qualifier are all stored in sort order based on the java comparable method for byte arrays.
- Access to records in any way other than through the primary row key requires scanning over potentially all the rows in the table to test them against your filter.
- Secondary indexing is a way to improve the performance of queries that do not use the primary row key. HBASE-9203 is a Jira entry that exists specifically to address the ideas behind secondary indexing.
- An index will surely work faster than scanning a large number of rows every time. If you use an HBase version that already has coprocessors you can follow the advice given in the documentation. If you are using older versions of HBase you need to set up an additional table to act as the index and update manually.