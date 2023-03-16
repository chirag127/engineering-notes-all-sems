# Structured Streaming Sinks

- Structured Streaming supports numerous sink types natively, including Delta, AWS S3, Google GCS, Azure ADLS, Kafka topics, Kinesis streams, and more.
- Structured Streaming also supports a specialized sink that has the ability to perform arbitrary logic on the output of a streaming query: the `foreachBatch` extension method.
- Sink is the extension of the BaseStreamingSink contract for streaming sinks that can add batches to an output.
- Sink is part of Data Source API V1 and used in Micro-Batch Stream Processing only.
- The number of sinks corresponds to the number of queries because one streaming query can have exactly one streaming sink.
- Structured Streaming uses one `microBatchThread` thread per streaming query.