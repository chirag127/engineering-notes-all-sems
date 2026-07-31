### The Spark Streaming Execution Model

Spark Streaming is a module of Apache Spark that enables scalable, high-throughput, fault-tolerant stream processing of live data streams. It uses the same core engine and APIs as Spark for batch processing, but extends them to handle streaming data in a unified way. 

Some of the key features of Spark Streaming are:

- It supports a variety of data sources, such as Kafka, Flume, Kinesis, TCP sockets, etc.
- It allows applying transformations and actions on streaming data, such as map, filter, reduce, join, window, etc.
- It integrates with Spark SQL, MLlib, GraphX, and other Spark libraries for advanced analytics on streaming data.
- It provides a high-level abstraction called **structured streaming**, which allows expressing streaming computations using the Dataset/DataFrame API and SQL queries.
- It provides a low-level abstraction called **discretized stream (DStream)**, which represents a continuous stream of RDDs (Resilient Distributed Datasets).

The execution model of Spark Streaming is based on the following concepts:

- **Micro-batch**: Spark Streaming processes streaming data as a series of small batches, each containing a slice of the data received during a short time interval. The size and frequency of the batches can be configured by the user. Each batch is treated as a regular Spark job and distributed across the cluster for parallel processing.
- **Receiver**: Spark Streaming uses one or more receivers to ingest data from different sources and store them in Spark's memory. Each receiver runs as a long-running task on an executor and creates a DStream for the received data. The receivers can be customized to handle different types of data and protocols.
- **Output operation**: Spark Streaming allows applying output operations on DStreams, such as print, save, foreach, etc. These operations trigger the actual execution of the streaming computation and produce the final results. The output operations can be performed on the entire stream or on a windowed subset of the stream.

The following diagram illustrates the Spark Streaming execution model:

![Spark Streaming Execution Model](https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2019/12/spark-streaming-execution-flow.jpg)

Source: