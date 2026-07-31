 Here are the points on Checkpointing for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS:

### Checkpointing

- Checkpointing is a mechanism to save the state of a streaming application periodically.
- This acts as a fail-safe and in case of any failure, the application can restart from the last saved state rather than processing the data from scratch again.
- This helps to achieve exactly-once processing semantics.
- The checkpoint data is stored in a reliable, fault-tolerant storage like HDFS.
- The checkpoint interval can be configured based on the application's requirements. A higher interval leads to faster processing but more data repetition in case of failure whereas a lower interval leads to slower processing but less data loss.
- The state stored in checkpoints includes:
-- Offset ranges for input DStreams
-- State of internal variables and aggregations

- To enable checkpointing, we need to call `ssc.checkpoint("checkpoint directory")`. Here, `ssc` is the `StreamingContext` object and `checkpoint directory` refers to the directory in fault-tolerant storage where checkpoint data will be stored.
- Checkpointing incurs some overhead in processing so we need to make a trade-off between checkpoint interval and application performance based on the application's requirements.