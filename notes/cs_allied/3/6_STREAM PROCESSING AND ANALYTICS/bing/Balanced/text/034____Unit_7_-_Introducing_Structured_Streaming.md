## Unit 7 - Introducing Structured Streaming

- Structured Streaming is a high-level API for building scalable and fault-tolerant streaming applications using Spark SQL.
- Structured Streaming allows you to express your streaming computation as a batch-like query on a table that is continuously updated with new data.
- Structured Streaming handles the details of streaming execution, such as incremental query planning, state management, checkpointing, and recovery.
- Structured Streaming supports various sources and sinks, such as files, Kafka, sockets, and memory.
- Structured Streaming supports two output modes: append and update.
  - Append mode: only the new rows appended to the result table since the last trigger are written to the sink.
  - Update mode: only the rows that were updated in the result table since the last trigger are written to the sink.
- Structured Streaming supports two types of triggers: processing-time and event-time.
  - Processing-time trigger: the query is executed periodically based on a fixed interval of time.
  - Event-time trigger: the query is executed based on the data arrival and watermarking logic.