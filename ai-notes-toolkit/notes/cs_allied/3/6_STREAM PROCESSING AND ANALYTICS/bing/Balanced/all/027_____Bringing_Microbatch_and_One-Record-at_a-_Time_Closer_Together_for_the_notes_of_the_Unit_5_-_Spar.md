# Bringing Microbatch and One-Record-at-a-Time Closer Together

- Spark Streaming is a framework that allows processing of streaming data using Spark's distributed processing model.
- Spark Streaming uses a microbatch approach, where incoming data is collected in small batches and processed by Spark jobs.
- A microbatch is a subset of data that is created based on a time window, rather than a number of records.
- Microbatching has some advantages over one-record-at-a-time processing, such as:
  - Higher throughput and lower latency, as Spark can leverage its batch processing optimizations and parallelism.
  - Fault tolerance and exactly-once semantics, as Spark can track the state of each microbatch and recover from failures.
  - Integration with batch and interactive processing, as Spark can use the same APIs and libraries for streaming and non-streaming data.
- However, microbatching also has some limitations, such as:
  - Inability to handle late or out-of-order data, as Spark assumes that each microbatch is complete and ordered.
  - Inflexibility to handle complex event processing, as Spark cannot apply operations on individual records or across microbatches.
  - Overhead of scheduling and launching Spark jobs for each microbatch, which can affect the performance and scalability.
- To overcome these limitations, Spark Streaming has introduced some features that bring microbatch and one-record-at-a-time processing closer together, such as:
  - Structured Streaming, which is a high-level API that allows defining streaming queries using SQL or DataFrames, and handles the details of microbatching, state management, and output modes.
  - Watermarks and window operations, which allow handling late and out-of-order data by specifying a threshold of how late the data can be and applying aggregations over sliding time windows.
  - Continuous processing mode, which is an experimental feature that allows processing data as soon as it arrives, without waiting for microbatches, and achieves sub-millisecond latency.