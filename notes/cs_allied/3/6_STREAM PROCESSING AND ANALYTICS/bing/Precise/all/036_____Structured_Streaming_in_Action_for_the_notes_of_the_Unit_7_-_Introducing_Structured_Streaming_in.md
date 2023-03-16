# Structured Streaming in Action

Structured Streaming is a high-level API for stream processing built on top of the Spark SQL engine. It provides a programming model for processing data in a continuous and incremental manner, with support for event-time processing, late data handling, and other advanced features.

Here are some key points to remember about Structured Streaming:

1. Structured Streaming is built on top of the Spark SQL engine, which means that it can take advantage of the optimizations and features of the SQL engine, such as the Catalyst optimizer and the Tungsten execution engine.

2. Structured Streaming provides a high-level API for defining streaming computations, which makes it easy to express complex streaming logic in a concise and readable manner.

3. Structured Streaming supports event-time processing, which means that it can handle out-of-order data and late data, and can compute results based on the event time of the data, rather than the processing time.

4. Structured Streaming provides exactly-once processing guarantees, which means that it can ensure that each record is processed exactly once, even in the face of failures.

5. Structured Streaming supports a wide range of data sources and sinks, including Kafka, HDFS, and many others.

6. Structured Streaming provides a rich set of built-in operations for manipulating data, including filtering, aggregation, windowing, and many others.

7. Structured Streaming integrates seamlessly with the rest of the Spark ecosystem, including Spark SQL, DataFrames, and Datasets, which makes it easy to combine streaming and batch processing in a single application.

In summary, Structured Streaming is a powerful and flexible API for stream processing, which provides a high-level, easy-to-use programming model, with support for advanced features such as event-time processing and exactly-once processing guarantees. It is built on top of the Spark SQL engine, and integrates seamlessly with the rest of the Spark ecosystem.