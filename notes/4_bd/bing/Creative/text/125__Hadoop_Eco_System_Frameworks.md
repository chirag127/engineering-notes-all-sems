### Hadoop Eco System Frameworks

Hadoop is an open source framework that allows for the distributed storage and processing of large datasets across clusters of computers using simple programming models. Hadoop is designed to scale up from a single computer to thousands of clustered computers, with each machine offering local computation and storage. Hadoop can efficiently store and process large datasets ranging in size from gigabytes to petabytes of data.

Hadoop consists of four major elements: HDFS, MapReduce, YARN, and Hadoop Common . These elements work together to form the core of the Hadoop ecosystem, which is a platform or a suite that provides various services to solve the big data problems. It includes Apache projects and various commercial tools and solutions.

- HDFS: Hadoop Distributed File System is the primary component of the Hadoop ecosystem and is responsible for storing large data sets of structured or unstructured data across various nodes and thereby maintaining the metadata in the form of log files. HDFS provides high-throughput access to application data with no need for schemas to be defined up front .
- MapReduce: MapReduce is a programming model for large-scale data processing. Using distributed and parallel computation algorithms, MapReduce makes it possible to carry over processing logic and helps to write applications that transform big datasets into one manageable set .
- YARN: Yet Another Resource Negotiator is a resource-management platform responsible for managing compute resources in clusters and using them to schedule users’ applications. It performs scheduling and resource allocation across the Hadoop system .
- Hadoop Common: Hadoop Common includes the libraries and utilities used and shared by other Hadoop modules .

All Hadoop modules are designed with a fundamental assumption that hardware failures of individual machines or racks of machines are common and should be automatically handled in software by the framework.

Beyond the core elements, the Hadoop ecosystem also includes many other tools and applications that help collect, store, process, analyze, and manage big data. Some of these are:

- Pig: Pig is a high-level scripting language that allows users to write complex data transformations using a simple syntax. Pig runs on top of MapReduce and can handle structured and semi-structured data.
- Hive: Hive is a data warehouse system that provides a SQL-like interface to query and analyze data stored in HDFS. Hive supports a variety of data formats and can perform complex analytics on large datasets.
- HBase: HBase is a NoSQL database that provides random access and strong consistency for large amounts of sparse data. HBase is built on top of HDFS and can support real-time applications that require low latency and high scalability.
- Spark: Spark is an in-memory data processing framework that can perform batch and streaming analytics on large datasets. Spark supports a variety of languages and libraries, such as Scala, Python, Java, R, SQL, MLlib, GraphX, and Spark Streaming.
- Presto: Presto is a distributed SQL query engine that can query data from multiple sources, such as HDFS, Hive, HBase, Cassandra, MongoDB, and MySQL. Presto is designed for interactive analytics and can handle complex queries on large datasets.
- Zeppelin: Zeppelin is a web-based notebook that allows users to interactively explore and visualize data using various languages and frameworks, such as Spark, SQL, Python, R, and Scala.

The Hadoop ecosystem is constantly evolving and growing with new tools and technologies that aim to solve the big data challenges. Hadoop provides a flexible and scalable platform that can handle various types of data and applications. Hadoop is widely used in various domains, such as finance, retail, healthcare, social media, and education.