## Unit 9 - Spark

Apache Spark is an open-source distributed computing system that can process large amounts of data quickly. It was developed in response to the limitations of the Hadoop MapReduce computing model, which is good for batch processing but not for interactive queries or iterative algorithms.

Some key features of Spark include:

1. **Speed:** Spark can run programs up to 100 times faster than Hadoop MapReduce in memory, or 10 times faster on disk.
2. **Ease of use:** Spark has easy-to-use APIs for operating on large datasets, including support for SQL queries, streaming data, and complex analytics such as machine learning and graph algorithms.
3. **Generality:** Spark combines SQL, streaming, and complex analytics in a single engine, making it easy to build and combine different types of processing.
4. **Runs Everywhere:** Spark runs on Hadoop, Mesos, standalone, or in the cloud. It can access diverse data sources including HDFS, Cassandra, HBase, and S3.

Spark has several components, including:

- **Spark Core:** The foundation of the overall project, responsible for task scheduling, memory management, fault recovery, and interacting with storage systems.
- **Spark SQL:** A module for working with structured data using SQL or a DataFrame API.
- **Spark Streaming:** A module for processing live data streams.
- **MLlib:** A library for machine learning algorithms.
- **GraphX:** A library for graph processing.

Spark is widely used in big data processing and has a large and active community of users and contributors. It is a powerful tool for data processing and analysis.