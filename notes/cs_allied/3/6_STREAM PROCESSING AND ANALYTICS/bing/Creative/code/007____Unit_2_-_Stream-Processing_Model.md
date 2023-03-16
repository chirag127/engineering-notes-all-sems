## Unit 2 - Stream-Processing Model

- A stream-processing model is a computational model that processes data as a continuous sequence of elements, called a stream.
- A stream can be finite or infinite, depending on the source and the termination condition of the processing.
- A stream-processing model consists of three main components: sources, operators, and sinks.
- Sources are the entities that generate or provide the data elements for the stream, such as sensors, files, databases, or network connections.
- Operators are the functions that transform, filter, aggregate, or combine the data elements in the stream, such as map, filter, reduce, join, or window.
- Sinks are the entities that consume or output the data elements from the stream, such as files, databases, network connections, or displays.
- A stream-processing model can be represented as a directed graph, where the nodes are the sources, operators, and sinks, and the edges are the streams.
- A stream-processing model can be implemented using various frameworks or platforms, such as Apache Spark, Apache Flink, Apache Kafka, or Apache Storm.
- A stream-processing model has several advantages over a batch-processing model, such as:
  - It can handle real-time or near-real-time data with low latency and high throughput.
  - It can handle unbounded or dynamic data with scalability and fault-tolerance.
  - It can support complex event processing and stateful computations with windowing and checkpointing mechanisms.
- A stream-processing model also has some challenges and limitations, such as:
  - It requires careful design and tuning of the operators and the streams to avoid backpressure, memory overflow, or data loss.
  - It requires trade-offs between consistency, availability, and latency, depending on the data quality and the application requirements.
  - It requires proper handling of out-of-order, duplicate, or missing data elements, using techniques such as watermarking, deduplication, or retraction.