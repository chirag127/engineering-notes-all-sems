### Structured Streaming Processing Model

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine .
- The model of Structured Streaming is based on Dataframe and Dataset APIs.
- Structured Streaming treats a data stream as a table that is being continuously appended.
- The basic idea of Structured Streaming is to use a high-level declarative API to specify the input sources, the desired transformations, and the output sinks for the streaming computation .
- Structured Streaming provides two types of output modes: append mode and update mode .
- Append mode is the default mode, where only the new rows appended to the result table since the last trigger are written to the sink .
- Update mode is where only the rows that were updated in the result table since the last trigger are written to the sink .
- Structured Streaming also supports event-time processing, watermarking, stateful aggregations, and join operations .
- Structured Streaming uses the same underlying architecture as Spark so that you can take advantage of all the performance and cost optimizations built into the Spark engine.
- Structured Streaming can handle various types of input sources, such as Kafka, Flume, socket, file, etc .
- Structured Streaming can also write the output to various types of sinks, such as console, file, memory, Kafka, etc .
- Structured Streaming can be integrated with Spark MLlib, Spark GraphX, and Spark R for advanced analytics.