### Structured Streaming Processing Model

- Spark Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- The model of Structured Streaming is based on Dataframe and Dataset APIs.
- Structured Streaming treats a data stream as a table that is being continuously appended.
- It is an improved Spark Streaming engine for handling streaming data.
- Built as part of Spark 2.0 on the Spark SQL library, Structured Streaming uses the Dataframe or Dataset APIs, offering a higher abstraction level than Spark Streaming RDDs.
- It processes data incrementally and updates the final results as more streaming data arrives.
- It brought a lot of ideas from other structured APIs in Spark (Dataframe and Dataset) and offered query optimizations similar to SparkSQL.
- You can express your streaming computation the same way you would express a batch computation on static data.
- Spark Structured Streaming provides the same structured APIs (DataFrames and Datasets) as Spark so that you don’t need to develop on or maintain two different technology stacks for batch and streaming.
- In addition, unified APIs make it easy to migrate your existing batch Spark jobs to streaming jobs.