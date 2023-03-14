HBase is a column-oriented non-relational database management system that runs on top of Hadoop Distributed File System (HDFS). It provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data.

HBase applications are written in Java™ much like a typical Apache MapReduce application. HBase does support writing applications in Apache Avro, REST and Thrift. HBase relies on ZooKeeper for high-performance coordination.

An HBase system is designed to scale linearly. It comprises a set of standard tables with rows and columns, much like a traditional database. Each table must have an element defined as a primary key, and all access attempts to HBase tables must use this primary key. HBase allows for many attributes to be grouped together into column families, such that the elements of a column family are all stored together.

HBase works well with Hive, a query engine for batch processing of big data, to enable fault-tolerant big data applications.

#### Advanced usage of HBase

HBase has two fundamental key structures: the row key and the column key. Both can be used to convey meaning, by either the data they store, or by exploiting their sorting order. In the following sections, we will use these keys to solve commonly found problems when designing storage solutions.

##### Key Design

HBase’s main unit of separation within a table is the column family —not the actual columns as expected from a column-oriented database in their traditional sense. Figure 1 shows the fact that, although you store cells in a table format logically, in reality these rows are stored as linear sets of the actual cells, which in turn contain all the vital information inside them. The top-left part of the figure shows the logical layout of your data—you have rows and columns. The columns are the typical HBase combination of a column family name and a column qualifier, forming the column key. The rows also have a row key so that you can address all columns in one logical row.

```
Figure 1. Rows stored as linear sets of cells

+----------------+----------------+----------------+----------------+
| Row Key        | Column Family  | Column Family  | Column Family  |
|                | A              | B              | C              |
+----------------+----------------+----------------+----------------+
| Row 1          | A:1            | B:1            | C:1            |
|                | A:2            | B:2            | C:2            |
|                | A:3            | B:3            | C:3            |
+----------------+----------------+----------------+----------------+
| Row 2          | A:1            | B:1            | C:1            |
|                | A:2            | B:2            | C:2            |
|                | A:3            | B:3            | C:3            |
+----------------+----------------+----------------+----------------+
| Row 3          | A:1            | B:1            | C:1            |
|                | A:2            | B:2            | C:2            |
|                | A:3            | B:3            | C:3            |
+----------------+----------------+----------------+----------------+

+----------------+----------------+----------------+----------------+
| Row Key        | Column Key     | Value          | Timestamp      |
+----------------+----------------+----------------+----------------+
| Row 1          | A:1            | Value 1        | 1234567890     |
| Row 1          | A:2            | Value 2        | 1234567891     |
| Row 1          | A:3            | Value 3        | 1234567892     |
| Row 1          | B:1            | Value 4        | 1234567893     |
| Row 1          | B:2            | Value 5        | 1234567894     |
| Row 1          | B:3            | Value 6        | 1234567895     |
| Row 1          | C:1            | Value 7        | 1234567896     |
| Row 1          | C:2            | Value 8        | 1234567897     |
| Row 1          | C:3            | Value 9        |