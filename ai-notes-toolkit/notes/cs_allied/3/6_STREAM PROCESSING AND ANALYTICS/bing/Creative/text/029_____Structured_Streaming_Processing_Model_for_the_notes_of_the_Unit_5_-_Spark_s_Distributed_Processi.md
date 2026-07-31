### Structured Streaming Processing Model

- Structured Streaming is a **scalable and fault-tolerant stream processing engine** built on the Spark SQL engine .
- Structured Streaming uses the **Dataframe and Dataset APIs** to express streaming computations the same way as batch computations on static data  .
- Structured Streaming treats a data stream as a **table that is being continuously appended**. This allows users to query the stream as a table, using SQL or DataFrame/Dataset operations  .
- Structured Streaming provides two types of output modes: **append** and **update**. Append mode only adds new rows to the result table, while update mode updates existing rows and adds new rows based on the query .
- Structured Streaming supports various sources and sinks for streaming data, such as Kafka, Flume, HDFS, S3, JDBC, console, memory, etc .
- Structured Streaming leverages **Spark SQL's Catalyst optimizer** and **Tungsten execution engine** to perform various optimizations, such as predicate pushdown, projection pruning, code generation, etc .
- Structured Streaming also provides **exactly-once** guarantees for end-to-end pipelines, by tracking the progress of the stream using **offsets** and **checkpoints**  .
- Structured Streaming enables users to monitor the streaming queries using **web UI** and **structured query status API** .