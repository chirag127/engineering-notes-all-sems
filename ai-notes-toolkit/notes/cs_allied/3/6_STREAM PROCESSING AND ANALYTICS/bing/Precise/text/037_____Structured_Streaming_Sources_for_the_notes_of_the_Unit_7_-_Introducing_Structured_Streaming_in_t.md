### Structured Streaming Sources

Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. It allows you to express your streaming computation the same way you would express a batch computation on static data. The Spark engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive.

Structured Streaming supports the following sources of data for streaming:

1. **File source**: Reads files written in a directory as a stream of data. Supported file formats are text, CSV, JSON, ORC, and Parquet. The file source is available for both Scala and Python.

2. **Kafka source**: Reads data from Kafka. The Kafka source is available for both Scala and Python.

3. **Socket source**: Reads data from a socket connection. The socket source is available for both Scala and Python.

4. **Rate source**: Generates data at the specified number of rows per second. The rate source is available for both Scala and Python.

5. **Custom sources**: You can also define your own streaming source by extending the `org.apache.spark.sql.execution.streaming.Source` interface.

These sources can be used to read data in a structured manner and perform real-time processing on the incoming data. The processed data can then be written to various sinks such as files, databases, or message queues. This allows for a flexible and powerful stream processing pipeline.