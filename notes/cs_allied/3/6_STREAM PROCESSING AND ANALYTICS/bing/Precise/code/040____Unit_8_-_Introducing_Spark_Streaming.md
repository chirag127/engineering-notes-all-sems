## Unit 8 - Introducing Spark Streaming

1. **Overview:** Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
2. **Data sources:** Data can be ingested from many sources like Kafka, Flume, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.
3. **Output:** Processed data can be pushed out to filesystems, databases, and live dashboards.
4. **Micro-batching:** Spark Streaming receives live input data streams and divides the data into batches, which are then processed by the Spark engine to generate the final stream of results in batches.
5. **Integration:** Spark Streaming seamlessly integrates with other Spark components, including Spark SQL, Spark MLlib, and GraphX, allowing users to combine stream processing with more complex analytics.
6. **Fault-tolerance:** Spark Streaming provides strong guarantees for the end-to-end fault-tolerance of its processing, ensuring that data is reliably processed even in the face of failures.
7. **Use cases:** Spark Streaming is used for a variety of use cases, including real-time data analytics, fraud detection, log processing, and monitoring.