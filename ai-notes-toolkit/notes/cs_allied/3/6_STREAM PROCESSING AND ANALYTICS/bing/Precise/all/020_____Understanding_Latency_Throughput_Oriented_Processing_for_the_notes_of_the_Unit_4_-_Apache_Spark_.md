# Understanding Latency Throughput Oriented Processing

Latency and throughput are two important metrics in the performance of a stream-processing system. Latency refers to the time it takes for a single data record to be processed, while throughput refers to the number of data records that can be processed in a given time period.

In a latency-oriented processing system, the focus is on minimizing the time it takes to process each individual data record. This is important in applications where timely processing of data is critical, such as in real-time fraud detection or stock trading.

On the other hand, in a throughput-oriented processing system, the focus is on maximizing the number of data records that can be processed in a given time period. This is important in applications where large volumes of data need to be processed quickly, such as in log analysis or data aggregation.

Apache Spark is a stream-processing engine that can be configured for both latency and throughput-oriented processing. It achieves low latency by processing data in micro-batches, which allows for near real-time processing of data. At the same time, it can achieve high throughput by processing data in parallel across multiple nodes in a cluster.

In summary, understanding the trade-off between latency and throughput is important when designing a stream-processing system. Apache Spark provides the flexibility to balance these two metrics depending on the specific needs of the application.