## Unit 2 - Stream-Processing Model

- A stream-processing model is a way of representing and executing computations that operate on streams of data.
- A stream is a sequence of data items that are produced and consumed over time, such as sensor readings, audio samples, video frames, network packets, etc.
- A stream-processing computation consists of one or more operators that transform, filter, aggregate, join, or split streams of data.
- A stream-processing system is a software platform that supports the development, deployment, and execution of stream-processing computations on distributed and parallel hardware.
- Stream-processing systems offer several benefits, such as:
  - Low latency: Stream-processing systems can process data as soon as it arrives, without waiting for batches or windows of data to accumulate.
  - High throughput: Stream-processing systems can scale horizontally by adding more nodes or partitions to handle larger volumes of data.
  - Fault tolerance: Stream-processing systems can handle failures of nodes or network links by replicating state and data across multiple nodes or regions.
  - Stateful processing: Stream-processing systems can maintain and update state information across multiple data items, such as counters, windows, aggregations, joins, etc.
  - Complex event processing: Stream-processing systems can detect and respond to patterns or anomalies in streams of data, such as alerts, trends, correlations, etc.

- Some examples of stream-processing systems are Apache Kafka, Apache Flink, Apache Spark Streaming, Apache Storm, Google Dataflow, etc.