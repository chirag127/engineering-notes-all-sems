# Structured Streaming Sinks

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- A Structured Streaming sink is a data source that can receive the output of a streaming query and store it in a specified format or location.
- Structured Streaming supports various types of sinks natively, such as Delta, AWS S3, Google GCS, Azure ADLS, Kafka topics, Kinesis streams, and more.
- Structured Streaming also supports two ways to write the output of a streaming query to data sources that do not have an existing streaming sink: foreachBatch() and foreach().
- foreachBatch() allows reusing existing batch data sources with a user-defined function that can perform arbitrary logic on the output of a streaming query.
- foreach() allows applying a user-defined function to each row of the output of a streaming query.
- Both foreachBatch() and foreach() require the user to manage the end-to-end fault-tolerance and exactly-once guarantees of the output.
- Structured Streaming sinks can be configured with various output modes, such as append, update, or complete, depending on the semantics of the streaming query.
- Structured Streaming sinks can also be configured with various trigger options, such as processing time, event time, or continuous, depending on the latency and throughput requirements of the streaming query.
- Structured Streaming sinks can be monitored and managed using the Spark UI, the Structured Streaming Web UI, or the StreamingQueryListener API.