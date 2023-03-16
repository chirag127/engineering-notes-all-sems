# Checkpointing for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS

- Checkpointing is a process of writing received records at checkpoint intervals to HDFS or other HDFS compatible file systems to build fault-tolerant and resilient Spark applications.
- Checkpointing is a requirement for streaming applications that must operate 24/7 and recover from failures.
- Checkpointing can be of two types: metadata checkpointing and data checkpointing.
- Metadata checkpointing stores the information about the streaming computation, such as:
  - Incomplete batches: the batches that are received but not yet processed.
  - Configuration: the configuration that was set up for the streaming application, such as maxFilesPerTrigger, maxOffsetsPerTrigger, etc.
  - DStream operations: the information about the transformations and output operations applied on the DStreams.
  - Batch time and offsets: the information about the batch time intervals and the offsets of the data that have been processed or will be processed.
- Data checkpointing stores the intermediate state of the stateful transformations, such as mapWithState, updateStateByKey, reduceByKeyAndWindow, etc.
- Data checkpointing is necessary when the stateful transformations have long lineage chains that may cause performance issues or out-of-memory errors.
- Data checkpointing can be synchronous or asynchronous.
  - Synchronous checkpointing means that the state is checkpointed every time the output is generated for a batch. This ensures that the state is always consistent with the output, but it may increase the end-to-end latency.
  - Asynchronous checkpointing means that the state is checkpointed periodically, independent of the output generation. This may reduce the end-to-end latency, but it may also introduce some inconsistency between the state and the output in case of failures.
- Checkpointing can be enabled by setting the checkpoint directory in the streaming context or the query .
- Checkpointing can be disabled by setting the checkpoint directory to null or empty string.
- Checkpointing should be used with care, as it may incur some overhead and affect the performance of the streaming application.