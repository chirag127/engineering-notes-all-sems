### Spark Streaming Sources

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams .
- Spark Streaming can ingest data from various sources, such as Kafka, Flume, Kinesis, TCP sockets, Twitter, etc .
- Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data as a sequence of RDDs .
- Spark Streaming also supports structured streaming, which is a high-level API that allows users to express streaming computations using SQL queries or DataFrames.
- Spark Streaming sources can be classified into two types: basic sources and advanced sources.
  - Basic sources are the ones that are built into the core Spark Streaming API, such as file systems, sockets, and Akka actors.
  - Advanced sources are the ones that are provided by external projects or libraries, such as Kafka, Flume, Kinesis, etc.
- Spark Streaming sources can be configured using various parameters, such as batch interval, parallelism, checkpointing, etc.
- Spark Streaming sources can be processed using various built-in functions, complex algorithms, or user-defined functions .
- Spark Streaming sources can be output to various sinks, such as file systems, databases, dashboards, etc  .