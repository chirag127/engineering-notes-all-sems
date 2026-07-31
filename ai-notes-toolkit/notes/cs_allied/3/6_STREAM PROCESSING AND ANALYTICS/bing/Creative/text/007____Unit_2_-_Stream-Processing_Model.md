## Unit 2 - Stream-Processing Model

- A stream-processing model is a computational model that processes data as a sequence of elements, called a stream, without storing the entire data in memory.
- A stream-processing model can handle large-scale, real-time, and distributed data processing applications, such as web analytics, sensor networks, social media, and machine learning.
- A stream-processing model consists of three main components: sources, operators, and sinks.
  - Sources are the entities that produce data elements and send them to the operators.
  - Operators are the functions that transform, filter, aggregate, or join data elements from one or more streams.
  - Sinks are the entities that consume data elements from the operators and output them to external systems, such as databases, files, or dashboards.
- A stream-processing model can be represented as a directed acyclic graph (DAG), where the nodes are the sources, operators, and sinks, and the edges are the data streams.
- A stream-processing model can be implemented using various frameworks, such as Apache Spark, Apache Flink, Apache Kafka, and Apache Storm.
- A stream-processing model has several advantages over a batch-processing model, such as:
  - Low latency: A stream-processing model can process data elements as soon as they arrive, without waiting for a batch to be completed, and deliver results in near real-time.
  - High scalability: A stream-processing model can scale horizontally by adding more sources, operators, or sinks, and distribute the workload across multiple nodes in a cluster.
  - High fault tolerance: A stream-processing model can handle failures and recover from them by using techniques such as checkpointing, replication, and state management.
  - High flexibility: A stream-processing model can support various types of data, such as structured, unstructured, or semi-structured, and various types of operators, such as windowing, grouping, or joining.