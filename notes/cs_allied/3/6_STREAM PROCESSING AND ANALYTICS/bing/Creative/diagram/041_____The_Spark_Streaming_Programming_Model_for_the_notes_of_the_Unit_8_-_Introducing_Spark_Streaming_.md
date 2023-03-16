### The Spark Streaming Programming Model

- Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.
- Spark Streaming provides a high-level abstraction called **discretized stream** or **DStream**, which represents a continuous stream of data.
- DStreams can be created either from input data sources such as Kafka, Flume, Kinesis, or TCP sockets, or by applying high-level operations on other DStreams .
- DStreams are internally represented as a sequence of **RDDs** (Resilient Distributed Datasets), which are Spark's core abstraction for distributed data.
- Each RDD in a DStream contains data from a certain interval, called a **batch interval**.
- Spark Streaming processes the live data streams using a **micro-batch processing model**, where the streaming computation is divided into small batches that are executed periodically  .
- The batch interval can be configured to control the latency and throughput of the streaming application.
- Spark Streaming's execution model is based on Spark's single execution engine and unified programming model for batch and streaming, which leads to some unique benefits over other traditional streaming systems .
  - Fast recovery from failures and stragglers, as Spark can leverage its lineage-based fault tolerance mechanism.
  - Better load balancing and resource usage, as Spark can dynamically adjust the degree of parallelism based on the workload.
  - Seamless integration with batch and interactive queries, as Spark can run SQL queries and machine learning algorithms on both static and streaming data.
- Spark Streaming also supports a newer high-level API called **structured streaming**, which is built on Spark SQL and the Dataset/DataFrame API.
- Structured streaming allows users to express streaming computations using familiar concepts such as tables, columns, and SQL queries.
- Structured streaming treats streaming data as an unbounded table that is continuously appended with new rows, and executes incremental and continuous queries on the table.
- Structured streaming supports various streaming operations such as aggregations, event-time windows, stream-to-batch joins, etc.
- Structured streaming also provides an end-to-end **exactly-once** semantics guarantee, which ensures that each record will be processed exactly once, even in the presence of failures.