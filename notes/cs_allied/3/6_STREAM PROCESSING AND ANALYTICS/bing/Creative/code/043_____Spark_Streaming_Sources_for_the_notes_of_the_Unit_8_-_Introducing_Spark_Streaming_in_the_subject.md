### Spark Streaming Sources

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams . Spark Streaming can ingest data from various sources, such as:

- **Streaming data sources**: These are sources that produce data continuously in real time, such as Kafka, Flume, Kinesis, etc. Spark Streaming can consume data from these sources using built-in or external libraries, and process them using complex algorithms expressed with high-level functions like map, reduce, join and window.
- **Static data sources**: These are sources that store data in a fixed format, such as MySQL, MongoDB, Cassandra, etc. Spark Streaming can read data from these sources using Spark SQL or Spark DataFrames, and join them with streaming data for advanced analytics.
- **TCP sockets**: These are sources that allow data to be sent and received over a network using the TCP protocol. Spark Streaming can create a DStream (discretized stream) from any host and port that is sending data as text or binary.
- **Twitter**: This is a source that allows data to be collected from the Twitter API. Spark Streaming can create a DStream from a set of keywords or user IDs that are used to filter tweets.

Spark Streaming provides a high-level abstraction called DStream, which represents a continuous stream of data. DStreams can be created from various sources as mentioned above, or by applying transformations on other DStreams. DStreams can be output to various destinations, such as file systems, databases, and live dashboards.

Spark Streaming also supports Structured Streaming, which is a higher-level API that allows stream processing using Spark SQL and DataFrames. Structured Streaming provides a unified way of dealing with both static and streaming data sources, and allows users to express their queries using SQL or the Dataset API. Structured Streaming handles the incremental and continuous execution of the queries, and provides end-to-end guarantees of exactly-once processing.