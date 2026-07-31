# Scaling Up Data Processing

## Unit 1 - Fundamentals of Stream Processing

- Stream processing is a data processing technology that supports the gathering, processing, and analysis of high-volume, heterogeneous, continuous data streams, to extract insights and actionable results near real-time.
- Stream processing differs from batch processing, which processes data in discrete chunks, typically after it has been stored in a database or a file system.
- Stream processing enables applications to react to data as soon as it arrives, without waiting for it to be collected and stored first.
- Stream processing can be used for various use cases, such as:
  - Monitoring and alerting: detecting anomalies, failures, or events of interest in real time and triggering appropriate actions or notifications.
  - Data enrichment and transformation: augmenting or modifying data streams with additional information or logic, such as geolocation, sentiment analysis, or data cleansing.
  - Aggregation and analytics: computing summary statistics, trends, or patterns over data streams, such as averages, counts, or top-k items.
  - Machine learning and artificial intelligence: training, updating, or applying machine learning models on data streams, such as classification, recommendation, or prediction.
- Stream processing requires a distributed computing paradigm that can handle the challenges of streaming data, such as:
  - Scalability: the ability to handle large volumes and high velocities of data streams, by partitioning and parallelizing the processing across multiple nodes or machines.
  - Fault tolerance: the ability to recover from failures or errors, by replicating or checkpointing the state of the processing and ensuring exactly-once or at-least-once delivery semantics.
  - Latency: the ability to process data streams with low delay, by minimizing the buffering, batching, or blocking of the data flow.
  - Correctness: the ability to handle the complexity and uncertainty of streaming data, such as out-of-order, duplicate, or missing data, by defining and applying consistent time semantics and windowing operations.
- Stream processing can be implemented using various frameworks, platforms, or services, such as:
  - Apache Spark: an open-source distributed processing system that supports both batch and stream processing, using a unified high-level API and a micro-batch execution model.
  - Apache Flink: an open-source distributed processing system that supports both batch and stream processing, using a unified low-level API and a native streaming execution model.
  - Apache Kafka: an open-source distributed messaging system that supports both data ingestion and stream processing, using a publish-subscribe model and a stream processing DSL or library.
  - Azure Stream Analytics: a cloud-based service that supports stream processing, using a SQL-like language and a fully managed, scalable, and secure environment.