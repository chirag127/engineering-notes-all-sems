### Structured Streaming Processing Model

- Structured Streaming is a **scalable and fault-tolerant stream processing engine** built on the Spark SQL engine.
- Structured Streaming uses the **Dataframe and Dataset APIs** to express streaming computations, which are very similar to batch computations on static data .
- Structured Streaming treats a data stream as a **table that is being continuously appended**. This allows users to write queries using standard SQL operators and functions, and get incremental results as new data arrives .
- Structured Streaming supports various sources and sinks for streaming data, such as Kafka, Flume, files, sockets, databases, etc.
- Structured Streaming provides **exactly-once** guarantees for end-to-end pipelines, by tracking the progress of the data and automatically handling failures and retries.
- Structured Streaming also offers **query optimizations** such as predicate pushdown, projection pruning, and state management, to improve the performance and efficiency of streaming applications .
- Structured Streaming can be integrated with other Spark components, such as MLlib, GraphX, and SparkR, to enable complex analytics on streaming data.