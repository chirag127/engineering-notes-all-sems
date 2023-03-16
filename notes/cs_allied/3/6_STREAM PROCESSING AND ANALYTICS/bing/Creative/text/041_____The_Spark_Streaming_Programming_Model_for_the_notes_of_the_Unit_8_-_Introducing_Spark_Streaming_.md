### The Spark Streaming Programming Model

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
- Spark Streaming provides a high-level abstraction called **discretized stream** or **DStream**, which represents a continuous stream of data.
- DStreams can be created either from input data sources such as Kafka, Flume, Kinesis, or TCP sockets, or by applying high-level operations on other DStreams .
- DStreams are internally represented as a sequence of **RDDs** (Resilient Distributed Datasets), which are Spark's core abstraction for distributed data.
- Each RDD in a DStream contains data from a certain interval, called a **batch interval**.
- Spark Streaming processes the live data streams using a **micro-batch** processing model, where the streaming computation is divided into small batches that are executed periodically .
- The batch interval can be configured based on the latency and throughput requirements of the application.
- Spark Streaming leverages Spark's core engine and unified programming model to provide the same APIs, fault-tolerance, and scalability for both batch and streaming workloads  .
- Spark Streaming supports two types of APIs: the **low-level DStream API** and the **high-level Structured Streaming API**.
- The low-level DStream API allows users to manipulate DStreams using transformations and output operations, and to define custom receivers for ingesting data from various sources.
- The high-level Structured Streaming API allows users to express streaming computations using the Dataset/DataFrame API, which supports SQL queries, streaming aggregations, event-time windows, stream-to-batch joins, etc.
- The Structured Streaming API also provides a declarative way to specify the expected output mode (append, update, or complete) and the trigger interval for the streaming query.
- The Spark SQL engine will take care of running the streaming query incrementally and continuously and updating the final result as streaming data continues to arrive.