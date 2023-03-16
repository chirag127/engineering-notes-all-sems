### Structured Streaming Sinks

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- A sink is a place where the output data of a stream processing job is written.
- Structured Streaming supports several built-in sinks, including file, console, memory, and Kafka.
- The file sink writes the output data to a file system, such as HDFS or a local file system.
- The console sink writes the output data to the console, which is useful for debugging and testing.
- The memory sink writes the output data to memory, which is useful for interactive queries and testing.
- The Kafka sink writes the output data to a Kafka topic.
- Custom sinks can also be implemented using the `DataStreamWriter.foreach` or `DataStreamWriter.foreachBatch` APIs.
- Sinks can be configured with various options, such as the output mode, trigger interval, and checkpoint location.
- The output mode determines how the output data is written to the sink. The supported output modes are `append`, `update`, and `complete`.
- The trigger interval determines how often the output data is written to the sink.
- The checkpoint location is used to store the progress of the stream processing job, which is used for fault tolerance and recovery.
