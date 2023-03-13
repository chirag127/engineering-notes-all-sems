#### Schema design in HBase

- HBase is a column-oriented, NoSQL database that runs on top of Hadoop. It does not support any kind of joins, but it provides the single-indexing strategy on the row key.
- HBase schema design supports denormalization with nested entities. These nested entities are nothing but a column whose name is the unique identifier for the nested entity and whose value is the entire record mashed together. Since HBase allows dynamic column definition, there's no problem.
- HBase schema design is very different compared to the relation database schema design. Below are some of general concept that should be followed while designing schema in Hbase:
  - Row key: Each table in HBase table is indexed on row key. Data is sorted lexicographically by this row key. The row key should be chosen carefully to ensure good performance and scalability. It should be unique, short, and meaningful. It should also avoid hotspots, which are regions of the table that receive more read or write requests than others. A common technique to avoid hotspots is to use salting, which is adding a random prefix to the row key to distribute the load evenly across the cluster.
  - Column family: A column family is a logical grouping of columns that share some common characteristics, such as compression, encoding, or versioning. A column family must be defined at the table creation time, and cannot be changed later. A column family can have one or more columns, which are identified by a qualifier. A column family name and a column qualifier name are separated by a colon, such as cf1:col1. A column family can have a maximum size of 2 GB, and should be kept as small as possible to reduce the I/O overhead.
  - Column: A column is a key-value pair that belongs to a column family. A column can have multiple versions, which are identified by a timestamp. A column can store any type of data, such as strings, numbers, or binary data. A column can be added or deleted dynamically, without affecting the schema of the table.
  - Cell: A cell is the smallest unit of data in HBase. It is the intersection of a row and a column. A cell can have a maximum size of 10 MB, and should be kept as small as possible to reduce the memory consumption and network latency.
- HBase schema design should follow some best practices, such as :
  - Use short and descriptive names for row keys, column families, and columns.
  - Avoid using composite row keys, unless they are necessary for efficient range scans or secondary indexing.
  - Use compression and encoding to reduce the disk space and network bandwidth usage.
  - Use Bloom filters to reduce the number of disk seeks for non-existent rows or columns.
  - Use filters to optimize read performance by applying predicates on the server side.
  - Use coprocessors to implement custom logic on the server side, such as aggregation, join, or trigger.
  - Use bulk loading to import large amounts of data into HBase efficiently.
  - Use compaction and major compaction to merge small files and delete obsolete data periodically.
  - Use regions and region servers to distribute and balance the data and load across the cluster.
  - Use replication and backup to ensure high availability and durability of the data.