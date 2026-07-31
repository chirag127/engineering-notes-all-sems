 Here is the formal content in Markdown format without any emojis or external links within the header ## Unit 8 - Introducing Spark Streaming:

## Unit 8 - Introducing Spark Streaming

1. Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
2. Spark Streaming receives live input data streams and divides the streams into batches, which are then processed by the Spark engine to generate the final results in batches.
3. The key benefits of Spark Streaming are:
- Integrated with the Spark core API, so developers can reuse their RDD and DataFrame knowledge.
- High throughput and scalability.
- Fault-tolerant guarantees through the use of RDDs.
- Complex stream processing through the use of high-level operators.
4. Input sources - File systems, Flume, Kafka, Twitter, ZeroMQ.
Output operations - Save to file systems, databases, dashboards.
5. Transformations on DStreams (Streaming RDDs) include map, reduce, filter, window operations (sliding window, tumbling window), and joining with static data.
6. Checkpoints can be enabled to recover from failures and scale to cluster changes.
7. Use-cases:
- Analytics on live data streams
- Machine learning on data streams
- Continuous applications