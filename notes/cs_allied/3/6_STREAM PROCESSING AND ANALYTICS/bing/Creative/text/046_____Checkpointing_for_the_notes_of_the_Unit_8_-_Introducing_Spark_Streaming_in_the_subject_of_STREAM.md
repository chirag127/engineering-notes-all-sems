### Checkpointing for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS

- Checkpointing is a process of writing received records at checkpoint intervals to a fault-tolerant compatible file system like HDFS, ADLS or S3 .
- Checkpointing helps to develop fault-tolerant and resilient Spark streaming applications that can recover from failures  .
- Checkpointing can store the following types of information :
  - Metadata checkpointing: It stores the configuration, DStream operations, incomplete batches and offsets of the input sources of the streaming application.
  - Data checkpointing: It stores the RDDs of DStreams to cut off the lineage of the RDDs and reduce the recovery time.
  - State checkpointing: It stores the state of stateful transformations like mapWithState and updateStateByKey to enable exactly-once semantics.
- To specify the checkpoint in a streaming query, we use the checkpointLocation as a parameter.
- To enable checkpointing in a streaming context, we use the streamingContext.checkpoint(directory) method.
- Checkpointing has some trade-offs and limitations:
  - Checkpointing introduces some overhead in terms of performance and disk space.
  - Checkpointing does not guarantee zero data loss in case of a failure, as some data may be in transit or in memory.
  - Checkpointing does not preserve the state of external systems like Kafka or Flume that are involved in the streaming application.