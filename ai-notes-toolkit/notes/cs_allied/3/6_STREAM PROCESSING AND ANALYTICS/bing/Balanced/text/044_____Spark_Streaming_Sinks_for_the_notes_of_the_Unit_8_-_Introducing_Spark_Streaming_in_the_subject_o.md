### Spark Streaming Sinks

- Spark Streaming Sinks are the components that store the output of a streaming query to an external storage system.
- Spark Structured Streaming supports different types of sinks, such as console, file, memory, Kafka, Foreach, ForeachBatch, and Delta Lake.
- The choice of sink depends on the output mode of the streaming query, the format of the data, and the requirements of the application.
- Some of the common sinks are:

  - Console sink: Displays the content of the DataFrame to the console. Useful for debugging and testing purposes. Supports only append and complete output modes.
  - File sink: Writes the output of the streaming query to a file system, such as HDFS, S3, or local disk. Supports various file formats, such as CSV, JSON, Parquet, and ORC. Supports append and update output modes.
  - Memory sink: Stores the output of the streaming query as an in-memory table that can be queried using Spark SQL or the DataFrame API. Useful for interactive analysis and testing. Supports only complete output mode.
  - Kafka sink: Writes the output of the streaming query to one or more Kafka topics. Supports only append output mode. Requires the `spark-sql-kafka` library.
  - Foreach sink: Allows the user to specify a custom logic to process each row of the output. Useful for complex transformations or writing to custom sinks. Supports all output modes. Requires the user to implement the `ForeachWriter` interface.
  - ForeachBatch sink: Allows the user to specify a custom logic to process each micro-batch of the output as a DataFrame. Useful for batch operations or writing to multiple sinks. Supports all output modes. Requires the user to provide a function that takes a DataFrame and a batch ID as parameters.
  - Delta Lake sink: Writes the output of the streaming query to a Delta Lake table. Supports append, update, and complete output modes. Requires the `delta-core` library.

: https://medium.com/expedia-group-tech/apache-spark-structured-streaming-output-sinks-3-of-6-ed3247545fbc
: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html