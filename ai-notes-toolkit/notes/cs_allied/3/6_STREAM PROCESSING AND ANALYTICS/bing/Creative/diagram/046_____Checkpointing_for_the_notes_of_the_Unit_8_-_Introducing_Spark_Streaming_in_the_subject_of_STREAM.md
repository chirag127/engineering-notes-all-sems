### Checkpointing for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS

- Checkpointing is a process of writing received records at checkpoint intervals to HDFS or other HDFS compatible file systems to build fault-tolerant and resilient Spark applications.
- Checkpointing is a requirement for streaming applications that must operate 24/7 and recover from failures without data loss.
- Checkpointing can be of two types: metadata checkpointing and data checkpointing.
- Metadata checkpointing stores the information about the streaming computation, such as:
  - Incomplete batches: the batches that are received but not yet processed.
  - Configuration: the configuration that was set up for the streaming application, such as maxFilesPerTrigger, maxOffsetsPerTrigger, etc.
  - DStream operations: the information about the transformations and output operations applied on the DStreams.
  - Offsets: the information about the offsets consumed by Kafka or other sources.
- Data checkpointing stores the intermediate state of stateful transformations, such as mapWithState, updateStateByKey, window, etc.
- Data checkpointing can be synchronous or asynchronous.
  - Synchronous checkpointing writes the state to the checkpoint directory as part of the query execution and blocks the query until the write is complete.
  - Asynchronous checkpointing writes the state to the checkpoint directory asynchronously and does not block the query execution.
  - Asynchronous checkpointing can reduce end-to-end latencies without sacrificing fault-tolerance guarantees, but with a minor cost of higher restart delays.
  - Structured Streaming uses synchronous checkpointing by default, but it can be enabled by setting the configuration spark.sql.streaming.stateStore.mode to async.
- Checkpointing can be enabled by setting the checkpoint directory in the streaming context or the query.
  - For DStream-based API, use streamingContext.checkpoint(checkpointDirectory).
  - For Dataset/DataFrame-based API, use query.writeStream.option("checkpointLocation", checkpointDirectory).