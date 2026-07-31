### Structured Streaming Sources

- Structured Streaming is a stream processing engine built on Spark SQL that processes data incrementally and updates the final results as more streaming data arrives.
- Structured Streaming provides two types of sources: built-in sources and external sources.
- Built-in sources are sources directly available in the SparkSession API. Examples: file systems, socket connections, and rate (for testing) .
- External sources are sources like Kafka, Kinesis, etc. that are available through extra utility classes or third-party libraries .
- To use an external source, you need to add the corresponding dependency to your project and specify the fully qualified class name of the source provider as the format parameter .
- Some of the common options for external sources are: 
  - **topic**: The name of the topic to read from or write to .
  - **bootstrap.servers**: A list of host/port pairs to use for establishing the initial connection to the Kafka cluster .
  - **startingOffsets**: The start point when a query is started, either "earliest" which is from the earliest offsets, "latest" which is just from the latest offsets, or a JSON string specifying a starting offset for each partition .
  - **endingOffsets**: The end point when a query is terminated, either "latest" which is up to the latest offsets, or a JSON string specifying an ending offset for each partition .
- Structured Streaming can also write data to REST API destinations using the Databricks REST API Sink library .
- The library allows you to specify the REST API endpoint, the HTTP method, the headers, and the payload for each record in the streaming data .
- The library also handles retries, backpressure, and batching for efficient and reliable data delivery .