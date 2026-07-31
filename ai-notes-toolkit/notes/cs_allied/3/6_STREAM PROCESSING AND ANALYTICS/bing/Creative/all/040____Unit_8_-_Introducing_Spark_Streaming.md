## Unit 8 - Introducing Spark Streaming

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
- Spark Streaming can ingest data from various sources, such as Kafka, Flume, Twitter, ZeroMQ, Kinesis, or TCP sockets, and process them using complex algorithms expressed with high-level functions like map, reduce, join, and window.
- Spark Streaming can also integrate with advanced analytics libraries, such as MLlib and GraphX, and write the processed data to various systems, such as HDFS, HBase, Cassandra, or Elasticsearch.
- Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data divided into small batches.
- DStreams can be created either from input data streams from sources such as Kafka, Flume, and Kinesis, or by applying high-level operations on other DStreams.
- Internally, each DStream is represented as a sequence of RDDs, which are Spark's core abstraction for distributed datasets.
- Spark Streaming leverages Spark's fast scheduling capability to perform streaming analytics, by launching a new batch of jobs to process each RDD in the DStream.
- Spark Streaming also provides fault-tolerance guarantees by tracking the lineage of each RDD in the DStream, and automatically recovering from failures and stragglers.
- Spark Streaming supports two types of operations on DStreams: transformations and output operations.
- Transformations are operations that produce a new DStream from one or more input DStreams, such as map, filter, reduceByKey, join, and window.
- Output operations are operations that write data from a DStream to an external system, such as print, saveAsTextFiles, saveAsHadoopFiles, and foreachRDD.
- Spark Streaming also supports stateful operations, such as updateStateByKey and mapWithState, which allow maintaining and updating state information across batches of data.
- Spark Streaming also supports window operations, which allow applying transformations over a sliding window of data, such as window, reduceByWindow, and countByWindow.
- Spark Streaming also supports checkpointing, which is a mechanism to periodically save the state of the streaming computation to a reliable storage system, such as HDFS or S3.
- Checkpointing is useful for ensuring fault-tolerance and enabling stateful and windowed operations.