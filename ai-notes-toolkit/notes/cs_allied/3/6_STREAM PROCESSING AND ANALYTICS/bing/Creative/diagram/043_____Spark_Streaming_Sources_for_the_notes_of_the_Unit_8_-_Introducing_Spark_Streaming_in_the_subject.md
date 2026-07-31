### Spark Streaming Sources

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams . Spark Streaming can ingest data from various sources, such as:

- **Streaming data sources**: These are sources that produce data continuously in real time, such as Kafka, Flume, Kinesis, etc. Spark Streaming can consume data from these sources using built-in or custom receivers.
- **Static data sources**: These are sources that store data in a fixed format, such as MySQL, MongoDB, Cassandra, etc. Spark Streaming can read data from these sources using Spark SQL or the DataFrame API.
- **TCP sockets**: These are sources that send data over a network connection using the TCP protocol. Spark Streaming can read data from these sources using the socketTextStream or socketStream methods.
- **Twitter**: This is a source that provides access to the Twitter streaming API. Spark Streaming can read data from this source using the TwitterUtils class.

Spark Streaming provides a high-level abstraction called **discretized stream** or **DStream**, which represents a continuous stream of data divided into small batches. A DStream can be created from any of the above sources, or by applying transformations on other DStreams. A DStream can be processed using various built-in or user-defined functions, such as map, reduce, join, window, etc. A DStream can also be output to various destinations, such as file systems, databases, or live dashboards.

Spark Streaming also supports **structured streaming**, which is a higher-level API that allows users to express their streaming computation as a SQL query or a DataFrame operation. Structured streaming provides a unified and consistent way of processing both streaming and batch data, and handles the complexities of stream processing, such as incremental state management, event-time processing, late data handling, etc. Structured streaming can read data from various sources, such as Kafka, files, sockets, etc., and can write data to various sinks, such as files, consoles, memory, etc.