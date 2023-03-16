### Spark Streaming Sources

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams .
- Spark Streaming can ingest data from various sources, such as:
  - Streaming data sources, such as Kafka, Flume, Kinesis, etc. These sources provide data in a continuous and asynchronous manner, and can handle high volumes and velocities of data .
  - Static data sources, such as MySQL, MongoDB, Cassandra, etc. These sources provide data in a batch or query-based manner, and can be used to enrich or join with streaming data .
  - TCP sockets, which allow data to be sent over a network connection using a simple protocol.
  - Twitter, which allows data to be collected from the Twitter API using a specific query or filter.
- Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data divided into small batches .
- Spark Streaming also supports Structured Streaming, which is a higher-level API that allows users to express streaming computations using SQL queries or DataFrames.
- Spark Streaming sources can be categorized into two types: basic and advanced.
  - Basic sources are the ones that are built into the core Spark Streaming API, such as file systems, sockets, and actors.
  - Advanced sources are the ones that are provided by external projects or libraries, such as Kafka, Flume, Kinesis, etc. These sources require additional dependencies and configurations to be used with Spark Streaming.