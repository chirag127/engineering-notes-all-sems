# Structured Streaming Sinks

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- A Structured Streaming sink is a data source that can receive the output of a streaming query and write it to a storage system or perform some arbitrary logic on it.
- Structured Streaming supports various types of sinks natively, such as Delta, AWS S3, Google GCS, Azure ADLS, Kafka topics, Kinesis streams, and more.
- Structured Streaming also supports two ways to write to arbitrary data sinks that do not have an existing streaming sink: foreachBatch() and foreach().
- foreachBatch() allows reusing existing batch data sources with a streaming query by applying a function to each micro-batch output.
- foreach() allows applying a function to each row of the streaming query output, which can be useful for sending the data to REST APIs or external systems.
- Structured Streaming sinks can be specified using the writeStream() method on a DataStreamWriter object, which takes the following parameters:
  - outputMode: specifies how the sink should handle updates to the streaming query output, such as append, update, or complete.
  - format: specifies the type of the sink, such as delta, kafka, console, etc.
  - options: specifies additional configuration options for the sink, such as path, checkpointLocation, topic, etc.
  - queryName: specifies an optional name for the streaming query, which can be used to identify it in the Spark UI.
  - trigger: specifies an optional trigger interval for the streaming query, such as ProcessingTime or Once.
  - partitionBy: specifies an optional list of columns to partition the output by, which can improve performance and scalability of the sink.
- Structured Streaming sinks can be started, stopped, and monitored using the StreamingQuery object returned by the start() method on the DataStreamWriter object.