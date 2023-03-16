### Structured Streaming Sinks

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- A Structured Streaming sink is a data source that can receive the output of a streaming query and write it to a storage system or perform some arbitrary logic on it.
- Structured Streaming supports various types of sinks natively, such as Delta Lake, file systems (AWS S3, Google GCS, Azure ADLS, etc.), Kafka topics, Kinesis streams, and more.
- Structured Streaming also supports two ways to write to arbitrary data sinks that do not have an existing streaming sink: `foreachBatch()` and `foreach()`.
- `foreachBatch()` allows reusing existing batch data sources with a streaming query by applying a function to each micro-batch output as a DataFrame.
- `foreach()` allows applying a function to each row of the streaming query output as a Row object.
- Both `foreachBatch()` and `foreach()` can be used to write to REST API destinations, custom databases, or any other data sinks that are not natively supported by Structured Streaming .
- Structured Streaming sinks can be configured with various options, such as output mode, trigger, watermark, checkpoint location, etc.