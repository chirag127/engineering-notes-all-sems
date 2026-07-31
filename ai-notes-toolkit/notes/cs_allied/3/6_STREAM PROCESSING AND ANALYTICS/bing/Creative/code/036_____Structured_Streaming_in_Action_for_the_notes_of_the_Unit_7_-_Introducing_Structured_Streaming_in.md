```
### Structured Streaming in Action

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- Structured Streaming allows you to take the same operations that you perform in batch mode using Spark’s structured APIs, and run them in a streaming fashion. This can reduce latency and allow for incremental processing.
- Structured Streaming lets you express computation on streaming data in the same way you express a batch computation on static data. The Structured Streaming engine performs the computation incrementally and continuously updates the result as streaming data arrives.
- In Structured Streaming, a data stream is treated as a table that is being continuously appended . You express your streaming computation as a standard batch-like query as on a static table, but Spark runs it as an incremental query on the unbounded input table.
- Structured Streaming supports various sources and sinks for streaming data, such as Kafka, Flume, files, sockets, etc. You can also define your own custom sources and sinks using the Source and Sink interfaces.
- Structured Streaming provides two output modes for streaming queries: append mode and update mode. Append mode only adds new rows to the result table, while update mode updates existing rows and adds new rows to the result table.
- Structured Streaming also supports watermarking, which allows you to specify a threshold of how late the data is expected to be, and accordingly handle late data and state.
- Structured Streaming provides various built-in operations for stream processing, such as aggregations, joins, window functions, etc. You can also use user-defined functions (UDFs) and user-defined aggregate functions (UDAFs) to extend the functionality of Structured Streaming.
- Structured Streaming integrates with Spark's MLlib and GraphX libraries, allowing you to apply machine learning and graph algorithms on streaming data.
- Structured Streaming provides a web UI and APIs for monitoring and debugging streaming queries.
```