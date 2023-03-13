#### HBase concepts

- HBase is a type of NoSQL database and is classified as a key-value store. It is an open-source project and is horizontally scalable. It is a distributed column-oriented database built on top of the Hadoop file system (HDFS) .
- HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data .
- HBase is a data model that is similar to Google’s big table designed to provide quick random access to huge amounts of structured data . It leverages the fault tolerance provided by the Hadoop File System (HDFS).
- HBase has a master-slave architecture, where a master node manages the cluster and region servers store portions of the tables and perform the work on the data. The master node is responsible for assigning regions to region servers, balancing the load, and handling schema changes.
- HBase stores data in tables, which are composed of rows and columns. Each row has a unique identifier called a row key, and each column has a name and a value. A column name consists of a column family and a column qualifier, separated by a colon. A column family is a logical grouping of columns that share some common characteristics, such as compression, encoding, or versioning.
- HBase supports multiple versions of data for each cell, where a cell is the intersection of a row and a column. Each version of data has a timestamp associated with it, which can be either assigned by the system or specified by the user. HBase allows users to query data by specifying a range of timestamps or a maximum number of versions.
- HBase also supports some advanced features, such as filters, coprocessors, and secondary indexes. Filters are used to apply some criteria on the data returned by a scan or a get operation. Coprocessors are user-defined code that can be executed on the region server side to perform some custom logic or aggregation. Secondary indexes are used to create alternative access paths to the data based on some column values.

Some mnemonics and learning tricks for HBase concepts are:

- HBase stands for Hadoop database, which indicates its relation to HDFS and MapReduce.
- HBase is a column-oriented database, which means it stores data by columns rather than by rows. This can be remembered by the word COBRA (COlumn-Based RAndom access).
- HBase has a master-slave architecture, which can be remembered by the word MASH (MAster-Slave HBase).
- HBase stores data in tables, which can be remembered by the word TAB (TAble-Based).
- HBase supports multiple versions of data, which can be remembered by the word MUD (MUltiple Data).
- HBase has a row key, a column family, and a column qualifier, which can be remembered by the word ROCK (ROw Key, COlumn family, Column Qualifier).