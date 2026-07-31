# Spark’s Fault-Tolerance Guarantees

- Spark Streaming is a framework for processing data streams in real time using Spark’s distributed computing engine.
- Spark Streaming provides fault-tolerance guarantees for both the input data and the processing logic, ensuring that the results are consistent and reliable even in the presence of failures.
- Spark Streaming’s fault-tolerance guarantees are based on the following principles:

  - **Input data is tracked using offsets**: Spark Streaming uses offsets to keep track of the position of each input data source, such as Kafka, Flume, or files. Offsets are periodically checkpointed to a reliable storage system, such as HDFS, to ensure that the input data can be recovered in case of a failure.
  - **Processing logic is expressed using deterministic operations**: Spark Streaming allows the user to express the processing logic using deterministic operations on RDDs, such as map, filter, reduce, join, etc. These operations are guaranteed to produce the same results regardless of the number of times they are executed, as long as the input data is the same.
  - **Output data is written using idempotent or transactional sinks**: Spark Streaming supports writing the output data to various sinks, such as files, databases, or message queues. These sinks are either idempotent, meaning that they can handle duplicate writes without affecting the final result, or transactional, meaning that they can atomically commit or abort a batch of writes.
  - **Worker fault-tolerance is achieved using lineage and replication**: Spark Streaming leverages Spark’s resilience model to handle worker failures. Each RDD maintains its lineage, or the sequence of operations that produced it, and can be recomputed from the input data if needed. Additionally, some RDDs, such as the ones that store state information, are replicated across multiple workers to provide fast recovery.

- Due to Spark Streaming’s fault-tolerance guarantees, it can provide exactly-once semantics for all transformations and outputs, even if a worker fails and some data gets reprocessed, the final result will be the same as if the data were processed exactly once   .