# The Spark Streaming Execution Model

Spark Streaming is a module of Apache Spark that enables scalable, high-throughput, fault-tolerant stream processing of live data streams. It is based on the Spark core engine and the Spark SQL engine, and provides a unified programming model for batch and streaming data processing.

The main concepts and components of the Spark Streaming execution model are:

- **DStream**: A DStream (discretized stream) is a sequence of RDDs (resilient distributed datasets) that represent a continuous stream of data. DStreams can be created from various sources, such as Kafka, Flume, sockets, or custom receivers. DStreams can also be transformed using high-level operations, such as map, filter, reduce, join, window, etc. DStreams can also be output to external systems, such as HDFS, databases, dashboards, etc.

- **Micro-batch**: Spark Streaming processes data in small batches, called micro-batches, instead of processing data one record at a time. This allows Spark Streaming to leverage the batch processing capabilities of Spark and achieve high performance and fault tolerance. The size and frequency of the micro-batches can be configured by the user, depending on the latency and throughput requirements of the application.

- **Receiver**: A receiver is a component that runs on a worker node and receives data from a source, such as Kafka, Flume, sockets, etc. The receiver then stores the data in the memory of the worker node as an RDD, and sends metadata to the driver node. The driver node then schedules the processing of the RDDs by the executor nodes. There can be multiple receivers running in parallel, each receiving data from a different source or partition.

- **Driver**: The driver is the main program that runs on the master node and coordinates the execution of the Spark Streaming application. The driver maintains the state of the DStreams, the metadata of the RDDs, and the scheduling of the tasks. The driver also periodically runs a streaming query planner that analyzes the DStreams and their dependencies, and generates a physical execution plan for each micro-batch.

- **Executor**: An executor is a process that runs on a worker node and executes the tasks assigned by the driver. An executor can run multiple tasks in parallel, each task processing a partition of an RDD. An executor can also cache RDDs in memory or disk for reuse.

The following diagram illustrates the Spark Streaming execution model:

![Spark Streaming Execution Model](https://www.databricks.com/wp-content/uploads/2015/07/Spark-Streaming-Execution-Model.png)

Source: [Diving into Apache Spark Streaming's Execution Model - Databricks](https://www.databricks.com/blog/2015/07/30/diving-into-apache-spark-streamings-execution-model.html)