## Unit 7 - Introducing Structured Streaming

Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. It allows you to express your streaming computations the same way you would express a batch computation on static data. The Spark engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive.

Some key features of Structured Streaming include:
- **Ease of use**: You can express your streaming computation using the same familiar DataFrame and Dataset APIs that you use for batch processing.
- **Event-time processing**: You can handle out-of-order and late data using event-time processing and watermarking.
- **Exactly-once processing**: Structured Streaming guarantees end-to-end exactly-once processing using checkpointing and write-ahead logs.
- **Integration with other data sources and sinks**: You can read data from and write data to a variety of data sources and sinks, including Kafka, HDFS, and more.

Structured Streaming is a powerful tool for building real-time data processing pipelines and is an essential component of any modern data architecture. It is a great way to unlock the value of your data and make it available to your users in real-time.