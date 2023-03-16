### Understanding Latency-Throughput-Oriented Processing for the notes of the Unit 4 - Apache Spark as a Stream-Processing Engine

- Latency is the time taken to process a single record or a batch of records in a stream-processing system.
- Throughput is the rate at which records are processed by the system, measured in records per second or bytes per second.
- Latency and throughput are often inversely related, meaning that increasing one may decrease the other.
- Apache Spark is a distributed computing framework that supports stream-processing applications, among other use cases.
- Spark uses a micro-batch model, where records are grouped into small batches and processed periodically by Spark tasks.
- Spark tasks are scheduled and executed by the Spark scheduler, which can be configured to optimize for different goals, such as fairness, locality, or resource utilization.
- Spark also provides various APIs and features to enable low-latency and high-throughput stream-processing, such as:
  - Structured Streaming, which is a high-level API that allows users to express complex stream-processing logic using SQL or DataFrames.
  - Project Lightspeed, which is a recent initiative to improve the performance and simplicity of Structured Streaming by reducing the overhead of micro-batching and enabling stateful stream-processing on GPUs.
  - Spark Streaming, which is a lower-level API that allows users to manipulate streams of RDDs (Resilient Distributed Datasets) and apply custom transformations and output operations.
  - Spark SQL, which is a module that supports SQL queries on streaming and static data sources, and can leverage Spark's Catalyst optimizer to generate efficient execution plans.
  - Spark MLlib, which is a library that provides machine learning algorithms and utilities for streaming and batch data analysis.
  - Spark GraphX, which is a library that supports graph processing and analytics on streaming and static data.