
#### Hadoop File System Interfaces

* **HDFS** (Hadoop Distributed File System): HDFS is a distributed file system designed to store very large files running on commodity hardware. It works on the principle of storing data across multiple nodes in a cluster. It is a highly fault-tolerant system, meaning that if one node in the cluster fails, the data stored on that node is replicated on other nodes. HDFS also provides high throughput access to application data and is suitable for applications that have large data sets.

* **MapReduce**: MapReduce is a programming model for processing large data sets in a distributed computing environment. It works by dividing a large task into smaller tasks that can be processed in parallel. The results of each task are then combined to produce the final output.

* **YARN** (Yet Another Resource Negotiator): YARN is an essential component of the Hadoop ecosystem. It is a resource management platform that enables applications to run on a cluster of nodes. It provides an efficient way to manage resources across multiple applications and helps to ensure that each application gets the resources it needs to run.

* **HBase**: HBase is a distributed, column-oriented database built on top of Hadoop. It provides a fault-tolerant way of storing large amounts of sparse data. It is especially suitable for applications that require random, real-time read/write access to large datasets.

* **Hive**: Hive is a data warehouse system for Hadoop. It provides a way to query large datasets stored in HDFS using a SQL-like language called HiveQL. It also provides a way to store the results of queries in tables, allowing for easy access and analysis of data.

* **Pig**: Pig is a data processing platform for Hadoop. It provides a way to write data processing scripts in a high-level language called Pig Latin. Pig makes it easy to process large datasets in a distributed environment.