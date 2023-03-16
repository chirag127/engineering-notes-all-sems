## Unit 7 - Introducing Structured Streaming

- Structured Streaming is a high-level API for building scalable and fault-tolerant streaming applications using Spark SQL.
- Structured Streaming allows you to express your streaming computation as a batch-like query on a table that is continuously updated with new data.
- Structured Streaming handles the details of streaming execution, such as incremental query planning, state management, checkpointing, and recovery.
- Structured Streaming supports various sources and sinks, such as files, Kafka, sockets, and memory.
- Structured Streaming supports two output modes: append and update.
  - Append mode: only the new rows appended to the result table since the last trigger are written to the sink.
  - Update mode: only the rows that were updated in the result table since the last trigger are written to the sink.
- Structured Streaming supports two types of triggers: processing-time and event-time.
  - Processing-time trigger: the query is executed periodically based on the processing time of the system.
  - Event-time trigger: the query is executed based on the event time of the data, which is specified by a watermark column.
- Structured Streaming supports various operations on streaming DataFrames and DataSets, such as filtering, aggregation, joining, windowing, and watermarking.
- Structured Streaming provides a web UI to monitor the streaming query progress, latency, and throughput.