## Unit 2 - Stream-Processing Model

- A stream-processing model is a way of designing and implementing software systems that can handle continuous and unbounded streams of data.
- A stream is a sequence of data items that arrives over time, such as sensor readings, tweets, web clicks, etc.
- A stream-processing system is composed of one or more stream sources, stream operators, and stream sinks.
- A stream source is a component that produces data items and sends them to a stream operator or a stream sink.
- A stream operator is a component that consumes data items from one or more stream sources, performs some computation or transformation on them, and sends the results to another stream operator or a stream sink.
- A stream sink is a component that consumes data items from one or more stream sources or stream operators, and performs some action or output on them, such as storing, displaying, or sending them to another system.
- A stream-processing system can be represented by a directed acyclic graph (DAG), where the nodes are stream sources, stream operators, and stream sinks, and the edges are data flows between them.
- A stream-processing system can have different properties and requirements, such as scalability, fault-tolerance, latency, throughput, consistency, etc.
- A stream-processing system can use different techniques and tools to achieve these properties and requirements, such as parallelism, partitioning, replication, state management, windowing, watermarking, etc.