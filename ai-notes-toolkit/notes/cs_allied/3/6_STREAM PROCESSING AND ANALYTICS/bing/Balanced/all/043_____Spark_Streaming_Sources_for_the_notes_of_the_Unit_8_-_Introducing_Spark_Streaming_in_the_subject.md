# Spark Streaming Sources

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams . Spark Streaming can ingest data from various sources, such as:

- **Streaming data sources**: These are sources that produce data continuously in real time, such as Kafka, Flume, Kinesis, etc. Spark Streaming can directly connect to these sources and consume the data as it arrives.
- **Static data sources**: These are sources that store data in a fixed format, such as MySQL, MongoDB, Cassandra, etc. Spark Streaming can periodically query these sources and process the data as batches.
- **TCP sockets**: These are sources that allow data to be sent and received over a network connection using the TCP protocol. Spark Streaming can create a socket stream that listens to a TCP port and receives text data from it.
- **Twitter**: This is a source that allows data to be collected from the Twitter API. Spark Streaming can create a Twitter stream that connects to the Twitter API and receives tweets as they are posted.

Spark Streaming provides a high-level abstraction called **discretized stream** or **DStream**, which represents a continuous stream of data. A DStream can be created from any of the above sources, or from transformations on other DStreams. A DStream can be processed using various built-in functions, complex algorithms, or user-defined functions.

Spark Streaming also supports **structured streaming**, which is a higher-level API that allows data to be processed as unbounded tables. Structured streaming can read data from various sources, such as Kafka, files, sockets, etc., and can write data to various sinks, such as files, databases, dashboards, etc. Structured streaming can process data using SQL queries, DataFrames, or Datasets.