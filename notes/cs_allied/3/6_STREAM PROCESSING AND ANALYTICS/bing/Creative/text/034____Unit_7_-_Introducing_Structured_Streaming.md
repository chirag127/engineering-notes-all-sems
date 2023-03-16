## Unit 7 - Introducing Structured Streaming

- Structured Streaming is a high-level API for building scalable and fault-tolerant streaming applications using Spark SQL.
- Structured Streaming allows you to express your streaming computation as a batch-like query on a table that is continuously updated with new data.
- Structured Streaming handles the details of streaming execution, such as incremental query planning, state management, checkpointing, and recovery.
- Structured Streaming supports various sources and sinks, such as files, Kafka, sockets, and memory.
- Structured Streaming supports two output modes: append and update. Append mode only adds new rows to the result table, while update mode can modify existing rows as well.
- Structured Streaming supports event-time and watermarking for handling late and out-of-order data.
- Structured Streaming supports various operations, such as aggregations, joins, window functions, and user-defined functions.