## Unit 8 - Introducing Spark Streaming

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams. Spark Streaming can ingest data from various sources, such as Kafka, Flume, Twitter, ZeroMQ, Kinesis, or TCP sockets, and process them using complex algorithms expressed with high-level functions like map, reduce, join, and window. The processed data can be pushed out to file systems, databases, dashboards, or live applications.

Some of the key features of Spark Streaming are:

- It supports both batch and stream processing, allowing the same code to be used for both scenarios.
- It integrates seamlessly with other Spark components, such as Spark SQL, Spark MLlib, and Spark GraphX, enabling rich analytics on streaming data.
- It provides a high-level abstraction called discretized streams or DStreams, which represent a continuous stream of data divided into small batches. DStreams can be transformed and combined using various operations, such as map, filter, reduceByKey, join, and window.
- It supports stateful stream processing, where the state of the computation can be maintained and updated across batches. This enables applications such as session analysis, user behavior analysis, and machine learning.
- It supports checkpointing and write-ahead logs, which ensure fault-tolerance and exactly-once semantics in the event of failures. Checkpointing periodically saves the state of the computation to a reliable storage system, while write-ahead logs record the received data to a fault-tolerant file system before processing.
- It supports dynamic resource allocation, which allows Spark to scale up or down the number of executors based on the workload. This enables efficient resource utilization and cost savings.