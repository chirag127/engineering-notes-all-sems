### Spark Streaming Sources

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams . Spark Streaming can ingest data from various sources, such as:

- **Streaming data sources**: These are sources that produce data continuously in real time, such as Kafka, Flume, Kinesis, etc. Spark Streaming can consume data from these sources using built-in or external libraries, and process them using complex algorithms expressed with high-level functions like map, reduce, join and window .
- **Static data sources**: These are sources that store data in a fixed format, such as MySQL, MongoDB, Cassandra, etc. Spark Streaming can read data from these sources using Spark SQL or DataFrames, and join them with streaming data for advanced analytics .
- **TCP sockets**: These are sources that allow data to be sent and received over a network using the TCP protocol. Spark Streaming can create a DStream (discretized stream) from a TCP socket, and process the data as text or binary.
- **Twitter**: This is a source that allows Spark Streaming to connect to the Twitter Streaming API and receive tweets in real time. Spark Streaming can filter, transform and analyze the tweets using various libraries, such as Spark MLlib or Spark GraphX.

Spark Streaming provides a high-level abstraction called **DStream**, which represents a continuous stream of data. A DStream can be created from various sources, or transformed from other DStreams using operations like map, filter, reduceByKey, etc. A DStream can also be output to various destinations, such as file systems, databases, or live dashboards .

Spark Streaming also supports **Structured Streaming**, which is a higher-level API that allows users to express their streaming computation as a SQL query or a DataFrame operation. Structured Streaming can handle both streaming and batch data sources, and provides a unified and consistent view of the data. Structured Streaming can also handle complex event-time and stateful processing, and provide end-to-end exactly-once fault-tolerance guarantees.