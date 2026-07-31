### Spark Streaming Sinks

- Spark Streaming Sinks are the components that store the output of a Spark Streaming application to external storage systems.
- Spark Streaming supports various types of sinks, such as console, file, memory, Kafka, Foreach, Delta Lake, etc.
- Each sink has its own advantages and limitations, depending on the use case and the output mode of the streaming query.
- The output mode defines how the sink should handle the new data and the existing data in the output table. There are three output modes: append, update, and complete.
- Append mode: Only the new rows appended to the result table since the last trigger are written to the sink. This is the default output mode and is supported by all sinks.
- Update mode: Only the rows that were updated in the result table since the last trigger are written to the sink. This mode is supported by some sinks, such as memory, console, and Kafka.
- Complete mode: The entire result table is written to the sink. This mode is supported by some sinks, such as memory, console, and Foreach.
- To use a sink, we need to specify the format and the options of the sink when calling the `writeStream` method on the streaming DataFrame or Dataset. For example, to use the console sink, we can write:

```scala
val query = streamingDF.writeStream
  .outputMode("append")
  .format("console")
  .start()
```

- To use the file sink, we can write:

```scala
val query = streamingDF.writeStream
  .outputMode("append")
  .format("parquet")
  .option("path", "output/path")
  .option("checkpointLocation", "checkpoint/path")
  .start()
```

- To use the Kafka sink, we can write:

```scala
val query = streamingDF.selectExpr("topic", "value")
  .writeStream
  .outputMode("update")
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("checkpointLocation", "checkpoint/path")
  .start()
```

- To use the Foreach sink, we can write:

```scala
val query = streamingDF.writeStream
  .outputMode("complete")
  .foreach(new ForeachWriter[Row] {
    // open, process, and close methods
  })
  .start()
```

- To use the Delta Lake sink, we can write:

```scala
val query = streamingDF.writeStream
  .outputMode("append")
  .format("delta")
  .option("checkpointLocation", "checkpoint/path")
  .start("output/path")
```

- For more details on the supported sinks and their options, refer to the [Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html).