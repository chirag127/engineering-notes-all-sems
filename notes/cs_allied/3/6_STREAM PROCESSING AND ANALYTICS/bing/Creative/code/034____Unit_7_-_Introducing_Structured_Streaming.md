## Unit 7 - Introducing Structured Streaming

- Structured Streaming is a high-level API for building scalable and fault-tolerant streaming applications using Spark SQL.
- Structured Streaming allows you to express your streaming computation as a batch-like query on a table that is continuously updated with new data.
- Structured Streaming handles the details of streaming execution, such as incremental query planning, state management, checkpointing, and recovery.
- Structured Streaming provides the same powerful and expressive APIs as Spark SQL, such as DataFrames, Datasets, SQL, and Catalyst optimizer.
- Structured Streaming supports various sources and sinks, such as Kafka, files, sockets, databases, and memory.
- Structured Streaming supports two types of output modes: append and update.
  - Append mode: only the new rows appended to the result table since the last trigger are written to the sink.
  - Update mode: only the rows that were updated in the result table since the last trigger are written to the sink.
- Structured Streaming supports two types of triggers: processing-time and event-time.
  - Processing-time trigger: the query is executed periodically based on a fixed interval of time, such as every 5 seconds.
  - Event-time trigger: the query is executed based on the data availability and watermark, which is a threshold for how late the data is expected to be.
- Structured Streaming supports watermarking, which is a technique to handle late and out-of-order data in streaming applications.
  - Watermarking allows you to specify a threshold for how late the data is expected to be, and discard any data that is older than the threshold.
  - Watermarking also allows you to perform windowed aggregations on event-time columns, and update the results as late data arrives.
- Structured Streaming supports various operations, such as map, filter, join, groupBy, window, and aggregation, on streaming DataFrames and Datasets.
- Structured Streaming supports monitoring and debugging of streaming queries using the StreamingQueryListener interface, which provides callbacks for query lifecycle events, such as start, progress, and termination.