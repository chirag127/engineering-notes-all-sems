## Unit 4 - Apache Spark as a Stream-Processing Engine

Apache Spark is an open source data-processing engine for large data sets. It is designed to deliver the computational speed, scalability, and programmability required for Big Data—specifically for streaming data, graph data, machine learning, and artificial intelligence (AI) applications .

Some of the features of Apache Spark as a stream-processing engine are:

- Spark Streaming: Spark Streaming is a component of Spark that enables real-time data stream processing. It allows users to process data from various sources such as Kafka, Flume, HDFS, sockets, etc. and perform transformations, aggregations, windowing, and output operations on the data streams .
- Structured Streaming: Structured Streaming is a higher-level API of Spark Streaming that provides a declarative way of defining streaming queries using the Dataset/DataFrame API. It supports event-time processing, watermarking, stateful operations, and output modes. It also integrates with Spark SQL and MLlib for structured queries and machine learning on streaming data .
- Spark SQL: Spark SQL is a module of Spark that provides a unified interface for querying structured and semi-structured data using SQL or the Dataset/DataFrame API. It supports various data sources such as Hive, Parquet, JSON, JDBC, etc. and can run SQL queries on streaming data as well as batch data .
- MLlib: MLlib is a library of Spark that provides scalable and distributed machine learning algorithms and utilities. It supports various types of machine learning tasks such as classification, regression, clustering, recommendation, etc. and can run on streaming data as well as batch data .

The following diagram illustrates the architecture of Apache Spark as a stream-processing engine:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Data Source   |---->|  Spark Streaming|---->|  Spark SQL/MLlib|
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```