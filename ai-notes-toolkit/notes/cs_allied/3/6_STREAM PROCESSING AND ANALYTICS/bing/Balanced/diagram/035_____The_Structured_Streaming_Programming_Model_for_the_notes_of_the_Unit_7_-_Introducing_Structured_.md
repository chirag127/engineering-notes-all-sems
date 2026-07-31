### The Structured Streaming Programming Model

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine .
- The key idea in Structured Streaming is to treat a live data stream as a table that is being continuously appended   .
- This leads to a new stream processing model that is very similar to a batch processing model   .
- You can express your streaming computation the same way you would express a batch computation on static data .
- You can use the Dataset/DataFrame API to create streaming DataFrames/Datasets from streaming sources such as Kafka, Flume, socket, etc .
- You can apply any kind of SQL operations on streaming DataFrames/Datasets, such as filtering, joining, aggregating, etc .
- You can write the output of your streaming query to streaming sinks such as console, file, Kafka, etc .
- You can also use the low-level API to manipulate the streaming query execution and handle late or out-of-order data .
- Structured Streaming provides end-to-end exactly-once fault-tolerance guarantees through checkpointing and write-ahead logs .
- Structured Streaming also supports event-time processing and watermarking to handle late data .