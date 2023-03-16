# Spark Streaming Sources

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams . Spark Streaming can ingest data from various sources, such as:

- **Streaming data sources**: These are sources that produce data continuously in real time, such as Kafka, Flume, Kinesis, etc. Spark Streaming can consume data from these sources using built-in or custom receivers.
- **Static data sources**: These are sources that store data in a fixed format, such as MySQL, MongoDB, Cassandra, etc. Spark Streaming can read data from these sources using Spark SQL or Spark DataFrames.
- **TCP sockets**: These are sources that send data over a network connection using the TCP protocol. Spark Streaming can read data from these sources using the socketTextStream or socketStream methods.
- **Twitter**: This is a source that provides access to the Twitter streaming API. Spark Streaming can read data from this source using the TwitterUtils class.

Spark Streaming provides a high-level abstraction called **discretized stream** or **DStream**, which represents a continuous stream of data divided into small batches. A DStream can be created from any of the above sources, or by applying transformations on other DStreams. A DStream can be processed using various built-in functions, complex algorithms, or Spark SQL queries. The processed data can be pushed out to file systems, databases, or live dashboards.

Spark Streaming also supports **structured streaming**, which is a higher-level API that allows users to express streaming computations using Spark SQL or DataFrames. Structured streaming provides a unified way of processing both streaming and batch data, and handles the complexities of stream processing such as state management, fault tolerance, and output consistency. Structured streaming can read data from various sources, such as:

- **File source**: This is a source that monitors a directory for new files and reads them as a stream of data. The files can be in any format supported by Spark SQL, such as CSV, JSON, Parquet, etc.
- **Kafka source**: This is a source that reads data from Apache Kafka, a popular distributed messaging system. The Kafka source can subscribe to one or more topics and read data from different partitions in parallel.
- **Socket source**: This is a source that reads data from a TCP socket. The socket source is mainly for testing and debugging purposes, and should not be used in production.
- **Rate source**: This is a source that generates data at a specified rate for testing and benchmarking purposes. The rate source produces rows with a single timestamp column and a value column that increases linearly.

Structured streaming can write data to various sinks, such as:

- **File sink**: This is a sink that writes data to a file system. The files can be in any format supported by Spark SQL, such as CSV, JSON, Parquet, etc. The file sink can also partition the output by a given column or expression.
- **Kafka sink**: This is a sink that writes data to Apache Kafka. The Kafka sink can write data to one or more topics and specify the key and value columns.
- **Console sink**: This is a sink that prints data to the standard output. The console sink is mainly for testing and debugging purposes, and should not be used in production.
- **Memory sink**: This is a sink that collects data in memory and allows users to query it using Spark SQL or DataFrames. The memory sink is mainly for testing and debugging purposes, and should not be used in production.
- **Foreach sink**: This is a sink that allows users to apply arbitrary logic to each row of data using a custom function. The foreach sink can be used to write data to custom destinations or perform side effects.