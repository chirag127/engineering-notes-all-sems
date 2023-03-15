### HBase

- HBase is a **column-oriented non-relational database management system** that runs on top of **Hadoop Distributed File System (HDFS)**  .
- HBase provides a **fault-tolerant** way of storing **sparse data sets**, which are common in many big data use cases .
- HBase is well suited for **real-time data processing** or **random read/write access** to large volumes of data .
- HBase is modeled after **Google's Bigtable**, a distributed storage system for structured data.
- HBase does not have a **fixed database schema** in a non-relational database, which means developers can add new data without conforming to a schema model.
- HBase uses **HBase Master** and **Region Servers** to manage the data and provide services to the clients .
- HBase stores data in **tables**, which are composed of **rows** and **columns**. Each row has a unique identifier called a **row key**. Each column belongs to a **column family**, which is a logical grouping of columns. Each cell in a table can have multiple **versions**, which are identified by a **timestamp** .
- HBase supports **CRUD operations** (create, read, update, delete) on the data, as well as **scan** and **filter** operations to retrieve a range of rows or columns .
- HBase also supports **coprocessors**, which are user-defined code that can run on the server side and provide custom functionality or hooks for the data processing .
- HBase can be integrated with other **Hadoop ecosystem components**, such as **MapReduce**, **Spark**, **Hive**, **Pig**, **Flume**, **Sqoop**, etc. to perform various data analysis tasks .