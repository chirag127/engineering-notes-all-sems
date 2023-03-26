 Here is the content in Markdown format without any emojis or external links as per your requirements:

## Unit 7 - Introducing Structured Streaming

1. Structured Streaming is a new streaming API introduced in Spark 2.0. It allows you to process data one record at a time as opposed to batch processing. This leads to lower latency and more meaningful error handling.
2. The key concepts in Structured Streaming are:
- Stream - An unbounded sequence of structured data records.
- Checkpoint - Periodically saves the application state to provide fault tolerance and allow stateful processing.
- Trigger - Processes the data once the checkpoint interval is reached or enough data has arrived.
3. The main components of a Structured Streaming program are:
- Stream source - Reads data from sockets, Kafka, Flume, Kinesis, etc.
- Stream query - Continuously processes input streams using SQL or the Dataset/DataFrame API.
- Sink - Writes the output to file systems, databases, dashboards, etc.
4. Some of the important points to keep in mind are:
- Micro-batch processing - Data is processed in small batches to provide low latency and throughput.
- Fault tolerance - Checkpoints and write-ahead logs provide fault tolerance. In the event of failures, processing can resume from the last checkpoint.
- Event time and processing time - You can operate on event time or processing time. Event time is useful for out-of-order data. Watermarks can be used to keep track of progress in event time.
- Stateful and stateless processing - You can perform stateful and stateless processing using maps, reduces, aggregations, joins, etc. State is maintained internally and recovered using checkpoints.