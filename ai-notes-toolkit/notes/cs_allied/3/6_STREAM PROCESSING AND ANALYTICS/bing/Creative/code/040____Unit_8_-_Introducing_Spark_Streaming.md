## Unit 8 - Introducing Spark Streaming

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
- Data can be ingested from many sources like Kafka, Flume, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.
- Spark Streaming provides a unified platform for both batch and stream processing, allowing the same code to be reused for both scenarios.
- Spark Streaming supports two types of streaming sources: 
  - Discretized Streams (DStreams), which are a sequence of RDDs representing a continuous stream of data.
  - Structured Streaming, which is a high-level API that allows users to express streaming computations using SQL queries or DataFrames.
- Spark Streaming provides various output modes to write the results of streaming queries to external systems, such as append, update, and complete modes.
- Spark Streaming also provides various stateful operations to maintain and update the state of streaming computations over time, such as mapWithState, updateStateByKey, and stateful aggregations.