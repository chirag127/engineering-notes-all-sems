### Checkpointing for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS

- Checkpointing is a process of writing received records at checkpoint intervals to HDFS or other compatible file systems.
- Checkpointing is a requirement for streaming applications that must operate 24/7 and be fault-tolerant .
- Checkpointing helps to recover from failures by storing intermediate state and metadata on persistent storage .
- Checkpointing can be synchronous or asynchronous. Synchronous checkpointing blocks the processing of the next batch until the current batch is checkpointed. Asynchronous checkpointing allows the processing of the next batch to start while the current batch is being checkpointed in the background.
- Checkpointing can be enabled by setting a checkpoint directory in the streaming context or the query . For example, in Scala:

```scala
// Create a streaming context with a checkpoint directory
val ssc = new StreamingContext(sparkConf, Seconds(1))
ssc.checkpoint("hdfs://...")

// Create a streaming query with a checkpoint location
val query = df.writeStream
  .outputMode("append")
  .format("console")
  .option("checkpointLocation", "hdfs://...")
  .start()
```

- Checkpointing can store different types of information, such as:
  - Metadata: It includes the configuration, DStream operations, incomplete batches, etc.
  - Received Data: It includes the raw data received from various sources, such as Kafka, Flume, etc.
  - State Data: It includes the state information of stateful transformations, such as mapWithState, updateStateByKey, etc.
- Checkpointing intervals depend on the type of information and the application requirements. For example, metadata checkpointing should be done frequently (every few seconds or minutes), received data checkpointing should be done at least once per batch interval, and state data checkpointing should be done at least once in 10 batch intervals .