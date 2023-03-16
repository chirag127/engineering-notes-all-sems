## Unit 2 - Stream-Processing Model

- A stream-processing model is a computational model that processes data as a sequence of elements, called a stream, without storing the entire data in memory.
- A stream-processing model can handle large-scale, real-time, and distributed data processing applications, such as web analytics, sensor networks, social media analysis, etc.
- A stream-processing model consists of three main components: sources, operators, and sinks.
  - Sources are the entities that produce data elements and send them to the operators.
  - Operators are the functions that transform, filter, aggregate, or join data elements from one or more streams.
  - Sinks are the entities that consume data elements from the operators and output them to external systems, such as databases, files, or dashboards.
- A stream-processing model can be represented as a directed acyclic graph (DAG), where the nodes are the sources, operators, and sinks, and the edges are the data flows between them.
- A stream-processing model can be implemented using various frameworks, such as Apache Spark, Apache Flink, Apache Storm, Apache Kafka, etc.
- A stream-processing model has several advantages, such as:
  - Low latency: It can process data elements as soon as they arrive, without waiting for batches or windows of data.
  - Scalability: It can handle large volumes and high velocities of data by parallelizing and distributing the computation across multiple nodes.
  - Fault tolerance: It can recover from failures by checkpointing the state of the operators and replaying the data from the sources.
  - Flexibility: It can support various types of data, such as structured, unstructured, or semi-structured, and various types of operators, such as map, filter, reduce, join, window, etc.