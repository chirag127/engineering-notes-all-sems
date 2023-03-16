# Time-Based Stream Processing with Spark SQL

- Time-based stream processing is a technique to process data streams that have a temporal dimension, such as sensor readings, web logs, or social media posts.
- Time-based stream processing can be used for various purposes, such as detecting anomalies, aggregating statistics, or performing complex event processing.
- Spark SQL is a module of Apache Spark that provides a unified interface for querying structured and semi-structured data using SQL or a DataFrame API.
- Spark SQL supports stream processing through Structured Streaming, which is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine .
- Structured Streaming allows ingesting real-time data from various sources, such as files, Azure Event Hubs, or Azure IoT Hubs, and applying SQL queries or DataFrame operations on them.
- Structured Streaming also supports various output modes, such as updating a table, appending new records, or writing to a file or a sink.
- Structured Streaming uses a concept of triggers to control the frequency and timing of batch processing. A trigger defines when the engine should process the next set of data available in the input source .
- There are three types of triggers in Structured Streaming: default, processing-time, and event-time .
  - The default trigger processes data as soon as it arrives, without any delay. This is suitable for near-real time processing or low-latency applications.
  - The processing-time trigger processes data at a fixed interval, such as every 5 minutes or every hour. This is suitable for periodic processing or refreshing databases.
  - The event-time trigger processes data based on the timestamps embedded in the data, such as the event creation time or the ingestion time. This is suitable for handling out-of-order or late-arriving data, or performing window-based aggregations.
- To configure the trigger for a Structured Streaming query, one can use the `trigger` method of the `DataStreamWriter` or the `DataStreamReader` classes, and specify the trigger type and the interval (if applicable) .
- For example, the following code snippet shows how to create a Structured Streaming query that reads data from a file source, applies a simple filter, and writes the output to a console sink, using a processing-time trigger of 10 seconds:

```python
# Read data from a file source
df = spark.readStream.format("csv").load("/path/to/input")

# Apply a filter
df = df.filter(df["value"] > 10)

# Write the output to a console sink
df.writeStream.format("console").trigger(processingTime="10 seconds").start()
```