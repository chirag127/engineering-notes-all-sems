### Unit 7 - Introducing Structured Streaming
#### Structured Streaming Sources

1. **File source**: Reads files written in a directory as a stream of data. Supported file formats are text, CSV, JSON, ORC, Parquet, Avro (from Spark 2.4), and Delta Lake (from Spark 3.0).
2. **Kafka source**: Reads data from Kafka. Supports subscribing to topics, partitions, and custom offsets.
3. **Socket source (for testing)**: Reads text data from a socket connection. Designed for testing and should not be used in production.
4. **Rate source (for testing)**: Provides a stream of data with a fixed number of rows per second. Designed for testing and should not be used in production.
5. **Custom sources**: Users can create their own custom sources by extending the `org.apache.spark.sql.sources.v2.DataSourceV2` interface and implementing the required methods.