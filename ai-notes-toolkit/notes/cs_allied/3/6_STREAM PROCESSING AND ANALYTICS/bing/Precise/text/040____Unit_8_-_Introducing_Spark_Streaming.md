## Unit 8 - Introducing Spark Streaming

1. Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
2. Data can be ingested from many sources like Kafka, Flume, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.
3. Finally, processed data can be pushed out to filesystems, databases, and live dashboards.
4. In addition, Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data.
5. DStreams can be created either from input data streams from sources such as Kafka, Flume, and Kinesis, or by applying high-level operations on other DStreams.
6. Internally, a DStream is represented as a sequence of RDDs.
7. Spark Streaming provides a simple and expressive programming model to define streaming computations, and provides strong guarantees on the processing of data.
8. It is designed to be easy to use, scalable, and fault-tolerant.
9. Spark Streaming is used in a wide range of use cases, including log processing, fraud detection, and real-time data analytics.