### Structured Streaming Sinks

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- A Structured Streaming sink is a data source that can receive the output of a streaming query and write it to a storage system or perform some arbitrary logic on it.
- Structured Streaming supports various types of sinks natively, such as Delta Lake, AWS S3, Google GCS, Azure ADLS, Kafka topics, Kinesis streams, and more.
- Structured Streaming also supports two ways to write to arbitrary data sinks that do not have an existing streaming sink: `foreachBatch()` and `foreach()`.
- `foreachBatch()` allows you to reuse existing batch data sources and write the output of each micro-batch as a static DataFrame.
- `foreach()` allows you to write custom logic to process each row of the output as a streaming Dataset.
- Structured Streaming sinks can be categorized into two types: append-only and update-mode.
- Append-only sinks can only append new rows to the output, and do not support deleting or updating existing rows. Examples of append-only sinks are file, Kafka, and Delta Lake.
- Update-mode sinks can update or delete existing rows in the output, and support aggregations and joins in the streaming query. Examples of update-mode sinks are memory, console, and Delta Lake.