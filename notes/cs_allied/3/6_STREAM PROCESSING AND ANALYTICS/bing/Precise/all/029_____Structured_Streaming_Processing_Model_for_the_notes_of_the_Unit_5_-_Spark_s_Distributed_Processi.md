### Structured Streaming Processing Model

- Spark Structured Streaming is a stream processing engine built on Spark SQL that processes data incrementally and updates the final results as more streaming data arrives.
- It brought a lot of ideas from other structured APIs in Spark (Dataframe and Dataset) and offered query optimizations similar to SparkSQL.
- The model of Structured Streaming is based on Dataframe and Dataset APIs. Structured Streaming treats a data stream as a table that is being continuously appended.
- Spark’s structured streaming model is an extension built on top of the Apache Spark’s DStreams construct. Therefore, users no longer need to access the RDD blocks directly.
- The structured streaming model utilizes DataFrames, which has the benefits of having a lower latency, a greater throughput, and guaranteed message delivery.
- The Spark SQL engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive.
- You can use the Dataset/DataFrame API in Scala, Java, Python or R to express streaming aggregations, event-time windows, stream-to-batch joins, etc.
- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. You can express your streaming computation the same way you would express a batch computation on static data.
