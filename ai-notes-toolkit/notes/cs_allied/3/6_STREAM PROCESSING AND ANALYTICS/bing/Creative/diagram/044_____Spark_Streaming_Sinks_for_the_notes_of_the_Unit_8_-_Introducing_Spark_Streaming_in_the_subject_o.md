### Spark Streaming Sinks

- Spark Streaming Sinks are the components that store the output of a streaming query to an external storage system.
- Spark Structured Streaming supports the following types of sinks:
  - **File sink**: Writes the output of a streaming query as files in a directory. Supports various file formats such as CSV, JSON, Parquet, etc.
  - **Kafka sink**: Writes the output of a streaming query to one or more Kafka topics.
  - **Foreach sink**: Allows the user to specify a custom logic to process the output of a streaming query. For example, writing the output to a database or a message queue.
  - **Console sink**: Displays the output of a streaming query to the standard output. Mainly used for debugging purposes.
  - **Memory sink**: Stores the output of a streaming query as an in-memory table. Mainly used for testing purposes.
- Spark Streaming Sinks can be specified using the `writeStream` method on a `DataStreamWriter` object. The `writeStream` method takes a `format` parameter that specifies the type of the sink, and optionally some additional options that are specific to each sink.
- For example, to write the output of a streaming query to a file sink in Parquet format, one can use the following code snippet:

```scala
val query = streamingDF.writeStream
  .format("parquet")        // can be "orc", "json", "csv", etc.
  .option("path", "path/to/destination/dir")
  .option("checkpointLocation", "path/to/checkpoint/dir")
  .start()
```

- To write the output of a streaming query to a Kafka sink, one can use the following code snippet:

```scala
val query = streamingDF.selectExpr("topic", "value").writeStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("checkpointLocation", "path/to/checkpoint/dir")
  .start()
```

- To write the output of a streaming query to a console sink, one can use the following code snippet:

```scala
val query = streamingDF.writeStream
  .format("console")
  .option("truncate", false)
  .start()
```

- To write the output of a streaming query to a foreach sink, one can use the following code snippet:

```scala
val query = streamingDF.writeStream
  .foreach(new ForeachWriter[Row] {

    def open(partitionId: Long, version: Long): Boolean = {
      // open a connection to the database
    }

    def process(record: Row) = {
      // write the record to the database
    }

    def close(errorOrNull: Throwable): Unit = {
      // close the connection to the database
    }
  })
  .start()
```

- To write the output of a streaming query to a memory sink, one can use the following code snippet:

```scala
val query = streamingDF.writeStream
  .format("memory")
  .queryName("my_table")
  .start()
```

- Spark Streaming Sinks can also support different output modes, such as `append`, `update`, or `complete`, depending on the type of the query and the sink. The output mode specifies how the output of a streaming query should be written to the sink.
- For example, the `append` mode means that only the new rows that are added to the result table after the last trigger will be written to the sink. The `update` mode means that only the rows that were updated in the result table after the last trigger will be written to the sink. The `complete` mode means that the entire result table will be written to the sink after every trigger.
- The output mode can be specified using the `outputMode` method on a `DataStreamWriter` object. For example, to write the output of a streaming query to a file sink in Parquet format using the `append` mode, one can use the following code snippet:

```scala
val query = streamingDF.writeStream
  .format("parquet")        // can be "orc", "json", "csv", etc.
  .option("path", "path/to/destination/dir")
  .option("checkpointLocation", "path/to/checkpoint/dir")
  .outputMode("append")
  .start()
```

- Spark