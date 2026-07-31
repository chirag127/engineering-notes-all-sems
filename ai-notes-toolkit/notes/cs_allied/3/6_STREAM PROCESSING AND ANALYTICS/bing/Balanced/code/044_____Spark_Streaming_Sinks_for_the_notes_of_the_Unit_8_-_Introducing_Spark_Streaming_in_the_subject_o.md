### Spark Streaming Sinks

- Spark Streaming Sinks are the components that store the output of a streaming query to an external storage system.
- Spark Structured Streaming supports the following types of sinks:
  - Console sink: Displays the content of the DataFrame to the console. Useful for debugging and testing purposes. 
  - File sink: Writes the output of the streaming query to a file system, such as HDFS, S3, or local file system. Supports various file formats, such as text, csv, json, parquet, orc, etc.  
  - Kafka sink: Writes the output of the streaming query to a Kafka topic. Supports both batch and streaming queries.  
  - Foreach sink: Allows the user to specify a custom logic to process each row of the output. Useful for integrating with external systems that are not supported by built-in sinks.  
  - Memory sink: Stores the output of the streaming query in memory as a table. Useful for interactive queries and testing purposes.  
  - Databricks Delta sink: Writes the output of the streaming query to a Databricks Delta table. Supports ACID transactions, schema evolution, and time travel. 
- Spark Streaming Sinks can be specified using the `writeStream` method on a DataFrame or Dataset, followed by the `format` method to specify the sink type, and the `option` or `options` methods to specify any additional configuration parameters. For example, to write the output of a streaming query to a Kafka topic, one can use the following code:

```scala
val df = ... // streaming DataFrame
df.writeStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("topic", "topic1")
  .start()
```

- Spark Streaming Sinks can also be specified using the `save` method on a DataFrame or Dataset, followed by the `mode` method to specify the output mode, and the `option` or `options` methods to specify any additional configuration parameters. For example, to write the output of a batch query to a Kafka topic, one can use the following code:

```scala
val df = ... // batch DataFrame
df.write
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("topic", "topic1")
  .save()
```

- Spark Streaming Sinks support different output modes, such as `append`, `update`, and `complete`, depending on the type of the sink and the query. Output modes define how the output of a streaming query is updated as new data arrives. For example, `append` mode only adds new rows to the output, `update` mode only updates the rows that have changed, and `complete` mode rewrites the entire output with every update.  
- Spark Streaming Sinks can be monitored and managed using the `StreamingQuery` object returned by the `start` method. The `StreamingQuery` object provides methods to get the query name, id, status, progress, and exception, as well as to stop, await termination, or restart the query.