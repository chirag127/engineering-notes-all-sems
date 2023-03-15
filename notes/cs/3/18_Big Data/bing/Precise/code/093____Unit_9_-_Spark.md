## Unit 9 - Spark

Apache Spark is an open-source distributed computing system that can process large amounts of data quickly. It was developed in response to the limitations of the Hadoop MapReduce computing model, which is good at batch processing but not as efficient for interactive queries or iterative algorithms.

Some key features of Spark include:

1. **Speed:** Spark can run programs up to 100 times faster than Hadoop MapReduce in memory, or 10 times faster on disk.
2. **Ease of Use:** Spark has easy-to-use APIs for operating on large datasets, including support for SQL queries, streaming data, and complex analytics such as machine learning and graph algorithms.
3. **Generality:** Spark combines SQL, streaming, and complex analytics in one platform, making it easy to build end-to-end data pipelines.
4. **Runs Everywhere:** Spark can run on Hadoop, Mesos, standalone, or in the cloud, and can access diverse data sources including HDFS, Cassandra, HBase, and S3.

Spark has several components, including:

- **Spark Core:** The foundation of the Spark platform, providing the basic functionality of distributed task scheduling, memory management, and fault recovery.
- **Spark SQL:** A module for working with structured data, providing a programming interface for data manipulation using relational or SQL-like operations.
- **Spark Streaming:** A module for processing live data streams, with support for many sources including Kafka, Flume, and HDFS.
- **MLlib:** A machine learning library, providing many common algorithms for classification, regression, clustering, and recommendation.
- **GraphX:** A graph computation engine, providing a flexible API for expressing graph algorithms and optimized execution on Spark.

Spark has become a popular tool for big data processing due to its speed, ease of use, and versatility. It is used by many organizations, including tech giants like Amazon, eBay, and Yahoo. It is also widely used in research and academia.