## Unit 8 - Introducing Spark Streaming

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
- Data can be ingested from many sources like Kafka, Flume, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.
- Spark Streaming provides two main abstractions: DStreams and Structured Streaming.
- DStreams are sequences of RDDs that represent a continuous stream of data. DStreams can be created from various sources and can be transformed using operations similar to those available on RDDs. DStreams can also be output to external systems like HDFS, databases, or dashboards.
- Structured Streaming is a high-level API that allows users to express streaming computations the same way they would express batch computations on static data, using Spark SQL or DataFrames. Structured Streaming automatically handles the incremental and continuous execution of queries, while providing the same fault-tolerance and scalability guarantees as Spark Streaming.
- Spark Streaming supports various streaming sources and sinks, such as Kafka, Flume, Kinesis, HDFS, JDBC, console, etc. It also integrates with Spark SQL, MLlib, and GraphX libraries to enable various types of analysis on streaming data.