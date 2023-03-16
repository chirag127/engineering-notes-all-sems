### Structured Streaming Sources

- Structured streaming sources are the inputs for structured streaming, which is a stream processing engine built on Spark SQL that processes data incrementally and continuously and updates the final results as more streaming data arrives.
- Structured streaming sources can be classified into two categories: basic sources and advanced sources.
- Basic sources are sources directly available in the `StreamingContext` API, such as file systems and socket connections. They can be created using the `readStream` method on a `SparkSession` object and specifying the format, schema, and options.
- Advanced sources are sources like Kafka, Kinesis, etc. that are available through extra utility classes. They can be created using the `format` method on a `DataStreamReader` object and specifying the class name of the source provider and the options.
- Some of the common options for structured streaming sources are:
  - `path`: the location of the files for file-based sources
  - `maxFilesPerTrigger`: the maximum number of files to be processed in each trigger for file-based sources
  - `subscribe` or `subscribePattern`: the topics to subscribe to for Kafka sources
  - `kafka.bootstrap.servers`: the Kafka brokers to connect to for Kafka sources
  - `startingOffsets` or `endingOffsets`: the offsets to start or end the stream for Kafka sources
- Structured streaming sources can be queried using SQL queries or DataFrame/Dataset operations, and the results can be written to structured streaming sinks using the `writeStream` method.