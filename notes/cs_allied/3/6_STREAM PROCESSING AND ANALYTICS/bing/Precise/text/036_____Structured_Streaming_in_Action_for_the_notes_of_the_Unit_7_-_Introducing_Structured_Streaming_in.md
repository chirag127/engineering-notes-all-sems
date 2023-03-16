### Structured Streaming in Action

- Structured Streaming is a stream processing framework built on top of the Apache Spark SQL engine .
- It uses existing DataFrame APIs in Spark, so almost all familiar operations are supported in streaming .
- Structured Streaming is fault-tolerant and implemented with check-pointing and write-ahead logs .
- It allows you to take the same operations that you perform in batch mode using Spark’s structured APIs and run them in a streaming fashion .
- This can reduce latency and allow for incremental processing .
- In Structured Streaming, a data stream is treated as a table that is being continuously appended .
- This leads to a stream processing model that is very similar to a batch processing model .
- You express your streaming computation as a standard batch-like query as on a static table, but Spark runs it as an incremental query on the unbounded input .
- The Structured Streaming engine performs the computation incrementally and continuously updates the result as streaming data arrives .