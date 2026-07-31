### Structured Streaming Processing Model

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine .
- Structured Streaming uses the Dataframe and Dataset APIs to express streaming computations the same way as batch computations on static data  .
- Structured Streaming treats a data stream as a table that is being continuously appended. This allows users to query the stream as a table using SQL or DataFrame/Dataset operations.
- Structured Streaming provides two types of output modes: append mode and update mode . Append mode only writes new records to the output sink, while update mode writes both new and updated records to the output sink.
- Structured Streaming supports various types of input sources and output sinks, such as Kafka, Flume, HDFS, S3, JDBC, console, memory, etc  .
- Structured Streaming guarantees end-to-end exactly-once fault-tolerance through checkpointing and write-ahead logs  . Checkpointing periodically saves the state of the streaming computation to a reliable storage system, while write-ahead logs record every data item that is received by the streaming application before processing it.