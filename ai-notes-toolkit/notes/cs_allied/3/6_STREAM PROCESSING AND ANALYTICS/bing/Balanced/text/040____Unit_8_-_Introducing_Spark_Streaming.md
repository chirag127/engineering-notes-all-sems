## Unit 8 - Introducing Spark Streaming

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
- Data can be ingested from many sources like Kafka, Flume, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.
- Spark Streaming provides two main abstractions: DStreams and Structured Streaming.
- DStreams are continuous sequences of RDDs that represent data coming from a stream. DStreams can be transformed and output to external systems using the same operations as RDDs.
- Structured Streaming is a higher-level API that allows users to express streaming computations using SQL queries or DataFrames. Structured Streaming automatically handles the incremental execution of the queries and provides consistency and fault-tolerance guarantees.
- Spark Streaming supports various output modes, such as append, update, and complete, to handle different types of queries and sinks.
- Spark Streaming also integrates with Spark SQL, MLlib, and GraphX, enabling users to perform advanced analytics on streaming data.