### Structured Streaming Sources

Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. It allows you to express your streaming computation the same way you would express a batch computation on static data. The Spark engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive.

Structured Streaming supports the following sources of data:

1. **File source**: Reads files written in a directory as a stream of data. Supported file formats are text, CSV, JSON, ORC, Parquet, Avro (from Spark 2.4), and Delta Lake (from Spark 3.0).
2. **Kafka source**: Reads data from Kafka. It’s compatible with Kafka broker versions 0.10.0 or higher.
3. **Socket source (for testing)**: Reads text data from a socket connection. The listening server socket is at the driver. Note that this should be used only for testing as this does not provide end-to-end fault-tolerance guarantees.
4. **Rate source (for testing)**: Generates data at the specified number of rows per second, each output row contains a timestamp and value.

These are the sources of data that can be used with Structured Streaming. It is important to choose the appropriate source for your use case to ensure efficient and reliable processing of your streaming data.