# The Spark Streaming Programming Model

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams. Data can be ingested from many sources like Kafka, Flume, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.

- By default, Spark structured streaming queries are executed using micro batch processing model. The model treats streaming data as batch table, but in micro batches. Here the spark engine checks the input source periodically for new data arrival since the last micro batch ended.

- Spark’s single execution engine and unified programming model for batch and streaming lead to some unique benefits over other traditional streaming systems. In particular, four major aspects are: Fast recovery from failures and stragglers, Better load balancing and resource usage.

- Key reason behind Spark Streaming’s rapid adoption is the unification of disparate data processing capabilities.

- The Spark SQL engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive. You can use the Dataset/DataFrame API in Scala, Java, Python or R to express streaming aggregations, event-time windows, stream-to-batch joins, etc.

- Spark Streaming provides a high-level abstraction called discretized stream or DStream, which represents a continuous stream of data. DStreams can be created either from input data streams from sources such as Kafka, and Kinesis, or by applying high-level operations on other DStreams.