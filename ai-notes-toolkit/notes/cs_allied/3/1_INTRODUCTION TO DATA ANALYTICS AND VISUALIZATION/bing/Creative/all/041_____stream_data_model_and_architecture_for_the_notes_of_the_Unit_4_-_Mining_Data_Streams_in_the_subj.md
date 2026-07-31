# Stream Data Model and Architecture

## Stream Data Model
- A stream data model is a way of representing data that arrives continuously from various sources and needs to be processed in real time.
- In a stream data model, data is not stored in a conventional database, but rather processed on the fly as it arrives.
- A stream data model has two main characteristics:
  - Data is transient: data is only available for a short period of time and if it is not processed immediately or stored, then it is lost forever.
  - Data is unbounded: data has no predefined size or end, and can grow indefinitely over time.

## Stream Data Architecture
- A stream data architecture is an information technology framework that puts the focus on processing data in motion and treats extract-transform-load (ETL) batch processing as just one more event in a continuous stream of events.
- A stream data architecture has three basic components:
  - An aggregator that gathers event streams and batch files from a variety of data sources, such as sensors, logs, web applications, etc.
  - A broker that makes data available for consumption and distributes it to different consumers, such as analytics engines, databases, dashboards, etc. A broker can also provide buffering, partitioning, and replication of data streams.
  - An analytics engine that analyzes the data, correlates values, and generates insights, alerts, or actions. An analytics engine can also perform transformations, aggregations, joins, or windowing of data streams.

## Examples of Stream Data Architecture
- Some examples of stream data architecture are:
  - Apache Kafka: a distributed streaming platform that provides a broker for data streams, and allows producers and consumers to communicate via topics and partitions. Kafka also provides a stream processing framework called Kafka Streams, and a connector platform called Kafka Connect.
  - Apache Spark: a unified analytics engine that supports both batch and stream processing. Spark provides a stream processing framework called Spark Streaming, which can consume data from various sources, such as Kafka, Flume, or HDFS, and process it using Spark's core APIs, such as RDDs, DataFrames, or Datasets.
  - Apache Flink: a distributed processing engine that supports both batch and stream processing. Flink provides a stream processing framework called Flink Streaming, which can consume data from various sources, such as Kafka, RabbitMQ, or AWS Kinesis, and process it using Flink's core APIs, such as DataStream, DataSet, or Table.