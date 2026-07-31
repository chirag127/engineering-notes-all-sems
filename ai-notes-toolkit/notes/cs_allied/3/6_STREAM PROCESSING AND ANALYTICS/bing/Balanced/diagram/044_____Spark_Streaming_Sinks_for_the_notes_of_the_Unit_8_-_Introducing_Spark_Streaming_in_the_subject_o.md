### Spark Streaming Sinks

- Spark Streaming Sinks are the components that store the output of a streaming query to an external storage system.
- Spark Structured Streaming supports the following types of sinks  :
  - **Console sink**: Displays the content of the DataFrame to the standard output. Useful for debugging purposes.
  - **File sink**: Writes the output of the streaming query to a file system, such as HDFS, S3, or local disk. Supports various formats, such as CSV, JSON, Parquet, ORC, etc.
  - **Kafka sink**: Publishes the output of the streaming query to one or more Kafka topics.
  - **Foreach sink**: Allows the user to specify a custom logic to process each row of the output. Useful for integrating with external systems that are not natively supported by Spark.
  - **Memory sink**: Stores the output of the streaming query as an in-memory table. Useful for testing and interactive queries.
  - **Delta sink**: Writes the output of the streaming query to a Delta Lake table. Supports ACID transactions, schema evolution, and time travel.
- Spark Streaming Sinks can be specified using the `writeStream` method on a DataFrame or Dataset, followed by the `format` method to indicate the type of the sink, and the `option` or `options` methods to provide any additional configuration parameters. For example :

```scala
// Write to a file sink in Parquet format
val query = df.writeStream
  .format("parquet")
  .option("path", "path/to/destination/dir")
  .option("checkpointLocation", "path/to/checkpoint/dir")
  .start()

// Write to a Kafka sink with a specific topic
val query = df.selectExpr("topic", "value").writeStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("checkpointLocation", "path/to/checkpoint/dir")
  .start()

// Write to a foreach sink with a custom logic
val query = df.writeStream
  .foreach(new ForeachWriter[Row] {
    // Open a connection to the external system
    def open(partitionId: Long, epochId: Long): Boolean = {
      // ...
    }
    // Write each row to the external system
    def process(row: Row): Unit = {
      // ...
    }
    // Close the connection to the external system
    def close(errorOrNull: Throwable): Unit = {
      // ...
    }
  })
  .start()
```
- Spark Streaming Sinks can also be categorized based on the output mode they support :
  - **Append mode**: Only the new rows appended to the result table since the last trigger are written to the sink. This is the default mode and is supported by all sinks except memory sink.
  - **Complete mode**: The entire updated result table is written to the sink. This mode is supported by console sink, file sink, memory sink, and delta sink.
  - **Update mode**: Only the rows that were updated in the result table since the last trigger are written to the sink. This mode is supported by console sink, memory sink, and delta sink.