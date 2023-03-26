 Here is the content in markdown format without any emojis or external links:

### Structured Streaming Processing Model

- Structured Streaming is a Spark API for scalable, fault-tolerant, continuous stream processing.
- It enables high-throughput, scalable processing of live data streams.
- The key capabilities of Structured Streaming are:

1. Integrated API for streaming and batch
Structured Streaming uses the Spark SQL engine and DataFrame/Dataset API, so that the same API can be used for both batch and streaming data.

2. Fault tolerance and scalability
Structured Streaming inherits the fault-tolerance and scalability guarantees of Spark.

3. Event time processing
Structured Streaming supports event time processing, which allows processing of late data and out-of-order data. This enablescapture of accurate trends even from out-of-order events.

4. Continuous queries
In addition to one-off queries, continuous queries return updates to results as new data arrives. This enables applications that continually react to new data.

5. Incremental processing
Processing can be incremental, that is, process only recently arrived data instead of all data from scratch. This improves performance for processing unbounded, continuous data.

6. Integration with other streaming engines
In addition to self-contained streaming, Structured Streaming integrates with other streaming processing engines like Kafka and Kinesis. Data can be read from such engines and processed using the Spark SQL engine.