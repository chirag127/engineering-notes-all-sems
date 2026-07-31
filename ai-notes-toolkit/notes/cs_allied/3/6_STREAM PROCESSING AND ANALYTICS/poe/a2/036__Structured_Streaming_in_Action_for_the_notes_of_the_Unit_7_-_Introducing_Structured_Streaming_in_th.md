 Here is the content in Markdown format without any emojis or external links:

### Structured Streaming in Action

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- It enables rapid generation of resilient incremental queries and analytics on unbounded data streams.
- Structured Streaming can process data streams from Kafka, Flume, Kinesis, or TCP sockets, and can output to sinks such as Kafka, Cassandra, and File systems.
- Some key benefits of Structured Streaming are:
-- Exactly-once semantics: processed data is consistent and accurate even with restarts and failures.
-- Low latency: can process data with latencies as low as a few seconds.
-- Scalability: can scale to process streams with throughput of millions of messages per second.
-- Fault tolerance: can handle machine failures and accommodate high availability with minimal data loss or duplication.
-- Easy integration with Spark SQL and the Spark ecosystem.
- The core abstraction in Structured Streaming is a continuous query on a streaming source, which generates incrementally updated results as data arrives.
- Some important configurations and concepts in Structured Streaming are:
-- Stream – represents an unbounded data source or sink.
-- Checkpoint – periodically saves the state of a streaming query in a reliable, fault-tolerant storage system.
-- Trigger – specifies when results should be materialized based on time or processing records.
-- Output mode – can output complete batches (micro-batches) or latest records (continuous).
-- Watermark – tracks event time progress and can be used for late arrival handling and to generate punctuations.