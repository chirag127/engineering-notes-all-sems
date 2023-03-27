## Unit 7 - Introducing Structured Streaming

Structured Streaming is a high-level API for stream processing in Apache Spark. It allows you to process data in real-time with the same APIs that you use for batch processing. Here are some key points to understand about Structured Streaming:

- Structured Streaming is built on top of Spark SQL, so you can use familiar SQL-like syntax to process streaming data.

- Structured Streaming provides a DataFrame/ Dataset API, so you can use the same code for both batch and streaming processing.

- Structured Streaming uses a continuous processing model, which means that it processes data as a continuous stream rather than in discrete batches.

- Structured Streaming provides fault-tolerant processing, which means that it can recover from failures and continue processing data without losing any data.

- Structured Streaming supports a variety of data sources, including Kafka, file systems, and socket connections.

- Structured Streaming provides a variety of output modes, including complete mode, append mode, and update mode, which allow you to control how the results of your stream processing are stored.

- Structured Streaming supports windowing and aggregation, which means that you can group data by time windows and perform aggregate operations on the data within each window.

- Structured Streaming provides support for event-time processing, which means that you can process data based on the time that events actually occurred, rather than the time that the data was received.

- Structured Streaming provides integration with Spark's machine learning libraries, which means that you can use machine learning algorithms to process streaming data.

Overall, Structured Streaming is a powerful API for stream processing in Apache Spark. By using familiar APIs and providing fault-tolerant processing, it makes it easy to process data in real-time and build scalable streaming applications.