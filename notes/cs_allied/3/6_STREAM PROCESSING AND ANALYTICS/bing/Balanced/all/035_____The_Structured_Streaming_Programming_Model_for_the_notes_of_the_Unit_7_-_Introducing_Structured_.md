# The Structured Streaming Programming Model

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine .
- The key idea in Structured Streaming is to treat a live data stream as a table that is being continuously appended   .
- This leads to a new stream processing model that is very similar to a batch processing model   .
- You can express your streaming computation the same way you would express a batch computation on static data .
- You can use the Dataset/DataFrame API to create streaming DataFrames/Datasets from streaming sources such as Kafka, Flume, and more .
- You can apply the same operations on streaming DataFrames/Datasets that you can on static ones, such as filtering, aggregating, joining, etc .
- You can write the results of your streaming computation to streaming sinks such as Kafka, memory, console, etc .
- Structured Streaming ensures end-to-end exactly-once fault-tolerance guarantees through checkpointing and Write-Ahead Logs .
- Structured Streaming provides rich semantics for handling late and out-of-order data using watermarking and windowing .
- Structured Streaming supports both event-time and processing-time based triggers for controlling the frequency and latency of result updates .
- Structured Streaming leverages the Spark SQL engine to perform optimizations such as predicate pushdown, projection pruning, and code generation .
- Structured Streaming exposes a low-level API for extending the built-in sources and sinks, and integrating with external systems .