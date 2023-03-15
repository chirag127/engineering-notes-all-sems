#### HBase concepts

- HBase is a type of **NoSQL database** and is classified as a **key-value store** .
- HBase is a **column-oriented** database management system that runs on top of the **Hadoop Distributed File System (HDFS)** .
- HBase provides a **fault-tolerant** way of storing **sparse data sets**, which are common in many big data use cases.
- HBase is well suited for **real-time data processing** or **random read/write access** to large volumes of data .
- HBase is a data model that is similar to **Google’s big table** designed to provide quick random access to huge amounts of structured data.
- HBase is a part of the **Hadoop ecosystem** that provides random real-time read/write access to data in the Hadoop File System.
- HBase is **horizontally scalable**, which means it can handle increasing data and load by adding more nodes to the cluster.
- HBase has a **master-slave** architecture, where a **HMaster** node manages the cluster and **HRegionServer** nodes store portions of the tables and perform the work on the data .
- HBase tables are divided into **regions**, which are contiguous ranges of rows that are stored together.
- Each region is assigned to a region server, which can serve multiple regions.
- Each region server is responsible for handling read and write requests, splitting regions, and reporting to the master.
- Each HBase table consists of one or more **column families**, which are logical groupings of columns that share common characteristics.
- Each column family contains one or more **columns**, which are identified by a **qualifier**.
- Each column can have multiple **versions**, which are timestamped values that are stored in descending order.
- Each row in an HBase table is identified by a unique **row key**, which is a byte array that can be any length.
- HBase supports **CRUD** operations (create, read, update, delete) on the data, as well as **scan** operations to retrieve a range of rows.
- HBase also supports **filters**, **coprocessors**, **bulk loading**, and **secondary indexing** to enhance the functionality and performance of the database.