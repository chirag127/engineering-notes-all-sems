### HBase

- HBase is a **column-oriented non-relational database management system** that runs on top of **Hadoop Distributed File System (HDFS)**  .
- HBase is an **open-source project** and is **horizontally scalable** .
- HBase is a data model that is similar to **Google’s Bigtable** designed to provide **quick random access** to huge amounts of **structured data** .
- HBase provides a **fault-tolerant** way of storing **sparse data sets**, which are common in many big data use cases.
- HBase is well suited for **real-time data processing** or **random read/write access** to large volumes of data.
- An HBase system is designed to scale linearly. It comprises a set of **standard tables** with **rows and columns**, much like a traditional database.
- Each table must have an element defined as a **primary key**, and all access attempts to HBase tables must use this primary key.
- HBase supports **versioning** of data, which means that multiple versions of the same data can be stored and retrieved.
- HBase also supports **compression**, **bloom filters**, and **in-memory caching** to optimize the performance and storage efficiency.
- HBase can be accessed through **Java API**, **REST API**, or **Thrift API**. It can also be integrated with other Hadoop components such as **MapReduce**, **Hive**, **Pig**, and **Spark**.