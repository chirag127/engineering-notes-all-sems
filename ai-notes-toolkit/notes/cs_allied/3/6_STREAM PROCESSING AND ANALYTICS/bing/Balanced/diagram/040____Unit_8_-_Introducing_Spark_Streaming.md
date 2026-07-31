## Unit 8 - Introducing Spark Streaming

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
- Data can be ingested from many sources like Kafka, Flume, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.
- Finally, processed data can be pushed out to filesystems, databases, and live dashboards.
- Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data.
- DStreams can be created either from input data streams from sources such as Kafka, Flume, and Kinesis, or by applying high-level operations on other DStreams.
- Internally, a DStream is represented as a sequence of RDDs.
- Spark Streaming receives live input data streams and divides the data into batches, which are then processed by the Spark engine to generate the final stream of results in batches.
- Spark Streaming provides two categories of built-in streaming sources:
  - Basic sources: Sources directly available in the Spark Streaming API. Examples are file systems, and socket connections.
  - Advanced sources: Sources like Kafka, Flume, Kinesis, etc. are available through extra utility classes. These require linking against extra dependencies.
- Spark Streaming also provides API for defining custom sources.
- Spark Streaming supports two types of output operations:
  - Basic output operations: These write data to an external system in a standard format. Examples are `print()`, `saveAsTextFiles()`, `saveAsHadoopFiles()`, etc.
  - Foreach output operation: This allows the user to write arbitrary code to send the output data to an external system. This is useful when the user wants to use a custom protocol or a custom data format.