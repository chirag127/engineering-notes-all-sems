### The Structured Streaming Programming Model

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine .
- The key idea in Structured Streaming is to treat a live data stream as a table that is being continuously appended   .
- This leads to a new stream processing model that is very similar to a batch processing model   .
- You can express your streaming computation the same way you would express a batch computation on static data .
- You can use the Dataset/DataFrame API to create streaming DataFrames/Datasets from streaming sources such as Kafka, Flume, and more .
- You can apply the same operations on streaming DataFrames/Datasets as on static ones, such as filtering, aggregating, joining, etc .
- You can write the results of your streaming computation to streaming sinks such as Kafka, memory, console, etc .
- Spark SQL will run your streaming computation incrementally and continuously, updating the final result as streaming data arrives .
- Spark SQL will also handle the complexities of stream processing, such as data consistency, fault tolerance, and late data .
- You can monitor the progress and performance of your streaming computation using the web UI or the Structured Streaming APIs .