# Structured Streaming Sources

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- Structured Streaming allows you to express computation on streaming data in the same way you express a batch computation on static data.
- Structured Streaming treats a data stream as a table that is being continuously appended, and runs an incremental query on the unbounded input table.
- Structured Streaming supports various sources of streaming data, such as files, Kafka, sockets, and cloud storage.
- Structured Streaming also supports different output modes, such as append, update, and complete, to specify how the output table should be updated as new data arrives.
- Structured Streaming can write the output of a streaming query to a table, which can be read by another streaming query or a batch query as a source.
- Structured Streaming can handle input that is not an append by throwing an exception or deleting the output and checkpoint and restarting the stream from the beginning.
- Structured Streaming can also integrate with REST API destinations using a custom sink that can handle retries, backpressure, and batching.
- Structured Streaming has support for both Python and SQL in Delta Live Tables.
- Structured Streaming can use Auto Loader, a source that automatically processes new files as they arrive in a cloud storage directory, with the option of also processing existing files.