# Unit 7 - Introducing Structured Streaming

- Structured Streaming is a high-level API for building end-to-end streaming applications with Apache Spark.
- Structured Streaming allows users to express streaming computations using the same familiar DataFrame and Dataset APIs as batch processing, and Spark automatically handles the incremental execution of the queries.
- Structured Streaming supports various sources and sinks for streaming data, such as files, Kafka, sockets, Delta Lake, etc.
- Structured Streaming provides two output modes for streaming queries: append and update.
  - Append mode: only the new rows appended to the result table since the last trigger are written to the sink.
  - Update mode: only the rows that were updated in the result table since the last trigger are written to the sink.
- Structured Streaming also supports watermarking, which is a way to specify how late the data is expected to arrive, and how long to wait for late data.
- Structured Streaming can handle both event-time and processing-time based aggregations, joins, and window operations.
- Structured Streaming provides a web UI to monitor the streaming queries and their metrics, such as input rate, processing rate, latency, etc.