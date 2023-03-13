## Hadoop Eco System Frameworks, Pig, Hive and HBase

Hadoop is an open-source, distributed computing framework designed to store and process large datasets on a cluster of commodity hardware. Over time, the Hadoop ecosystem has grown to include several other frameworks that complement and extend the capabilities of Hadoop. Here are some of the popular frameworks in the Hadoop ecosystem:

### Hadoop Eco System Frameworks:

1. HDFS: Hadoop Distributed File System (HDFS) is a distributed file system that stores data across multiple machines in a cluster. It provides high throughput access to application data and is designed to be fault-tolerant.

2. MapReduce: MapReduce is a programming model for processing large datasets in parallel across a cluster of machines. It consists of two phases - Map and Reduce - that are executed in parallel across the cluster.

3. YARN: Yet Another Resource Negotiator (YARN) is a resource management system that schedules and manages resources in a Hadoop cluster. It enables multiple data processing engines to run on the same cluster, such as MapReduce, Spark, and Flink.

4. Spark: Apache Spark is a fast and general-purpose cluster computing system that can process data in memory. It provides APIs for Java, Scala, and Python, and supports batch processing, stream processing, and machine learning.

### Pig:

Pig is a high-level platform for creating MapReduce programs used with Hadoop. It is a scripting language that makes it easy to write complex MapReduce programs without having to write Java code. Pig is used for data processing, data pipeline creation, and ad-hoc analysis. It provides a simple language for data manipulation, and its syntax is similar to SQL.

Mnemonic: "Pig is the animal that loves to play with big data."

### Hive:

Hive is a data warehouse system that provides a SQL-like interface to query data stored in Hadoop. It was developed by Facebook and is now an Apache Software Foundation project. Hive is used for ad-hoc queries, data analysis, and data warehousing. It supports SQL-like queries, and its syntax is similar to SQL. Hive supports data serialization and deserialization, and it can read data from multiple sources, including HDFS, HBase, and Amazon S3.

Mnemonic: "Hive is the place where bees store honey, and Hive is the place where data is stored."

### HBase:

HBase is a NoSQL database that provides real-time access to large datasets stored in Hadoop. It is a column-oriented database that is designed to handle large amounts of structured and semi-structured data. HBase is used for real-time data processing, data storage, and data retrieval. It provides a simple interface for storing and retrieving data, and it can be integrated with other Hadoop ecosystem tools, such as Pig and Hive.

Mnemonic: "HBase is like a bookshelf, with each row being a book and each column being a chapter."

In conclusion, the Hadoop ecosystem has several frameworks that provide different capabilities for storing, processing, and analyzing large datasets. Pig, Hive, and HBase are popular tools that make it easy to process and analyze data stored in Hadoop. With the help of these frameworks, developers and data analysts can build complex data processing pipelines and extract valuable insights from large datasets.