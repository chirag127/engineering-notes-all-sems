### Structured Streaming Sources

- Structured Streaming is a stream processing engine built on Spark SQL that processes data incrementally and updates the final results as more streaming data arrives.
- Structured Streaming supports various sources of streaming data, such as Kafka, Flume, Kinesis, or TCP sockets, and can run on various file formats and storage systems such as Parquet, JSON, ORC, Avro, and HDFS.
- Structured Streaming sources can be classified into two types: basic sources and advanced sources.
- Basic sources are sources directly available in the `spark.readStream` API, such as file systems, socket connections, and rate limiters.
- Advanced sources are sources like Kafka, Kinesis, etc. that are available through extra utility classes or external libraries.
- Structured Streaming sources can be configured with various options, such as schema, format, partitioning, watermarking, and trigger.
- Structured Streaming sources can be used to create DataFrames or Datasets that represent the streaming data, and then apply various transformations and output operations on them.
- Structured Streaming sources can also be integrated with REST API destinations, such as Macrometa, to enable scalable and reliable data delivery to various cloud services.