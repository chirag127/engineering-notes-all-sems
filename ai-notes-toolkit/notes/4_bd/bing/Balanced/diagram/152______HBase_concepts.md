#### HBase concepts

- HBase is a type of NoSQL database and is classified as a key-value store.
- HBase is a column-oriented database that runs on top of the Hadoop Distributed File System (HDFS) .
- HBase is an open-source project and is horizontally scalable.
- HBase is a data model that is similar to Google’s Bigtable and is designed to provide quick random access to huge amounts of structured data.
- HBase has a master-slave architecture, where a master node manages the cluster and region servers store portions of the tables and perform the work on the data.
- HBase table schema defines only column families, which are collections of columns. Each column family can have unlimited columns.
- HBase table contains multiple rows, each identified by a unique row key. Each row can have different columns under the same column family.
- HBase table supports versioning, which means multiple values can be stored for the same cell with different timestamps.
- HBase table supports compression, bloom filters, and in-memory caching to optimize the storage and performance.
- HBase is well suited for real-time data processing or random read/write access to large volumes of data. It is also used for sparse data sets, which are common in many big data use cases.