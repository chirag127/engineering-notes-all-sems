### Spark Streaming Sources

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams . Spark Streaming can ingest data from various sources, such as:

- **Streaming data sources**: These are sources that produce data continuously in real time, such as Kafka, Flume, Kinesis, etc. Spark Streaming can consume data from these sources using built-in or external libraries, and process them using the Spark Streaming engine .
- **Static data sources**: These are sources that store data in a fixed format, such as MySQL, MongoDB, Cassandra, etc. Spark Streaming can read data from these sources using the Spark SQL API, and join them with streaming data for complex analysis .
- **TCP sockets**: These are sources that send data over a network connection, such as a web server or a sensor. Spark Streaming can read data from TCP sockets using the `socketTextStream` or `socketStream` methods, and parse them as text or binary data.
- **Twitter**: This is a source that provides access to the Twitter streaming API, which allows users to filter tweets by keywords, users, or locations. Spark Streaming can read data from Twitter using the `TwitterUtils` class, and process them as `Status` objects.

Spark Streaming provides a high-level abstraction called **discretized stream** or **DStream**, which represents a continuous stream of data divided into small batches. Each batch is a Spark RDD, which can be transformed and outputted using the Spark API .

Spark Streaming also supports **structured streaming**, which is a higher-level API that allows users to express streaming computations using SQL queries or DataFrames. Structured streaming provides a unified model for batch and streaming processing, and handles the incremental and continuous execution of the queries automatically.