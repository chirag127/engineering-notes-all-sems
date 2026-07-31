### Structured Streaming Sources

- Structured Streaming is a stream processing engine built on Spark SQL that processes data incrementally and updates the final results as more streaming data arrives.
- Structured Streaming supports various sources of streaming data, such as Kafka, Flume, Kinesis, or TCP sockets, and can process the data using complex algorithms expressed with high-level functions like map, reduce, join and window.
- Structured Streaming sources can be categorized into two types: basic sources and advanced sources.
- Basic sources are sources directly available in the `spark.readStream` API, such as file systems, socket connections, and rate limiters.
- Advanced sources are sources like Kafka, Kinesis, etc. that are available through extra utility classes or external libraries.
- Some of the common properties of Structured Streaming sources are:
  - Schema: The schema of the data produced by the source, which can be specified by the user or inferred by the source.
  - Partitioning: The way the data is distributed across different partitions, which can affect the performance and fault-tolerance of the streaming query.
  - Offsets: The positions of the data within the source, which can be used to track the progress of the streaming query and resume from failures.
  - Triggers: The intervals at which the streaming query will check for new data and update the result.
  - Output modes: The way the result of the streaming query is updated, which can be append, update, or complete.