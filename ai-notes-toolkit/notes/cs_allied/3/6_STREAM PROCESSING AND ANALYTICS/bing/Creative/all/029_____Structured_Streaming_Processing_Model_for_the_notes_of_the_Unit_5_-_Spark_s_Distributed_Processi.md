# Structured Streaming Processing Model

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine .
- Structured Streaming uses the same underlying architecture as Spark, so it can leverage the performance and cost optimizations built into the Spark engine.
- Structured Streaming treats a data stream as a table that is being continuously appended, and allows users to express their streaming computation using the same DataFrame and Dataset APIs as batch computation  .
- Structured Streaming provides two types of output modes: append mode and update mode .
  - Append mode: only the new rows appended to the result table since the last trigger are written to the sink .
  - Update mode: only the rows that were updated in the result table since the last trigger are written to the sink .
- Structured Streaming supports various types of sources and sinks, such as Kafka, Flume, HDFS, S3, JDBC, console, memory, etc .
- Structured Streaming supports various types of operations on streaming data, such as filtering, aggregation, joining, windowing, watermarking, etc .
- Structured Streaming guarantees end-to-end exactly-once semantics for some of the sources and sinks, such as Kafka, HDFS, S3, etc .
- Structured Streaming provides a web UI to monitor the streaming queries and their metrics, such as input rate, processing rate, latency, etc .