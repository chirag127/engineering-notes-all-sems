### Structured Streaming in Action

- Structured Streaming is a **scalable and fault-tolerant stream processing engine** built on the Spark SQL engine.
- Structured Streaming allows you to **take the same operations that you perform in batch mode** using Spark’s structured APIs, and **run them in a streaming fashion**. This can reduce latency and allow for incremental processing.
- Structured Streaming lets you **express computation on streaming data in the same way you express a batch computation on static data**. The Structured Streaming engine performs the computation incrementally and continuously updates the result as streaming data arrives.
- In Structured Streaming, a data stream is treated as a **table that is being continuously appended** . You express your streaming computation as a standard batch-like query as on a static table, but Spark runs it as an incremental query on the unbounded input table.
- Structured Streaming provides **fast, scalable, fault-tolerant, end-to-end exactly-once stream processing** without the user having to reason about streaming.
- Structured Streaming supports various sources and sinks for streaming data, such as Kafka, Flume, socket, files, Delta Lake, console, memory, etc.
- Structured Streaming supports various output modes for streaming queries, such as append, update, and complete.
- Structured Streaming supports various operations on streaming data, such as aggregations, joins, window functions, watermarking, etc.
- Structured Streaming supports various triggers for streaming queries, such as processing-time, event-time, and continuous.
- Structured Streaming supports various monitoring and debugging tools for streaming queries, such as web UI, SQL tab, metrics, and explain.