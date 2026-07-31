
### Checkpointing for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS

1. Checkpointing is a process of saving the state of a streaming application at a particular point in time. 
2. This allows the application to be restarted from the same point in time if it fails or is stopped. 
3. Checkpointing is an important part of any streaming application, as it ensures that data is not lost due to system or application failure. 
4. Spark Streaming provides a built-in mechanism for checkpointing, which can be used to save the state of a streaming application. 
5. Checkpointing is done by writing the application state to a reliable storage system, such as HDFS or S3. 
6. Checkpointing can be enabled by setting the `spark.streaming.checkpoint.dir` parameter in the Spark configuration. 
7. Checkpointing can also be used to save the state of a streaming application across multiple nodes in a cluster. 
8. This allows for a more robust and fault-tolerant streaming application.