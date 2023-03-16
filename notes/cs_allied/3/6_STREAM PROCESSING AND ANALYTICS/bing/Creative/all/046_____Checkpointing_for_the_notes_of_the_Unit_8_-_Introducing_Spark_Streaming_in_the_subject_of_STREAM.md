# Checkpointing for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS

- Checkpointing is a process of writing received records at checkpoint intervals to HDFS or other fault-tolerant file systems.
- Checkpointing helps to develop fault-tolerant and resilient Spark streaming applications that can recover from failures  .
- Checkpointing maintains intermediate state on fault-tolerant compatible file systems like HDFS, ADLS and S3 storage systems.
- To specify the checkpoint in a streaming query, we use the `checkpointLocation` as parameter.
- Checkpointing can store different types of information, such as :
  - Metadata checkpointing: It stores the configuration, incomplete batches, DStream operations, and offsets of the input sources.
  - Data checkpointing: It stores the RDDs of DStreams to cut the lineage of the RDD graph.
  - State checkpointing: It stores the state of stateful transformations like `mapWithState` and `updateStateByKey`.
- Checkpointing has some requirements and best practices, such as :
  - The checkpoint directory must be a HDFS path or a path that implements Hadoop FileSystem API.
  - The checkpoint interval should be a multiple of the batch interval or at least 10 seconds.
  - The checkpoint directory should not be deleted while the streaming application is running.
  - The checkpoint directory should be backed up periodically to avoid data loss.
  - The checkpoint data should be cleaned up manually after the streaming application is stopped.