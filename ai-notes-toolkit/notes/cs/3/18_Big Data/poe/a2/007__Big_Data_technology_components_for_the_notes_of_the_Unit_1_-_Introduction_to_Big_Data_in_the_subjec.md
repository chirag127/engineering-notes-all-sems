 Here is the formal content in Markdown format without any emojis or external links for the topic -

### Big Data technology components for the notes of the Unit 1 - Introduction to Big Data in the subject of Big Data:

1. Hadoop: Hadoop is an open-source software framework for distributed storage and processing of big data sets using the MapReduce programming model. It contains the Hadoop Distributed File System (HDFS) for storage and a MapReduce engine for processing large data sets.

2. MapReduce: MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. It consists of two major tasks - Map and Reduce. The Map function processes the input data and generates output which is then aggregated by the Reduce function.

3. Hive: Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis. It allows analysts familiar with SQL to query the data. It translates SQL-like queries into MapReduce jobs to be executed by the Hadoop framework.

4. Pig: Pig is a high-level dataflow language and execution framework for parallel computation. It provides a procedural style of programming for mapping and reducing data using Pig Latin language which is then compiled into physical plans to execute on Hadoop. It aims to abstract away the complexity of MapReduce programming.

5. Mahout: Mahout is a machine learning library on top of Hadoop. It provides scalable implementations of machine learning algorithms for clustering, classification, and collaborative filtering for large data sets. Some of the machine learning algorithms included are k-means, logistic regression, naive Bayes, etc.

6. Sqoop: Sqoop is a tool for transferring bulk data between Hadoop and structured datastores such as relational databases. It can import data from external sources into Hadoop Distributed File System (HDFS) and export from HDFS into external sources. It provides a connector-based architecture to plug into different databases and data formats.

7. Flume: Flume is a distributed service for collecting, aggregating, and moving large amounts of log data into Hadoop. It is highly fault-tolerant and horizontally scalable and uses streams to provide a flexible and loosely coupled mechanism to transport data reliably. It has sources to ingest data and channels and sinks to deliver data to the required destinations.