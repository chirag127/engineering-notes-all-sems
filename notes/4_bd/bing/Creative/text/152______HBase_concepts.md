#### HBase concepts

- HBase is a type of NoSQL database and is classified as a key-value store.
- HBase is a column-oriented database that runs on top of the Hadoop Distributed File System (HDFS) .
- HBase is an open-source project and is horizontally scalable.
- HBase is a data model that is similar to Google’s Bigtable designed to provide quick random access to huge amounts of structured data.
- HBase is well suited for real-time data processing or random read/write access to large volumes of data.
- HBase has a master-slave architecture, where a master node manages the cluster and region servers store portions of the tables and perform the work on the data.
- HBase table schema defines only column families, and each family can have unlimited columns.
- HBase table contains multiple families, and each family can have multiple versions of the same column.
- HBase table values are identified with a key, and both key and values are byte array, which means binary formats can be stored easily.
- HBase table values are stored in key-orders, and values can be quickly accessed by their keys.