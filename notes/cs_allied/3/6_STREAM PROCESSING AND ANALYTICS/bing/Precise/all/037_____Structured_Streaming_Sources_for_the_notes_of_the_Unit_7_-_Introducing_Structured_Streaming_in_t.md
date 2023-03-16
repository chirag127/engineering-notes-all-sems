# Structured Streaming Sources

Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. It allows you to express your streaming computation the same way you would express a batch computation on static data. The Spark engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive.

In Structured Streaming, there are several built-in sources available for reading data from, including:

1. **File source**: Reads files written in a directory as a stream of data. Supported file formats are text, CSV, JSON, ORC, and Parquet.

2. **Kafka source**: Reads data from Kafka. It’s compatible with Kafka broker versions 0.10.0 or higher.

3. **Socket source**: Reads text data from a socket connection. The listening server socket is at the driver, and the data received from the socket is replicated to all the executors.

4. **Rate source**: Generates data at the specified number of rows per second, each output row contains a timestamp and value.

These are the main sources available in Structured Streaming, but it is also possible to define custom sources by extending the `Source` interface.