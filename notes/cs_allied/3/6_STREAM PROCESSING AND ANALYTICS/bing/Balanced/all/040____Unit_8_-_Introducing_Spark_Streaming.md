## Unit 8 - Introducing Spark Streaming

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
- Spark Streaming can ingest data from various sources, such as Kafka, Flume, Twitter, ZeroMQ, Kinesis, or TCP sockets, and process them using complex algorithms expressed with high-level functions like map, reduce, join, and window.
- Spark Streaming can also integrate with advanced analytics libraries, such as MLlib and GraphX, and write the processed data to various systems, such as HDFS, HBase, Cassandra, or Elasticsearch.
- Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data divided into small batches.
- DStreams can be created either from input data streams from sources such as Kafka, Flume, and Kinesis, or by applying high-level operations on other DStreams.
- Internally, each DStream is represented as a sequence of RDDs, which are Spark's core abstraction for distributed datasets.
- Spark Streaming leverages Spark's fast scheduling capability to perform streaming analytics, by launching a new batch of jobs to process each RDD in the DStream.
- Spark Streaming provides two categories of built-in streaming sources:

  - Basic sources: Sources directly available in the Spark Streaming API, such as file systems, and socket connections.
  - Advanced sources: Sources like Kafka, Flume, Kinesis, etc. are available through extra utility classes. These require linking against extra dependencies as discussed in the linking section.

- Spark Streaming also provides an API for defining custom sources, which will be covered in a later unit.