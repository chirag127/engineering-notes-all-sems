# Structured Streaming Sources

- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.
- It allows you to express your streaming computation the same way you would express a batch computation on static data.
- It supports various sources of streaming data, such as Kafka, Kinesis, files, sockets, etc .
- The sources can be classified into two categories: basic sources and advanced sources.
- Basic sources are directly available in the `StreamingContext` API and include file systems and socket connections.
- Advanced sources are available through extra utility classes and include Kafka, Kinesis, Flume, etc.
- Some sources also support different modes of reading data, such as append, complete, or update.
- To use a source, you need to specify the source type, the schema of the data, and the options for the source.
- For example, to read data from a Kafka topic, you can use the following code:

```python
df = spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("subscribe", "topic1")
  .load()
```

- The `df` is a `DataFrame` that represents the stream of data from the source.
- You can apply various transformations and actions on the `df` as you would on a static `DataFrame`.
- You can also write the `df` to a sink, such as a file, a database, or a console.