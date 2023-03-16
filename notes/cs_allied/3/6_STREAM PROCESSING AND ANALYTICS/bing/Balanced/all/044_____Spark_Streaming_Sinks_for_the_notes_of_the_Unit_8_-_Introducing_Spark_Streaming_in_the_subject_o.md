# Spark Streaming Sinks

- Spark Streaming Sinks are the components that store the results of a streaming query into external storage systems.
- Spark Structured Streaming supports various types of sinks, such as console, file, memory, Kafka, Foreach, ForeachBatch, and Delta Lake .
- Each streaming query can have exactly one sink, and the type of the sink determines how the output is formatted and written.
- Some sinks support only append mode, which means only new records are written to the sink. Other sinks support update or complete mode, which means the entire result table is rewritten to the sink .
- Some sinks also support watermarking and event-time windows, which are techniques to handle late or out-of-order data in streaming applications .
- To use a sink, we need to specify the sink type, the output mode, and the options for the sink in the `writeStream` method of the streaming DataFrame or Dataset .
- For example, to write the streaming output to a console sink in append mode, we can use the following code:

```scala
val query = streamingDF.writeStream
  .outputMode("append")
  .format("console")
  .start()
```

- To write the streaming output to a file sink in parquet format, we can use the following code:

```scala
val query = streamingDF.writeStream
  .outputMode("append")
  .format("parquet")
  .option("path", "path/to/destination/dir")
  .option("checkpointLocation", "path/to/checkpoint/dir")
  .start()
```

- To write the streaming output to a Kafka sink, we can use the following code:

```scala
val query = streamingDF.selectExpr("topic", "value")
  .writeStream
  .outputMode("append")
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("checkpointLocation", "path/to/checkpoint/dir")
  .start()
```

- To write the streaming output to a custom sink using the Foreach or ForeachBatch APIs, we can use the following code:

```scala
// Using Foreach
val query = streamingDF.writeStream
  .outputMode("update")
  .foreach(new MyForeachWriter())
  .start()

// Using ForeachBatch
val query = streamingDF.writeStream
  .outputMode("update")
  .foreachBatch { (batchDF: DataFrame, batchId: Long) =>
    // Transform and write batchDF
  }
  .start()
```

- To write the streaming output to a Delta Lake table, we can use the following code:

```scala
val query = streamingDF.writeStream
  .format("delta")
  .option("checkpointLocation", "path/to/checkpoint/dir")
  .table("delta_table")
```