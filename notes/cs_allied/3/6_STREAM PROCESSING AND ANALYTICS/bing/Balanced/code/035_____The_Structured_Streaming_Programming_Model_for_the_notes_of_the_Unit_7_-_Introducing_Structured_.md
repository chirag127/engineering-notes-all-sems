### The Structured Streaming Programming Model

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine .
- The key idea in Structured Streaming is to treat a live data stream as a table that is being continuously appended   .
- This leads to a new stream processing model that is very similar to a batch processing model   .
- You can express your streaming computation the same way you would express a batch computation on static data .
- You can use the Dataset/DataFrame API to create streaming DataFrames/Datasets from streaming sources such as Kafka, Flume, socket, etc .
- You can apply the same operations on streaming DataFrames/Datasets as on static ones, such as map, filter, join, groupBy, window, etc .
- You can write the results of the streaming computation to streaming sinks such as Kafka, console, memory, etc .
- Spark SQL will run the streaming computation incrementally and continuously update the result as streaming data arrives .
- Spark SQL will also handle the intermediate state and fault recovery of the streaming computation automatically .
- You can monitor the streaming computation using the web UI or the status and progress APIs .